# Drug Consumption Analysis

## Personality Traits and Drug Consumption Patterns: An Exploratory Data Analysis 

### Drug Consumption and Personality Traits
#### Exploratory Data Analysis using the UCI Drug  Consumption Dataset
**Author:** Jose Estrella
**Program:** Galvanize Data Science & Analytics Bootcamp (DDI)
**Project Type:** Exploratory Data Analysis (EDA)

### Overview
This project explores how psychological and demographic factors influence drug consumption patterns using the UCI Drug Consumption Dataset (Kaggle). The analysis investigates relationships between personality traits, impulsivity, sensation-seeking, and the likelihood of using specific substances.

I performed data cleaning, exploratory analysis, and visualization to identify behavioral patterns that may predict substance use frequency. The analysis combines psychological measures (such as impulsivity and sensation-seeking) with demographic data to understand the link between personality and substance use.

### Research Questions
1. Do personality traits and demographics predict the likelihood and frequency of drug consumption?
2. Are impulsive or sensation-seeking individuals more likely to use psychoactive substances (e.g., cannabis, cocaine, LSD)?
3. How do demographics such as age, gender, and education level influence drug usage patterns?
4. Can we identify clusters of users based on drug type (e.g., stimulants, depressants, hallucinogens)?
5. Is there a relationship between personality factors and the type of substances consumed?

### Hypothesis
Personality traits (such as Neuroticism, Impulsivity, and Sensation Seeking) and demographic factors (age, gender, education) significantly influence the likelihood and frequency of drug consumption.

### Why Analysis Of This Topic Matters?
#### Understanding the behavioral and psychological factors behind substance use can:
- Help inform public health and education strategies.
- Identify risk profiles for early intervention.
- Demonstrate how data analytics can uncover behavioral insights from psychological and demographic variables.


### Data Source
**Dataset:** [Drug Consumption (UCI) — Kaggle](https://www.kaggle.com/datasets/obeykhadija/drug-consumptions-uci)  
**Records/Rows:** 1,885 participants
**Columns/Features:** 32 attributes, including personality traits, demographics ,and drug-use frequency acroff 18 substances.

### Key Attibutes/Columns:
- Demographics: Age, Gender, Education, Country, Ethnicity
- Personality: Neuroticism (Nscore), Extraversion (Escore), Openness (Oscore), Agreeableness (Ascore), Conscientiousness (Cscore), Impulsivity Sensation-Seeking (SS)
- Substances: Alcohol, Cannabis, Cocaine, Heroin, LSD, etc.
- Consumption Levels: CL0–CL6 (Never Used → Used in Last Day)

### Data Cleaning and Transformation Steps
1. Load Data: Read CSV file and preview structure.
2. Standardize Columns: Renamed columns and implemented uniformity with lowe case headers and underscore as needed.
3. Handle Missing Values: N/A, all values were contained in dataset.
4. Encode Drug Levels: Converted categorical usage (CL0–CL6) into numeric scores (0–6).
5. Feature Engineering: Created a drug_intensity_index representing total consumption across substances.
6. Data Validation: Checked for duplicates, outliers, and consistent value ranges.

**Code Reference:** src/data_cleaning.py 

### Exploratory Visualizations

| **Type**              | **Visualization**                          | **Purpose**                                      |
|-----------------------|--------------------------------------------|--------------------------------------------------|
| Demographics          | Countplot (Age, Gender, Education)         | See population distribution                      |
| Drug Use Overview     | Bar chart by drug type                     | Identify most/least used substances              |
| Correlation Heatmap   | Heatmap of all features                    | Reveal personality and usage relationships       |
| Boxplot               | Personality scores vs. drug usage          | Compare behavioral patterns                      |
| Pairplot              | Between key personality traits             | Detect natural clustering                        |
| Cluster Map           | KMeans or hierarchical clustering          | Group users by usage patterns                    |
| Word Cloud            | Drug frequency visualization               | Visual storytelling                              |

### Key Analytical Steps
-	Compute correlation matrix to find strongest personality–drug use relationships.
-	Use groupby() to analyze average personality traits by drug type.
-	Perform chi-square or ANOVA tests to check for statistically significant differences.
-	Use Principal Component Analysis (PCA) or KMeans clustering to group similar user profiles.
-	Visualize personality clusters and consumption intensity.

### Key Insights 



### Tools & Libraries
- Python, Pandas  
- Matplotlib, Seaborn  


### Key Steps
1. Data cleaning and quantification of variables  
2. Exploratory Data Analysis (EDA) and correlation analysis  
3. Visual insights into behavior and drug patterns  
5. Key findings and recommendations  

### Reference
**Kaggle Dataset:** [Drug Consumption (UCI) — Kaggle](https://www.kaggle.com/datasets/obeykhadija/drug-consumptions-uci)  

### Contributors
**Team:** Jose R. Estrella Sr.  
**Program:** Galvanize Data Science & Analytics Bootcamp

### Contact
**Author:** Jose R. Estrella Sr.
**E-mail:** josephstar48@gmail.com
**GitHub:** https://github.com/josephstar48 
