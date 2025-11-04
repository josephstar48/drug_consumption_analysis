import pandas as pd

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
def convert_to_midpoint(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:
   
    midpoint_dict = {
        '18-24': 21,    
        '25-34': 29.5,  
        '35-44': 39.5,  
        '45-54': 49.5,    
        '55-64': 59.5,  
        '65+': 70,
    }

    df[drug_cols] = df[drug_cols].replace(midpoint_dict)
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
Creates a drug_intensity_position representing total consumption across substances.
"""
def add_drug_intensity_position(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:
    df['drug_intensity_position'] = df[drug_cols].sum(axis=1)
    return df