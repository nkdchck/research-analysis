import os
import json
import math

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from src.utils.constants import COLUMNS_DECODER, QUESTIONS_GROUPS, ATTENTION_CHECK_WEIGHTING, ENGAGEMENT_SURVEY_COLUMNS, ENGAGEMENT_SURVEY_COLUMNS_REMAP


def single_line_plot(df: pd.DataFrame, x_column:str, y_column:str, x_title: str, y_title: str, title: str, info_dir: str, file_name: str, name: str, y_axis_range: list = []) -> None:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=df, label=name)

    plt.title(title, fontsize=14)
    plt.xlabel(x_title, fontsize=12)
    plt.ylabel(y_title, fontsize=12)
    if y_axis_range:
        plt.ylim(y_axis_range)

    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.legend(loc='best', fontsize=10)
    plt.savefig(f'{info_dir}/{file_name}.png', dpi=300, bbox_inches='tight')
    plt.close()

clean_surveys_path = 'data/surveys_cleaned.csv'
surveys = pd.read_csv(clean_surveys_path)
voice_engagement_path = 'data/voice_engagement.xlsx'
voice_engagement = pd.read_excel(voice_engagement_path, sheet_name='part1').rename(columns={'Order of participant': 'participant_id', 'Engagement': 'engagement_voice', 'Normalization': 'normalized_voice_engagement'})
voice_engagement.drop(columns=['normalized_voice_engagement'], inplace=True)
voice_engagement['engagement_voice'] = voice_engagement['engagement_voice'] / 100
eda_engagement_path = 'data/eda_engagement.xlsx'
eda_engagement = pd.read_excel(eda_engagement_path, sheet_name='Features').rename(columns={'Composite_Engagement_MinMax': 'engagement_eda', 'Participant ID': 'participant_id'})


# Extract engagement features from text and add them to the surveys dataframe
text_features_path = 'quantitative_features.json'
perc_interactions_diffs = []
mean_user_complexities = []
mean_agent_complexities = []
mean_user_polarities = []
mean_agent_polarities = []
mean_user_subjectivities = []
mean_agent_subjectivities = []
mean_user_sentiments = []
mean_agent_sentiments = []
for data_dir in surveys['data_dir'].tolist():
    file_path = f'{data_dir}/{text_features_path}'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            text_features = json.load(file)
        perc_interactions_diff = abs(text_features['n_user_interactions'] - text_features['n_agent_interactions']) / text_features['n_user_interactions']
        perc_interactions_diffs.append(perc_interactions_diff)

        mean_user_complexity = sum(text_features['user_complexities']) / len(text_features['user_complexities'])
        mean_agent_complexity = sum(text_features['agent_complexities']) / len(text_features['agent_complexities'])
        mean_user_complexities.append(mean_user_complexity)
        mean_agent_complexities.append(mean_agent_complexity)

        mean_user_polarity = sum(text_features['user_polarities']) / len(text_features['user_polarities'])
        mean_agent_polarity = sum(text_features['agent_polarities']) / len(text_features['agent_polarities'])
        mean_user_polarities.append(mean_user_polarity)
        mean_agent_polarities.append(mean_agent_polarity)

        mean_user_subjectivities.append(sum(text_features['user_subjectivities']) / len(text_features['user_subjectivities']))
        mean_agent_subjectivities.append(sum(text_features['agent_subjectivities']) / len(text_features['agent_subjectivities']))

        mean_user_sentiment = sum(text_features['user_sentiments']) / len(text_features['user_sentiments'])
        mean_agent_sentiment = sum(text_features['agent_sentiments']) / len(text_features['agent_sentiments'])
        mean_sentiment_diff = abs(mean_user_sentiment - mean_agent_sentiment)
        mean_user_sentiments.append(mean_user_sentiment)
        mean_agent_sentiments.append(mean_agent_sentiment)

    else:
        perc_interactions_diffs.append(None)
        mean_user_complexities.append(None)
        mean_agent_complexities.append(None)
        mean_user_polarities.append(None)
        mean_agent_polarities.append(None)
        mean_user_subjectivities.append(None)
        mean_agent_subjectivities.append(None)
        mean_user_sentiments.append(None)
        mean_agent_sentiments.append(None)
surveys['perc_interactions_diff'] = perc_interactions_diffs
surveys['mean_user_complexity'] = mean_user_complexities
surveys['mean_agent_complexity'] = mean_agent_complexities
surveys['mean_user_polarity'] = mean_user_polarities
surveys['mean_agent_polarity'] = mean_agent_polarities
surveys['mean_user_subjectivity'] = mean_user_subjectivities
surveys['mean_agent_subjectivity'] = mean_agent_subjectivities
surveys['mean_user_sentiment'] = mean_user_sentiments
surveys['mean_agent_sentiment'] = mean_agent_sentiments

# Group questions and calculate mean for each group, then bin the results by 0.25 intervals
bins = list(np.arange(0, 5.25, 0.25))
labels = list(np.arange(0.25, 5.25, 0.25))
for k, features in QUESTIONS_GROUPS.items():
    surveys[k] = surveys[features].mean(axis=1) * surveys['attention_check_q'].map(ATTENTION_CHECK_WEIGHTING)
    surveys[k] = pd.cut(surveys[k], bins=bins, labels=labels)

# Compute the engagement metric based on the survey
for k, v in ENGAGEMENT_SURVEY_COLUMNS_REMAP.items():
    surveys[k] = surveys[k].map(v)
surveys['engagement_survey'] = (surveys[ENGAGEMENT_SURVEY_COLUMNS].mean(axis=1) / 5) * surveys['attention_check_q'].map(ATTENTION_CHECK_WEIGHTING)

# Add the engagement measured through electrodermal activity device
eda_engagement = eda_engagement[['participant_id', 'engagement_eda']]
surveys = pd.merge(surveys, eda_engagement, on='participant_id', how='left')
# Add the engagement measured through voice analysis with hume ai
surveys = pd.merge(surveys, voice_engagement, on='participant_id', how='left')
# Add the mean engagement between the three sources
surveys['engagement_mean'] = surveys[['engagement_survey', 'engagement_eda', 'engagement_voice']].mean(axis=1)

surveys.to_csv('data/surveys_engagement.csv', index=False)
