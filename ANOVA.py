import os
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load data
surveys = pd.read_csv('data/surveys_engagement.csv')

# Retain relevant columns and remove NaN values
surveys = surveys.dropna(subset=['expertise_level_q', 'engagement_mean', 'engagement_voice', 'engagement_eda', 'engagement_survey', 'gender'])

# H1: Does interaction with digital humans increase user engagement?
left_room = surveys[surveys['room'] == 'LeftRoom']
right_room = surveys[surveys['room'] == 'RightRoom']

def perform_t_test(feature):
    t_stat, p_value = stats.ttest_ind(left_room[feature].values, right_room[feature].values, equal_var=True)
    print(f"\nH1: Digital human vs. static avatar comparison for {feature}:")
    if p_value < 0.05:
        print(f"Rejecting null hypothesis, digital humans significantly influence {feature}.")
    else:
        print(f"Failed to reject null hypothesis, no significant difference in {feature}.")

for feature in ['engagement_mean', 'engagement_voice', 'engagement_eda', 'engagement_survey']:
    perform_t_test(feature)

# H2: Does AI proficiency influence engagement?
def perform_anova(feature):
    print(f"\nH2: AI proficiency and {feature} relationship")
    grouped_data = [surveys[surveys['expertise_level_q'] == level][feature] for level in surveys['expertise_level_q'].unique()]
    stat, p_value = stats.levene(*grouped_data)
    print(f'Levene test for homogeneity of variances: p = {p_value:.4f}')
    if p_value < 0.05:
        print('Variances are not equal, using Welch ANOVA')
    anova_model = ols(f'{feature} ~ C(expertise_level_q)', data=surveys).fit()
    print(sm.stats.anova_lm(anova_model, typ=2))

for feature in ['engagement_mean', 'engagement_voice', 'engagement_eda', 'engagement_survey']:
    perform_anova(feature)

# H3: Does entrepreneurship knowledge influence engagement?
def perform_entrepreneurship_anova(feature):
    print(f"\nH3: Entrepreneurship knowledge and {feature} relationship")
    grouped_data = [surveys[surveys['entrepreneurship_knowledge'] == level][feature] for level in surveys['entrepreneurship_knowledge'].unique()]
    stat, p_value = stats.levene(*grouped_data)
    print(f'Levene test for homogeneity of variances: p = {p_value:.4f}')
    if p_value < 0.05:
        print('Variances are not equal, using Welch ANOVA')
    anova_model = ols(f'{feature} ~ C(entrepreneurship_knowledge)', data=surveys).fit()
    print(sm.stats.anova_lm(anova_model, typ=2))

for feature in ['engagement_mean', 'engagement_voice', 'engagement_eda', 'engagement_survey']:
    perform_entrepreneurship_anova(feature)

# H4: Gender-based T-test for engagement
print("\nH4: Gender-based engagement T-test")
# Gender is coded as 1 (Male) and 2 (Female)
def perform_gender_t_test(feature):
    male_engagement = surveys[surveys['gender'] == 1][feature].dropna()
    female_engagement = surveys[surveys['gender'] == 2][feature].dropna()
    print(f"\nT-test for {feature}:")
    print(f"Male count: {len(male_engagement)}, Female count: {len(female_engagement)}")
    if len(male_engagement) > 1 and len(female_engagement) > 1:
        t_stat, p_value = stats.ttest_ind(male_engagement, female_engagement, equal_var=True)
        print(f'T-test results: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}')
        if p_value < 0.05:
            print(f"Significant difference in {feature} between genders.")
        else:
            print(f"No significant difference in {feature} between genders.")
    else:
        print(f"Not enough data for T-test in {feature}. Check gender data distribution.")

for feature in ['engagement_mean', 'engagement_voice', 'engagement_eda', 'engagement_survey']:
    perform_gender_t_test(feature)
