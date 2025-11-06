import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""
Personality traits (such as Neuroticism, Impulsivity, and Sensation Seeking) and demographic factors (age, gender, education) significantly influence the likelihood and frequency of drug consumption.

Do personality traits and demographics predict the likelihood and frequency of drug consumption?

Are impulsive or sensation-seeking individuals more likely to use psychoactive substances (e.g., cannabis, cocaine, LSD)?

How do demographics such as age, gender, and education level influence drug usage patterns?

Can we identify clusters of users based on drug type (e.g., stimulants, depressants, hallucinogens)?

Is there a relationship between personality factors and the type of substances consumed?
"""

# *Creates Counterplot graph for demographics of age distribution
def plot_age_distribution(df: pd.DataFrame, age_col: str) -> None:
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x=age_col, order=sorted(df[age_col].unique()))
    plt.title('Age Distribution of Participants')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show() 
    
# *Creates Counteplot Graph for gender distribution
def plot_gender_distribution(df: pd.DataFrame, gender_col: str) -> None:
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x=gender_col)
    plt.title('Gender Distribution of Participants')
    plt.xlabel('Gender')
    plt.ylabel('Count') 
    plt.show()

# *Creates Stacked Bar Graph for Most Frequently used Drugs
def plot_drug_usage_frequency(df: pd.DataFrame, drug_columns: list) -> None:
    
    plt.figure(figsize=(16,12))
    df[drug_columns].apply(pd.Series.value_counts).T.plot(kind='bar', stacked=True)
    plt.title('Drug Usage Levels Across Substances')
    plt.xlabel('Substances')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.legend(title='Usage Level')
    plt.show()

# *Creates barplot to visualize usage frequency distribution 
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

# *Combines daily and weekly into heavy users usage and creates graphs for visualization of heavy users

def combine_and_plot_heavy_users(df: pd.DataFrame) -> pd.DataFrame:

    boolean_mask = df['Usage Frequency'].isin(['Daily User', 'Weekly User'])
    heavy_user_total = df.loc[boolean_mask, 'heavy_user'].sum()
    df = df[~boolean_mask]
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

# *Creates Correlation Heatmap for personality traits and drug use
def plot_personality_drug_correlation_heatmap(df: pd.DataFrame, drug_cols: list) -> None:
    traits = ['neuroticism_nscore', 'extraversion_escore', 'openness_oscore', 'agreeableness_ascore', 'conscientiousness_cscore', 'impulsivity_impulsive', 'sensation_seeking_ss']
    
    combined_cols = traits + drug_cols
    corr = df[combined_cols].corr()

    plt.figure(figsize=(len(drug_cols) * 0.7, len(traits) * 0.7))

    ax = sns.heatmap(
        corr.loc[traits, drug_cols],
        annot=True,
        cmap='coolwarm',
        cbar_kws={'shrink': 0.7},  
        linewidths=0.5,             
        fmt=".2f"                   
    )

    ax.set_title('Correlation Heatmap of Personality Traits and Drug Use', fontsize=14, pad=15)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    plt.tight_layout()
    plt.show()

# *Creates correlation heatmap for personality traits
def plot_personality_trait_correlation(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10,8))
    traits = ['neuroticism_nscore', 'extraversion_escore', 'openness_oscore', 'agreeableness_ascore', 'conscientiousness_cscore', 'impulsivity_impulsive', 'sensation_seeking_ss']
    correlation_matrix = df[traits].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Personality Traits')
    plt.tight_layout()
    plt.show()

# Creates a stacked bar chart showing personality traits vs. drug intensity levels. 

def plot_personality_drug_intensity_stacked(df: pd.DataFrame) -> None:

    traits = [
        'neuroticism_nscore', 'extraversion_escore', 'openness_oscore',
        'agreeableness_ascore', 'conscientiousness_cscore',
        'impulsivity_impulsive', 'sensation_seeking_ss'
    ]
    
    mean_intensity = df['drug_intensity_position'].mean()
    below = []
    above = []

    for trait in traits:
        below.append((df.loc[df['drug_intensity_position'] < mean_intensity, trait] > df[trait].mean()).sum())

        above.append((df.loc[df['drug_intensity_position'] >= mean_intensity, trait] > df[trait].mean()).sum())
    
    weight_counts = {
        "Below Avg Drug Use": np.array(below),
        "Above Avg Drug Use": np.array(above),
    }

    width = 0.5
    fig, ax = plt.subplots(figsize=(12, 7))
    bottom = np.zeros(len(traits))

    for label, counts in weight_counts.items():
        ax.bar(traits, counts, width, label=label, bottom=bottom)
        bottom += counts

    ax.set_title("Personality Traits vs. Drug Intensity Levels", fontsize=14, pad=15)
    ax.set_xlabel("Personality Traits", fontsize=12)
    ax.set_ylabel("Count of Individuals", fontsize=12)
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Creates barplots to explore how impulsivity affects use of drugs like cannabis, cocaine, and LSD.

def plot_trait_drug_barplots(df: pd.DataFrame, traits: list, drugs: list) -> None:

    sns.set(style="whitegrid", palette="muted", font_scale=1.1)
    plt.figure(figsize=(16, 12))

    for trait in traits:
        for drug in drugs:
            plt.figure(figsize=(8, 5))
            sns.barplot(
                x=drug,
                y=trait,
                data=df,
                ci=None,
                palette="coolwarm"
            )
            plt.title(f"{trait} vs. {drug} Usage Level", fontsize=14, fontweight='bold')
            plt.xlabel(f"{drug} Use (0–6)", fontsize=12)
            plt.ylabel(f"Average {trait} Score", fontsize=12)
            plt.tight_layout()
            plt.show()

# Creates a boxplot to compare drug use intensity across age, gender, and education levels.

def plot_drug_intensity_by_demographics(df: pd.DataFrame) -> None:

    sns.set(style="whitegrid", palette="muted", font_scale=1.1)
    plt.figure(figsize=(16, 12))

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='age', y='drug_intensity_position', data=df, palette='Blues')
    plt.title("Drug Use Intensity by Age Group", fontsize=14, fontweight='bold')
    plt.xlabel("Age Group")
    plt.ylabel("Drug Intensity Index")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='gender', y='drug_intensity_position', data=df, palette='Set2')
    plt.title("Drug Use Intensity by Gender", fontsize=14, fontweight='bold')
    plt.xlabel("Gender")
    plt.ylabel("Drug Intensity Index")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='education', y='drug_intensity_position', data=df, palette='viridis')
    plt.title("Drug Use Intensity by Education Level", fontsize=14, fontweight='bold')
    plt.xlabel("Education Level")
    plt.ylabel("Drug Intensity Index")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Creates a pairplot to find patterns between different drug types and user groups.

def plot_drug_pairplot(df: pd.DataFrame, drug_columns: list) -> None:

    sns.set(style="whitegrid", font_scale=1.1)

    pairplot = sns.pairplot(
        df[drug_columns],
        corner=True,
        diag_kind="kde",
        plot_kws={"alpha": 0.6, "s": 40, "edgecolor": "k"},
        diag_kws={"shade": True},
        palette="coolwarm"
    )

    pairplot.fig.suptitle(
        "Pairwise Relationships Among Selected Drug Types",
        fontsize=14,
        fontweight="bold",
        y=1.02
    )

    plt.show()


# Creates a bar chart of the top 5 most commonly used substances for quick insight.

def plot_top_five_drugs(df: pd.DataFrame, drug_columns: list) -> None:

    sns.set(style="whitegrid", font_scale=1.1)
    plt.figure(figsize=(8, 5))

    avg_usage = df[drug_columns].mean().sort_values(ascending=False).head(5)

    sns.barplot(x=avg_usage.index, y=avg_usage.values, palette="coolwarm")

    plt.title("Top 5 Most Commonly Used Substances", fontsize=14, fontweight="bold")
    plt.xlabel("Substance")
    plt.ylabel("Average Usage Level (0–6)")
    plt.tight_layout()
    plt.show()