import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Personality traits (such as Neuroticism, Impulsivity, and Sensation Seeking) and demographic factors (age, gender, education) significantly influence the likelihood and frequency of drug consumption.

Do personality traits and demographics predict the likelihood and frequency of drug consumption?

Are impulsive or sensation-seeking individuals more likely to use psychoactive substances (e.g., cannabis, cocaine, LSD)?

How do demographics such as age, gender, and education level influence drug usage patterns?

Can we identify clusters of users based on drug type (e.g., stimulants, depressants, hallucinogens)?

Is there a relationship between personality factors and the type of substances consumed?
"""

# *****Creates Counterplot graph for demographics of age distribution
def plot_age_distribution(df: pd.DataFrame, age_col: str) -> None:
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x=age_col, order=sorted(df[age_col].unique()))
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show() 

# *****Creates Counteplot Graph for gender distribution
def plot_gender_distribution(df: pd.DataFrame, gender_col: str) -> None:
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x=gender_col)
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count') 
    plt.show()

# *****Creates Stacked Bar Graph for Most Frequently used Drugs
def plot_drug_usage_distribution(df: pd.DataFrame, drug_columns: list) -> None:
    plt.figure(figsize=(12,8))
    df[drug_columns].apply(pd.Series.value_counts).T.plot(kind='bar', stacked=True)
    plt.title('Drug Usage Levels Across Substances')
    plt.xlabel('Substances')
    plt.ylabel('Count')
    plt.legend(title='Usage Level')
    plt.tight_layout()
    plt.show()

# *****Creates correlation heatmap for personality traits
def plot_personality_trait_correlation(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10,8))
    traits = ['nscore', 'escore', 'oscore', 'ascore', 'cscore', 'impulsive', 'ss']
    correlation_matrix = df[traits].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Personality Traits')
    plt.tight_layout()
    plt.show()

# *****Creates barplot to visualize usage frequency distribution 
def plot_drug_usage_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df,
        x='Usage Frequency',
        y='heavy_user',
        hue='Usage Frequency',
        palette='viridis',
        legend=False
    )

    plt.title("Drug Usage Frequency Distribution", fontsize=14)
    plt.xlabel("Usage Frequency", fontsize=12)
    plt.ylabel("Number of Users", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    return None

# ***** Combines daily and weekly into heavy users usage and creates graphs for visualization of heavy users

def combine_and_plot_heavy_users(df: pd.DataFrame) -> pd.DataFrame:

    mask = df['Usage Frequency'].isin(['Daily User', 'Weekly User'])
    heavy_user_total = df.loc[mask, 'heavy_user'].sum()
    df = df[~mask]
    df = pd.concat([
        df,
        pd.DataFrame({'Usage Frequency': ['Heavy User'], 'heavy_user': [heavy_user_total]})
    ], ignore_index=True)

    df = df.sort_values('heavy_user', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df,
        x='Usage Frequency',
        y='heavy_user',
        hue='Usage Frequency',
        palette='viridis',
        legend=False
    )

    plt.title("Heavy Drug Usage Frequency (Daily + Weekly Combined as Heavy Users)", fontsize=14)
    plt.xlabel("Heavy Usage Frequency", fontsize=12)
    plt.ylabel("Number of Heavy Users", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    return df




# Creates Correlation Heatmap for personality traits and drug use
def plot_personality_drug_correlation_heatmap(df: pd.DataFrame, drug_cols: list) -> None:
    plt.figure(figsize=(14,12))
    traits = ['nscore', 'escore', 'oscore', 'ascore', 'cscore', 'impulsive', 'ss']
    combined_cols = traits + drug_cols
    corr = df[combined_cols].corr()
    sns.heatmap(corr.loc[traits, drug_cols], annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap of Personality Traits and Drug Use')
    plt.show()

# Creates Pairplot for personality traits and drug use
def plot_personality_drug_pairplot(df: pd.DataFrame, drug_cols: list) -> None:
    traits = ['nscore', 'escore', 'oscore', 'ascore', 'cscore', 'impulsive', 'ss']
    combined_cols = traits + drug_cols
    sns.pairplot(df[combined_cols])
    plt.suptitle('Pairplot of Personality Traits and Drug Use', y=1.02)
    plt.show()

