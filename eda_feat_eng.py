import pandas as pd
from datetime import datetime
import os
import neurokit2 as nk
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.stats import ttest_ind
from scipy.stats import shapiro


# Extract all csv files from the directory
def extract_csv_files(directory):
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files


directory = 'data'
csv_files = extract_csv_files(directory)


eda_dataframes = []
for file in csv_files:
    df = pd.read_csv(file, skiprows=2)
    df = df.iloc[:, :4]

    if 'uS' in df.columns:
        if 'LeftRoom' in file:
            df['Room'] = 1
        elif 'RightRoom' in file:
            df['Room'] = 2
        else:
            df['Room'] = None
        
        df['datetime'] = pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d %H:%M:%S.%f')
        df['date_hour'] = df['datetime'].dt.strftime('%Y-%m-%d %H:00:00')
        df['time'] = df['datetime'].dt.strftime('%H:%M:%S')
        df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
    
        eda_dataframes.append(df)
    else:
        print(f"File {file} does not contain 'uS' column.")


# Participant Registry
registry_path = 'data/Participant Registry Final.xlsx'
registry_df = pd.read_excel(registry_path)

registry_df['Start Date & Time'] = pd.to_datetime(registry_df['Start Date & Time'], format='%Y/%m/%d %H:%M:%S')
registry_df['date_hour'] = registry_df['Start Date & Time'].dt.strftime('%Y-%m-%d %H:00:00')
registry_df['Task start time'] = pd.to_datetime(registry_df['Task start time'], format='%H:%M:%S').dt.time
registry_df['Task end time'] = pd.to_datetime(registry_df['Task end time'], format='%H:%M:%S').dt.time

# Merge each eda_df with the registry_df on 'date_hour' and 'Room'
filtered_dataframes = []
for eda_df in eda_dataframes:
    merged_df = pd.merge(eda_df, registry_df, on=['date_hour', 'Room'], how='left')
    # Cut the data to the task start and end time
    if merged_df['Participant ID'].notna().all():
        filtered_df = merged_df[(merged_df['time'] >= merged_df['Task start time']) & (merged_df['time'] <= merged_df['Task end time'])]
        filtered_dataframes.append(filtered_df)


# Clean and standardize the 'uS' column using nk.eda_clean for each dataframe
preprocessed_dataframes = []

scaler = StandardScaler()

for df in filtered_dataframes:

    df['uS_cleaned'] = nk.eda_clean(df['uS'], sampling_rate=50)
    df['uS_standardized'] = scaler.fit_transform(df['uS_cleaned'].values.reshape(-1, 1))
    preprocessed_dataframes.append(df)

# List to store the selected features for each CSV file
features_list = []

for df in preprocessed_dataframes:
    signals, info = nk.eda_process(df['uS_standardized'], sampling_rate=50)
    features = nk.eda_intervalrelated(signals, sampling_rate=50)
        
    # Extract the desired features
    selected_features = {
        'Date & Time': df['date_hour'].iloc[0],
        'Participant ID': df['Participant ID'].iloc[0],
        'Room': df['Room'].iloc[0],
        'mean_scl': signals["EDA_Tonic"].mean(),
        'SCR_Peaks_N': features['SCR_Peaks_N'].values[0],
        'SCR_Peaks_Amplitude_Mean': features['SCR_Peaks_Amplitude_Mean'].values[0],
        'AUC_scr': np.trapezoid(signals["EDA_Phasic"], dx=1/50)
    }

    features_list.append(selected_features)


features_df = pd.DataFrame(features_list)

# Calculate composite EDA engagement score
features_scaled = pd.DataFrame(scaler.fit_transform(features_df.iloc[:, 3:]))

composite_engagement = features_scaled.mean(axis=1)

features_df["Composite_Engagement"] = composite_engagement

min_val = composite_engagement.min()
max_val = composite_engagement.max()

composite_engagement_minmax = (composite_engagement - min_val) / (max_val - min_val)

features_df["Composite_Engagement_MinMax"] = composite_engagement_minmax


# Export features to Excel
with pd.ExcelWriter('data/eda_engagement.xlsx') as writer:
    features_df.to_excel(writer, sheet_name='Features', index=False)

# Extract dataframes based on 'Room' value
features_df_room1 = features_df[features_df['Room'] == 1]
features_df_room2 = features_df[features_df['Room'] == 2]

# Test if the data is normally distributed
stat1, p1 = shapiro(features_df_room1['Composite_Engagement'])
print(f"Room 1 - Shapiro-Wilk Test: statistic={stat1}, p-value={p1}")

stat2, p2 = shapiro(features_df_room2['Composite_Engagement'])
print(f"Room 2 - Shapiro-Wilk Test: statistic={stat2}, p-value={p2}")

# t-test for each feature
ttest_results = {
    'mean_scl': ttest_ind(features_df_room1['mean_scl'], features_df_room2['mean_scl']),
    'SCR_Peaks_N': ttest_ind(features_df_room1['SCR_Peaks_N'], features_df_room2['SCR_Peaks_N']),
    'SCR_Peaks_Amplitude_Mean': ttest_ind(features_df_room1['SCR_Peaks_Amplitude_Mean'], features_df_room2['SCR_Peaks_Amplitude_Mean']),
    'AUC_scr': ttest_ind(features_df_room1['AUC_scr'], features_df_room2['AUC_scr']),
    'Composite_Engagement': ttest_ind(features_df_room1['Composite_Engagement'], features_df_room2['Composite_Engagement']),
}

print("\nT-test Results:")
for key, value in ttest_results.items():
    print(f"{key}: statistic={value.statistic}, p-value={value.pvalue}")



    




    




