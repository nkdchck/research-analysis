import os
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from src.utils.constants import COLUMNS_DECODER, BINS


def histogram(df: pd.DataFrame, x_column:str, y_column:str, x_title: str, y_title: str, title: str, info_dir: str, file_name: str, name: str='', y_axis_range: list = []) -> None:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=df, dodge=False, label=name) if name != '' else sns.barplot(x=x_column, y=y_column, data=df, dodge=False)

    plt.title(title, fontsize=14)
    plt.xlabel(x_title, fontsize=12)
    plt.ylabel(y_title, fontsize=12)
    plt.xticks(rotation=45, ha='right')
    if y_axis_range:
        plt.ylim(y_axis_range)

    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=10)
    plt.savefig(f'{info_dir}/{file_name}.png', dpi=300, bbox_inches='tight')
    plt.close()


def paired_histogram(df: pd.DataFrame, x_column: str, y_columns: list, x_title: str, y_title: str,
                     title: str, info_dir: str, file_name: str, legend_labels: list, y_axis_range: list = []) -> None:
    """
    Plots two histograms side by side with bars grouped by bin.

    Args:
        df (pd.DataFrame): DataFrame containing binned data.
        x_column (str): Column representing bin ranges (x-axis).
        y_columns (list): List of two column names to plot as paired bars.
        x_title (str): Label for x-axis.
        y_title (str): Label for y-axis.
        title (str): Chart title.
        info_dir (str): Directory to save the plot.
        file_name (str): File name for saving the plot.
        legend_labels (list): Names for the two bars in the legend.
        y_axis_range (list, optional): Custom y-axis range. Defaults to [].
    """
    
    plt.figure(figsize=(12, 6))

    # Compute bar positions
    bar_width = 0.4
    x_positions = np.arange(len(df[x_column]))

    # Plot the bars side by side
    plt.bar(x_positions - bar_width/2, df[y_columns[0]], width=bar_width, label=legend_labels[0], alpha=0.8)
    plt.bar(x_positions + bar_width/2, df[y_columns[1]], width=bar_width, label=legend_labels[1], alpha=0.8)

    # Formatting
    plt.xticks(ticks=x_positions, labels=df[x_column], rotation=45, ha='right')
    plt.xlabel(x_title, fontsize=12)
    plt.ylabel(y_title, fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend(loc='best', fontsize=10)

    if y_axis_range:
        plt.ylim(y_axis_range)

    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(f'{info_dir}/{file_name}.png', dpi=300, bbox_inches='tight')
    plt.close()


def histogram_perc_with_engagement_lines(
    df: pd.DataFrame, x_column: str, y_column: str, engagement_columns: list, 
    x_title: str, y_title: str, title: str, info_dir: str, file_name: str, 
    name: str, y_axis_range: list = []
) -> None:
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Ensure x_column is categorical for proper alignment
    df[x_column] = pd.Categorical(df[x_column], ordered=True)

    # Convert x-axis to positions to avoid shifting issues
    bar_positions = np.arange(len(df[x_column]))
    bar_width = 0.4  # Adjust width for spacing

    # Plot bar chart on the primary axis
    ax1.bar(bar_positions, df[y_column], width=bar_width, label=name, alpha=0.7, color='tab:blue')
    ax1.set_xlabel(x_title, fontsize=12)
    ax1.set_ylabel(y_title, fontsize=12, color='tab:blue')

    if y_axis_range:
        ax1.set_ylim(y_axis_range)

    ax1.grid(visible=True, linestyle='--', alpha=0.7)
    ax1.set_xticks(bar_positions)
    ax1.set_xticklabels(df[x_column])

    # Create a secondary y-axis
    ax2 = ax1.twinx()
    if y_axis_range:
        ax2.set_ylim(y_axis_range)
    ax2.set_ylabel('Engagement Score', fontsize=12, color='tab:red')

    # Plot engagement lines on secondary y-axis
    for engagement_column in engagement_columns:
        ax2.plot(bar_positions, df[engagement_column], marker='o', linestyle='-', label=engagement_column)

    # Combine legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

    plt.title(title, fontsize=14)

    # Save the figure
    plt.savefig(f'{info_dir}/{file_name}.png', dpi=300, bbox_inches='tight')
    plt.close()


def value_counts_perc(df: pd.DataFrame, column: str, engagement_columns:list=[], possible_values:list=[1, 2, 3, 4, 5], x_str:bool=False, surveys:pd.DataFrame=pd.DataFrame()) -> pd.DataFrame:
    df = df.dropna(subset=[column])
    df = df[column].value_counts().reset_index().sort_values(column, ascending=True)
    df['perc'] = df['count'] / df['count'].sum()
    # if some possible values are missing, add them to the dataframe with all 0s
    missing_values = [value for value in possible_values if value not in df[column].tolist()]
    for eng_col in engagement_columns:
        df[eng_col] = surveys.groupby(column)[eng_col].mean().reset_index()[eng_col]
    if missing_values:
        engagement_cols_d = {eng_col: 0 for eng_col in engagement_columns}
        missing_values_data = {column: missing_values, 'count': 0, 'perc': 0, **engagement_cols_d}
        missing_values_df = pd.DataFrame(missing_values_data)
        df = pd.concat([df, missing_values_df]).sort_values(column, ascending=True)
    if not x_str:
        df[column] = df[column].map(COLUMNS_DECODER[column]['answers'])

    return df



def value_counts_bins(df: pd.DataFrame, n_bins: int, columns: list, perc_mode:bool=False, predefined_bins=[]) -> pd.DataFrame:
    """
    Computes value counts for multiple columns using common binning.

    Args:
        df (pd.DataFrame): DataFrame containing numerical columns.
        n_bins (int): Number of bins.
        columns (list): List of column names to bin.

    Returns:
        pd.DataFrame: Aggregated value counts for each bin across multiple columns.
    """

    # Determine common bin range across all specified columns
    col_min = df[columns].min().min()
    col_max = df[columns].max().max()
    
    if not predefined_bins:
        # Define bin edges
        bins = np.linspace(col_min, col_max, n_bins + 1)
        # Create bin labels
        labels = [f'{bins[i]:.2f} - {bins[i+1]:.2f}' for i in range(n_bins)]
    else:
        bins = predefined_bins
        labels = [f'{predefined_bins[i]:.2f} - {predefined_bins[i+1]:.2f}' for i in range(len(predefined_bins) - 1)]
    
    # Initialize result DataFrame
    bin_counts = pd.DataFrame({'bin_range': labels})
    
    # Apply binning for each column and count occurrences
    for column in columns:
        df[f'{column}_binned'] = pd.cut(df[column], bins=bins, labels=labels, include_lowest=True)
        counts = df[f'{column}_binned'].value_counts().reindex(labels, fill_value=0).sort_index()
        bin_counts[column] = counts.values  # Add counts for this column
        if perc_mode:
            bin_counts[column] = bin_counts[column] / bin_counts[column].sum()

    return bin_counts


def value_counts_bins_with_engagement(df_value_counts: pd.DataFrame, surveys:pd.DataFrame, value_counts:str, engagement_columns:list) -> pd.DataFrame:
    mean_engagements = {eng_col : [] for eng_col in engagement_columns}
    for idx, row in df_value_counts.iterrows():
        range_ = row['bin_range']
        first, last = range_.split(' - ')
        first = float(first.strip())
        last = float(last.strip())
        for eng_col in engagement_columns:
            eng_mean = surveys[(surveys[value_counts] >= first) & (surveys[value_counts] <= last)][eng_col].mean() 
            if not np.isnan(eng_mean):
                mean_engagements[eng_col].append(eng_mean)
            else:
                mean_engagements[eng_col].append(0)

    for eng_col in engagement_columns:
        df_value_counts[eng_col] = mean_engagements[eng_col]

    df_value_counts = df_value_counts[df_value_counts[value_counts] != 0]

    return df_value_counts

os.makedirs('plots', exist_ok=True)
surveys = pd.read_csv('data/surveys_engagement.csv')
surveys['start date & time'] = pd.to_datetime(surveys['start date & time'], errors='coerce')
left_room = surveys[surveys['room'] == 'LeftRoom']
right_room = surveys[surveys['room'] == 'RightRoom']
engagement_columns = ['engagement_voice', 'engagement_survey', 'engagement_eda', 'engagement_mean']
surveys = surveys.dropna(subset=engagement_columns)

# General plots: general EDA
# What do they study?
curr_h = 'H0'
os.makedirs(f'plots/{curr_h}', exist_ok=True)
study_programme_value_counts = value_counts_perc(surveys, 'study_programme', possible_values=[], x_str=True)
histogram(study_programme_value_counts, 'study_programme', 'perc', 'Distribution of answers', 'Percentage', 'Question: "What do you study?"', f'plots/{curr_h}', 'study_programme_distribution', 'Number of students', [0, 1])
# How many participants per date?
dates_df = surveys['start date & time'].dt.date.value_counts().reset_index().sort_values('start date & time', ascending=True)
histogram(dates_df, 'start date & time', 'count', 'Date', 'Number of participants', 'Distribution of participants by date', f'plots/{curr_h}', 'dates_distribution', 'Number of participants')
# How many participants per gender?
genders_df = surveys.groupby('gender')['participant_id'].count().reset_index()
genders_df['gender'] = genders_df['gender'].map({1:'Men', 2:'Women'})
genders_df = genders_df.rename(columns={'participant_id': 'count'})
histogram(genders_df, 'gender', 'count', 'Gender', 'Number of participants', 'Distribution of participants by gender', f'plots/{curr_h}', 'gender_distribution', 'Number of participants')
# How reliable are the students answers? Plot distribution of attention
attention_value_counts = value_counts_perc(surveys, 'attention_check_q')
histogram(attention_value_counts, 'attention_check_q', 'perc', 'Distribution of answers', 'Percentage', 'Question: "How carefully did you read the questions from 1 to 5?"', f'plots/{curr_h}', 'attention_distribution', 'Attention', [0, 1])
# Text analysis
perc_value_counts = value_counts_bins(surveys.copy(), 10, ['perc_interactions_diff'])
histogram(perc_value_counts, 'bin_range', 'perc_interactions_diff', 'Percentage of interactions length difference between agent and user', 'Percentage', 'Distribution interaction lengths differences (absolute value)', f'plots/{curr_h}', 'perc_interactions_diff_distribution', 'Percentage of interactions difference')
complexity_value_counts = value_counts_bins(surveys.copy(), 10, ['mean_user_complexity', 'mean_agent_complexity'])
paired_histogram(complexity_value_counts, 'bin_range', ['mean_user_complexity', 'mean_agent_complexity'], 'Mean language complexity measured with Wiener Sachtextformel formula, groupped by bins (4 very simple - 15 very difficult)', 'Percentage', 'Distribution of language complexity: User vs Agent', f'plots/{curr_h}', 'complexity_distribution', ['User', 'Agent'])
polarity_value_counts = value_counts_bins(surveys.copy(), 10, ['mean_user_polarity', 'mean_agent_polarity'])
paired_histogram(polarity_value_counts, 'bin_range', ['mean_user_polarity', 'mean_agent_polarity'], 'Mean polarity of the language measured with TextBlob, groupped by bins [-1 very negative, 1 very positive]', 'Percentage', 'Distribution of polarity: User vs Agent', f'plots/{curr_h}', 'polarity_distribution', ['User', 'Agent'])
subjectivity_value_counts = value_counts_bins(surveys.copy(), 10, ['mean_user_subjectivity', 'mean_agent_subjectivity'])
paired_histogram(subjectivity_value_counts, 'bin_range', ['mean_user_subjectivity', 'mean_agent_subjectivity'], 'Mean subjectivity of the language measured with TextBlob, groupped by bins [0 very objective, 1 very subjective]', 'Percentage', 'Distribution of subjectivity: User vs Agent', f'plots/{curr_h}', 'subjectivity_distribution', ['User', 'Agent'])


# Proficiency in AI
#H1: Interaction with digital human -> the use of interactive digital human will increase the level of user engagement during interaction compared to static avatars.
curr_h = 'H1'
os.makedirs(f'plots/{curr_h}', exist_ok=True)
experience_value_counts = value_counts_bins(surveys.copy(), 10, ['usage_experience'], perc_mode=True)
hist_value_counts = value_counts_bins_with_engagement(experience_value_counts, surveys, 'usage_experience', engagement_columns)
histogram_perc_with_engagement_lines(hist_value_counts, 'bin_range', 'usage_experience', engagement_columns, 
                                     'Question: "How would you rate your experience with AI?"', 'Percentage', 'H1: use of interactive digital human will increase the level of user engagement', 
                                     f'plots/{curr_h}', 'experience_engagement', 'Engagement', [0, 1])
for eng_col in engagement_columns:
    left_room_val_counts_perc = value_counts_bins(left_room, 5, [eng_col], perc_mode=True, predefined_bins=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    right_room_val_counts_perc = value_counts_bins(right_room, 5, [eng_col], perc_mode=True, predefined_bins=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    merged_left_right = pd.merge(left_room_val_counts_perc, right_room_val_counts_perc, on='bin_range', suffixes=('_left', '_right'))
    paired_histogram(merged_left_right, 'bin_range', [f'{eng_col}_left', f'{eng_col}_right'], f'{eng_col} left vs right', 'Percentage', f'Percentages of engagement by bins distribution', f'plots/{curr_h}', f'{eng_col}_distribution_left_vs_right_paired_histogram', ['Left Room', 'Right Room'], [0, 1])

t_stat, p_value = stats.ttest_ind(left_room['engagement_mean'].values, right_room['engagement_mean'].values, equal_var=True)
if p_value < 0.05:
    print("Reject the null hypothesis H1: The groups are significantly different. The use of interactive digital human will increase the level of user engagement during interaction compared to static avatars.")
else:
    print("Fail to reject the null hypothesis H1: No significant difference. Both left and right room have similar engagement levels.")

#H2: Higher AI proficiency -> higher engagement during interaction with the conversational agents.
curr_h = 'H2'
os.makedirs(f'plots/{curr_h}', exist_ok=True)
chatbots_value_counts = value_counts_perc(surveys, 'which_suscriptions_q', possible_values=[], x_str=True)
histogram(chatbots_value_counts, 'which_suscriptions_q', 'perc', 'Chatbots/LLMs the participants frequently use', 'Percentage', 'Distribution of answers', f'plots/{curr_h}', 'chatbots_distribution', 'Percentage of participants', [0, 1])

ai_knowledge_value_counts = value_counts_bins(surveys.copy(), 10, ['expertise_level_q'], perc_mode=True, predefined_bins=[1.0, 2.0, 3.0, 4.0, 5.0])
hist_value_counts = value_counts_bins_with_engagement(ai_knowledge_value_counts, surveys, 'expertise_level_q', engagement_columns)
histogram_perc_with_engagement_lines(hist_value_counts, 'bin_range', 'expertise_level_q', engagement_columns,
                                        'Engagement ranges percentage distribution', 'Percentage', 'H2: higher AI proficiency -> higher engagement', 
                                        f'plots/{curr_h}', 'ai_knowledge_engagement', '% of participants for engagement range', [0, 1])

# H3
curr_h = 'H3'
os.makedirs(f'plots/{curr_h}', exist_ok=True)
entrepreneurship_value_counts = value_counts_bins(surveys.copy(), 10, ['entrepreneurship_knowledge'], perc_mode=True, predefined_bins=[1.0, 2.0, 3.0, 4.0, 5.0])
entrepreneurship_value_counts = value_counts_bins_with_engagement(entrepreneurship_value_counts, surveys.copy(), 'entrepreneurship_knowledge', engagement_columns)
histogram_perc_with_engagement_lines(entrepreneurship_value_counts, 'bin_range', 'entrepreneurship_knowledge', engagement_columns,
                                        'Engagement ranges percentage distribution', 'Percentage', 'H3: higher entrepreneurship knowledge -> higher engagement', 
                                        f'plots/{curr_h}', 'entrepreneurship_engagement', '% of participants for engagement range', [0, 1])

# H4
curr_h = 'H4'
os.makedirs(f'plots/{curr_h}', exist_ok=True)

genders_value_counts = value_counts_perc(left_room.copy(), 'gender', possible_values=[], x_str=True)
mean_men_engagements = {eng_col : [left_room[left_room['gender'] == 1][eng_col].mean()] for eng_col in engagement_columns}
mean_men_engagements['gender'] = [1]
mean_men_engagements = pd.DataFrame(mean_men_engagements)
mean_women_engagements = {eng_col : [left_room[left_room['gender'] == 2][eng_col].mean()] for eng_col in engagement_columns}
mean_women_engagements['gender'] = [2]
mean_women_engagements = pd.DataFrame(mean_women_engagements)
mean_engagements = pd.concat([mean_men_engagements, mean_women_engagements], ignore_index=True)
genders_value_counts = pd.merge(mean_engagements, genders_value_counts, on='gender') 
genders_value_counts['gender'] = genders_value_counts['gender'].map({1:'men', 2:'women'})
histogram_perc_with_engagement_lines(genders_value_counts, 'gender', 'perc', engagement_columns, 
                                     'Gender distribution & mean engagement scores on LEFT room', 'Percentage', 
                                     'H4: different genders have different engagement levels depending on type of digital human',
                                     f'plots/{curr_h}', 'gender_engagement_left_room', 'Engagement', [0, 1])

genders_value_counts = value_counts_perc(right_room.copy(), 'gender', possible_values=[], x_str=True)
mean_men_engagements = {eng_col : [right_room[right_room['gender'] == 1][eng_col].mean()] for eng_col in engagement_columns}
mean_men_engagements['gender'] = [1]
mean_men_engagements = pd.DataFrame(mean_men_engagements)
mean_women_engagements = {eng_col : [right_room[right_room['gender'] == 2][eng_col].mean()] for eng_col in engagement_columns}
mean_women_engagements['gender'] = [2]
mean_women_engagements = pd.DataFrame(mean_women_engagements)
mean_engagements = pd.concat([mean_men_engagements, mean_women_engagements], ignore_index=True)
genders_value_counts = pd.merge(mean_engagements, genders_value_counts, on='gender') 
genders_value_counts['gender'] = genders_value_counts['gender'].map({1:'men', 2:'women'})
histogram_perc_with_engagement_lines(genders_value_counts, 'gender', 'perc', engagement_columns, 
                                     'Gender distribution & mean engagement scores on RIGHT room', 'Percentage', 
                                     'H4: different genders have different engagement levels depending on type of digital human',
                                     f'plots/{curr_h}', 'gender_engagement_right_room', 'Engagement', [0, 1])
