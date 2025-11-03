import pandas as pd

"""Loads the dataset from a CSV file into a pandas DataFrame."""
def load_dataset(filepath: str) -> pd.DataFrame:
  return pd.read_csv(filepath)

"""Cleans the column names of the DataFrame by stripping whitespace, converting to lowercase, and replacing spaces with underscores."""
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
  df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
  return df

"""Converts drug use categories in specified columns to numerical values."""
def converts_drug_use_categories(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:

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

def converts_to_midpoint(df: pd.DataFrame, drug_cols: list) -> pd.DataFrame:
    """Converts age ranges in Age column to their midpoint numerical values."""
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

