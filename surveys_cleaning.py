import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import editdistance

from src.utils.constants import COLUMNS_RENAME

# Surveys data
survey_path = 'data/PsyToolkitData_Digital_Human_2025_01_28_14_48/data without discarded.xlsx'
df = pd.read_excel(survey_path)
df = df.rename(columns=COLUMNS_RENAME)
df.columns = df.columns.str.lower()
df = df[df['attention_check_q'] == 5]
df['study_programme'] = df['study_programme'].str.replace('.', '').str.lower().str.strip().str.replace('bsc', '').str.strip().str.replace('b sc', '').str.strip().str.replace('-', '')
df.loc[df['study_programme'].str.contains('wirtschaftsingenieur', case=False, na=False), 'study_programme'] = 'Industrial Engineering'
df.loc[df['study_programme'].str.contains('vwl', case=False, na=False), 'study_programme'] = 'Economics & Sustainability'
df.loc[df['study_programme'].str.contains('Fahrzeugtechnik', case=False, na=False), 'study_programme'] = 'Vehicle Engineering'
df.loc[df['study_programme'].str.contains('Imes', case=False, na=False), 'study_programme'] = 'Innovation Management, Entrepreneurship & Sustainability'
df.loc[df['study_programme'].str.contains('Innovation', case=False, na=False), 'study_programme'] = 'Innovation Management, Entrepreneurship & Sustainability'
df.loc[df['study_programme'].str.contains('Machinenbau', case=False, na=False), 'study_programme'] = 'Mechanical Engineering'
df.loc[df['study_programme'].str.contains('Mathematik', case=False, na=False), 'study_programme'] = 'Mathematics'
df.loc[df['study_programme'].str.contains('Informationsgesellschaft', case=False, na=False), 'study_programme'] = 'Natural Sciences in the Information Society'
df.loc[df['study_programme'].str.contains('Technischer Umweltschutz', case=False, na=False), 'study_programme'] = 'Environmental Science and Technology'
df.loc[df['study_programme'].str.contains('Wima', case=False, na=False), 'study_programme'] = 'Business Mathematics'
df.loc[df['study_programme'].str.contains('Wirtschaftsmathematik', case=False, na=False), 'study_programme'] = 'Business Mathematics'
df.loc[
        df['study_programme'].str.contains('nachhaltig', case=False, na=False) &
        df['study_programme'].str.contains('manag', case=False, na=False)
        , 'study_programme'
    ] = 'Sustainability Management'
df.loc[
        df['study_programme'].str.contains('wirtschafts', case=False, na=False) &
        df['study_programme'].str.contains('informat', case=False, na=False)
        , 'study_programme'
    ] = 'Business & Informatics'
df.loc[
        df['study_programme'].str.contains('wirtschafts', case=False, na=False) &
        df['study_programme'].str.contains('ingen', case=False, na=False)
        , 'study_programme'
    ] = 'Industrial Engineering'
df.loc[
        df['study_programme'].str.contains('volkswirtsch', case=False, na=False) &
        df['study_programme'].str.contains('nachhalt', case=False, na=False)
        , 'study_programme'
    ] = 'Economics & Sustainability'

def map_study_programme(value):
    if pd.isna(value):  # Ensure NaN values remain unchanged
        return value
    value = value.lower().strip()  # Normalize case & whitespace for matching
    d = {
    'informatik':'computer science', 
    'computational engineering science': 'computational engineering science',
    'innovation management, entrepreneurship & sustainability': 'innovation management, entrepreneurship & sustainability',
    'intenational business': 'international business',
    'nama': 'sustainability management',
    'wiing': 'industrial engineering',
    'wi ing': 'industrial engineering',
    'imes': 'innovation management',
    'ces': 'computational engineering science',
    }
    return d.get(value, value)  # Keep original if no match

df['study_programme'] = df['study_programme'].apply(map_study_programme).str.title()

ref_subscriptions = ['chatgpt', 'claude', 'deepseek', 'copilot', 'jetbrains ai']

def clean_subscription(value):
    value = value.replace(' ', '')
    subscriptions = [s.strip() for s in value.split(',')]
    clean_subscriptions = []
    for s in subscriptions:
        if s in ref_subscriptions:
            clean_subscriptions.append(s)
        else:
            for ref_subscription in ref_subscriptions:
                if editdistance.eval(s, ref_subscription) <= 2:
                    clean_subscriptions.append(ref_subscription)
                    break
                else:
                    if 'gbt' in s:
                        print(f'Found gbt in {s}')
    clean_subscriptions = ', '.join(clean_subscriptions)
    return clean_subscriptions

df['which_suscriptions_q'] = df['which_suscriptions_q'].str.lower().str.replace('-', '').fillna('').str.strip()
df['which_suscriptions_q'] = df['which_suscriptions_q'].apply(lambda x: clean_subscription(x))

# Participant registry
participant_registry_path = 'data/participant_registry.xlsx'
participant_registry_excel = pd.ExcelFile(participant_registry_path)
sheet_names = participant_registry_excel.sheet_names
all_participants = []
for sheet_name in sheet_names:
    curr_registry = participant_registry_excel.parse(sheet_name)
    curr_registry.columns = curr_registry.iloc[0]
    curr_registry['Attendance (yes/no)'] = curr_registry['Attendance (yes/no)'].str.lower().str.strip()
    curr_registry = curr_registry[curr_registry['Attendance (yes/no)'] == 'yes']
    curr_registry['Start Date & Time'] = pd.to_datetime(curr_registry['Start Date & Time'])
    all_participants.append(curr_registry)

all_participants = pd.concat(all_participants)
all_participants['Room'] = all_participants['Room'].map({1.0:'LeftRoom', 2.0:'RightRoom'})
all_participants['data_dir'] = all_participants.apply(
    lambda x: f'data/{x["Start Date & Time"].day}.{x["Start Date & Time"].strftime("%m")}/{x["Start Date & Time"].strftime("%H")}/{x["Room"]}',
    axis=1
)
all_participants = all_participants.rename(columns={'Participant ID': 'participant_id'})

df = pd.merge(df, all_participants, on='participant_id', how='inner')
df = df.dropna(subset=['data_dir'])
df.columns = df.columns.str.lower()

df.to_csv('data/surveys_cleaned.csv', index=False)
