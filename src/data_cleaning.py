import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt



# Creates global constants for filepaths
FILEPATH_RAW = '../data/raw/Drug_Consumption.csv'
FILEPATH_CLEANED = '../data/cleaned/cleaned_drug_consumption.csv'

"""Loads the dataset from a CSV file into a pandas DataFrame."""
def load_dataset(filepath: str) -> pd.DataFrame:
  return pd.read_csv(filepath)

"""Saves the cleaned DataFrame to a CSV file."""
def save_cleaned_dataset(df: pd.DataFrame, filepath: str) -> None:
  df.to_csv(filepath, index=False)

"""Cleans the column names of the DataFrame by stripping whitespace, converting to lowercase, and replacing spaces with underscores."""
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
  df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
  return df

"""Converts drug use ratings in specified columns to numerical values."""
def convert_drug_use_ratings(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:

  category_dict = {
      'CL0': 0,  
      'CL1': 1,  
      'CL2': 2, 
      'CL3': 3,  
      'CL4': 4, 
      'CL5': 5,  
      'CL6': 6   
  }

  df[drug_cols] = df[drug_cols].replace(category_dict)
  return df

"""Converts age ranges in Age column to their midpoint numerical values."""
def convert_to_midpoint(df: pd.DataFrame, age_col: list) -> pd.DataFrame:
   
    midpoint_dict = {
        '18-24': 21,    
        '25-34': 29.5,  
        '35-44': 39.5,  
        '45-54': 49.5,    
        '55-64': 59.5,  
        '65+': 70,
    }

    df[age_col] = df[age_col].replace(midpoint_dict)
    return df

"""Changes column headers for personality traits to more descriptive names."""
def rename_personality_traits(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        'Nscore': 'neuroticism_nscore',
        'Escore': 'extraversion_escore',
        'Oscore': 'openness_oscore',
        'AScore': 'agreeableness_ascore',
        'Cscore': 'conscientiousness_cscore',
        'Impulsive': 'impulsivity_impulsive',
        'SS': 'sensation_seeking_ss'
    })
    return df

"""
Creates a drug_intensity_position column representing total consumption across substances.
"""
def add_drug_intensity_position(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:
    df['drug_intensity_position'] = df[drug_cols].sum(axis=1)
    return df

""" Changes column names for some of the drug column names to be more descriptive. """

def rename_drug_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        'Amphet': 'amphetamine',
        'Amyl': 'amyl_nitrate',
        'Benzos': 'benzodiazepines',
        'Caff': 'caffeine', 
        'Choc': 'chocolate',
        'Coke': 'cocaine',
        'Crack': 'crack_cocaine',
        'Legalh': 'legal_highs',
        'Meth': 'methamphetamine',
        'Mushrooms': 'magic_mushrooms',
        'VSA': 'volatile_solvent_abuse'
    })
    return df


"""
Transforms personality traits scores to numeric values between 0 and 1. This makes comparisons cleaner and more intuitive when plotting graphs
"""
def apply_min_max_scaling(df: pd.DataFrame, min_max_personality_traits: list) -> pd.DataFrame:
    min_max_scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[min_max_personality_traits] = min_max_scaler.fit_transform(df_scaled[min_max_personality_traits])
    return df_scaled


""" Creates function to visualize and verify data balance across demographics and personality traits. """

def visualize_data_balance(df: pd.DataFrame, demographic_cols: list, personality_traits: list) -> None:
    sns.set_style("whitegrid")

    for col in demographic_cols:
        plt.figure(figsize=(12, 8))
        sns.countplot(data=df, x=col)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()    
        plt.show()

    for trait in personality_traits:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=trait, kde=True, bins=20, color='teal')
        plt.title(f'Distribution of {trait}')
        plt.ylabel("Frequency")
        plt.xlabel(trait)
        plt.xticks(rotation=30, ha='left', fontsize=10, wrap=True)
        plt.tight_layout()

        plt.show()

    return None


"""Creates usage_frequency and heavy_user columns to flag frequent daily and weekly drug users."""

def flag_heavy_users(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:

    df['usage_frequency'] = df[drug_cols].apply(lambda row: sum(1 for val in row if val >= 5), axis=1)
    
    df['heavy_user'] = df['usage_frequency'] >= 5

    summary = pd.DataFrame({
        'Usage Frequency': ['Never Used', 'Used Over a Decade Ago', 'Used in Last Decade', 'Used in Last Year', 'Monthly User', 'Weekly User', 'Daily User'],
        'heavy_user': [
            (df[drug_cols] == 0).sum().sum(),          
            (df[drug_cols] == 1).sum().sum(),          
            (df[drug_cols] == 2).sum().sum(),         
            (df[drug_cols] == 3).sum().sum(), 
            (df[drug_cols] == 4).sum().sum(),          
            (df[drug_cols] == 5).sum().sum(),       
            (df[drug_cols] == 6).sum().sum(),         
        ]
    })

    print(summary.to_string(index=False))
    return df, summary

""" Replaces outlier values that are higher than 6 with the average  value of that column"""

def replace_outliers_with_mean(df: pd.DataFrame, col: str) -> pd.DataFrame:

    mean_value = df[col].mean()  
    df[col] = df[col].apply(lambda x: mean_value if x > 6 else x)
    return df

""" Converts float values in user_frequency column to String labels for better readability in visualizations."""

def convert_usage_frequency_to_labels(df: pd.DataFrame) -> pd.DataFrame:

    frequency_labels_dict = {
        0: 'Never Used',
        1: 'Used Over a Decade Ago',
        2: 'Used in Last Decade',
        3: 'Used in Last Year',
        3.6: 'Used in Last Year',
        4: 'Monthly User',
        5: 'Weekly User',
        6: 'Daily User'
    }
    df['usage_frequency_label'] = df['usage_frequency'].replace(frequency_labels_dict)

    return df



