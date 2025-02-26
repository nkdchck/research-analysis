import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

# Load data
surveys = pd.read_csv('data/surveys_engagement.csv')

# Select engagement metrics for correlation analysis
engagement_metrics = ['engagement_voice', 'engagement_eda', 'engagement_survey']
surveys = surveys[engagement_metrics].dropna()  # Drop NaN values to ensure valid correlation

# Rename for cleaner visualization
rename_dict = {
    'engagement_voice': 'Voice',
    'engagement_eda': 'EDA',
    'engagement_survey': 'Survey'
}
surveys = surveys.rename(columns=rename_dict)

# Compute Spearman correlation matrix
spearman_corr = surveys.corr(method='spearman')


# Plot heatmap of Spearman correlations with updated labels
plt.figure(figsize=(6, 5))
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', linewidths=0.5, xticklabels=rename_dict.values(), yticklabels=rename_dict.values())
plt.title("Spearman Correlation Heatmap")
plt.show()
