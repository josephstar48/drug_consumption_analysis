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
**Columns/Features:** 32 attributes, including personality traits, demographics, and drug-use frequency across 18 substances.

### Key Attibutes/Columns:
- **Demographics:** Age, Gender, Education, Country, Ethnicity
- **Personality:** Neuroticism (Nscore), Extraversion (Escore), Openness (Oscore), Agreeableness (Ascore), Conscientiousness (Cscore), Impulsivity (Impulsive), Sensation-Seeking (SS)
- **Drug Usage:** 19 different drugs to include: Alcohol, Cannabis, Cocaine, Heroin, LSD, etc.
- **Consumption Levels:** CL0(0) through CL6(6) (from Never Used to Used in Last Day)
- **Control Variable:** Semer column (fictitious drug)

### Data Cleaning and Transformation Steps
1. **Load Data:** Read CSV file and preview structure.
2. **Standardize Columns:** Renamed columns and implemented uniformity with lowe case headers and underscore as needed.
3. **Handle Missing Values:** N/A, all values are present in dataset.
4. **Categorical Drug Levels/Scales:** Converted categorical usage (CL0–CL6) to numeric scores (0–6).
5. **Feature Engineering:** Created a drug_intensity_position column representing total consumption across substances, heavy_user and usage_frequency columns to display/flag frequent daily and weekly drug users "heavy users", and a usage_frequency_label column for better readability of data and graphs.
6. **Data Validation:** Checked for duplicates, outliers, and consistent value ranges.
7. **Normalize Personality Scores:** Used for comparison (using Min-Max scaling or Z-scores).
8. **Verify Data Balance:** Verified for all demographics and personality traits. 

**Code References:** 
- [Data Cleaning Functions](src/data_cleaning.py)
- [Visualization Functions](src/visualization.py)

### Visualization Steps
For this project, I used visualizations to explore patterns between personality traits, demographics, and drug use.

**Here are the main visualization steps I followed:**

1. Demographics:
- Plotted age, gender, and education distributions to understand who was in the dataset.

2. Personality vs. Drug Use:
- Used heatmaps to see how traits like impulsivity and sensation-seeking relate to total drug use.

3. Specific Drug Patterns:
- Created barplots to explore how impulsivity affects use of different types pf drugs to include: cannabis, cocaine, and LSD.

4. Demographic Influence:
- Used boxplots to compare drug use intensity across age, gender, and education levels.

5. Clustering & Relationships:
- Built pairplots to find patterns between different drug types and user groups.

6. Summary:
- Created a bar chart of the top 5 most commonly used substances for quick insight.

These steps helped me visualize key relationships and understand how personality and demographics influence drug use.

### Exploratory Visualizations

| **Type**              | **Visualization**                          | **Purpose**                                      |
|-----------------------|--------------------------------------------|--------------------------------------------------|
| Demographics          | Countplot (Age, Gender, Education)         | See population distribution                      |
| Drug Use Overview     | Bar chart by drug type                     | Identify most/least used substances              |
| Correlation Heatmap   | Heatmap of all features                    | Reveal personality and usage relationships       |
| Boxplot               | Personality scores vs. drug usage          | Compare behavioral patterns                      |
| Pairplot              | Between key personality traits             | Detect natural clustering                        |
| Cluster Map           | KMeans or hierarchical clustering          | Group users by usage patterns                    |
| Word Cloud            | Drug frequency visualization               | Visual storytelling                          |

### Key Analytical Steps
-	Compute correlation matrix to find strongest personality–drug use relationships.
-	Use groupby() to analyze average personality traits by drug type.
-	Perform chi-square or ANOVA tests to check for statistically significant differences.
-	Use Principal Component Analysis (PCA) or KMeans clustering to group similar user profiles.
-	Visualize personality clusters and consumption intensity.

### Visualization/Graphs with Analysis 

- **Counterplot/Bar Graphs:** Demographics
### Gender Distribution
![Gender Graph](img/4_gender_distribution.png)

**Analysis:**
The Gender Distribution graph shows that the number of male and female participants is almost the same, meaning the dataset has a balanced gender distribution.

### Age Distribution
![Age Graph](img/3_age_distribution.png)

**Analysis:**
The Age Distribution graph shows that most participants are young adults between 18 and 30 years old, and the number of participants decreases as age increases.

### Education Distribution
![Education Graph](img/8_education_distribution.png)

**Analysis:**
The Education Distribution graph shows that most participants have a university degree or left school around age 16, showing a mix of higher education and early school leavers in the dataset.

### Country Distribution
![Country Graph](img/11_country_distribution.png)

**Analysis:**
The Country Distribution graph shows that most participants are from the UK, followed by the United States and Canada; which indicates that the dataset mainly represents English-speaking countries.

### Ethnicity Distribution
![Ethnicity Graph](img/12_ethnicity_distribution.png)

**Analysis:**
The Ethnicity Distribution graph shows that most participants identify as White, with smaller representation from other ethnic groups, indicating limited diversity in the dataset.

- **Bar Graph:** Most Frequently Used Substances/Drugs
### Mosty Frequently Used Substances
![Drugs Graph](img/10_top_five_used_drugs.png)

**Analysis:**
TheThe Drug Usage Frequency Distribution Graph shows that Caffeine, chocolate, and alcohol are the most used substances, while nicotine and cannabis are used less frequently. 

- **Heatmap Graphs:** Personality Traits
### Correlation Between Personality Traits
![Personality Traits Graph](img/6_corr_heatmap_personality_traits.png)

**Analysis:**
The Personality Traits graph shows that impulsivity and sensation seeking are strongly related, while neuroticism tends to be opposite of personality traits like extraversion and conscientiousness.

### Correlation Between Personality Traits and Drugs
![Personality Traits and Drugs Graph](img/7_corr_heatmap_drug_personality.png)

**Analysis:**
The Personality Traits and Drugs Correlation graph shows that people with higher sensation-seeking and impulsivity scores are more likely to use al different types of drugs, while conscientious individuals tend to use drugs a lot less.

- **Barplot Graph:** Drug Usage Frequency Distribution
### Drug Usage Frequency Distribution
![Drug Usage Frequency Graph](img/1_drug_usage_freq_dist.png)

**Analysis:**
The Drug Usage Frequency Distribution graph shows that most people in the dataset have never used drugs, while a smaller group reported daily or occasional use, showing that regular drug use is less common among participants.

- **Barplot Graph:** Heavy Users (Daily and Weekly Users)
### Heavy Users
![Heavy Users Frequency Graph](img/2_heavy_drug_usage_freq.png)

**Analysis:**
The Heavy Drug Users graph shows that most people have never used drugs, while a smaller portion are heavy users who use daily or weekly, showing that frequent drug use is relatively uncommon.

### Key Insights 
- Impulsive and sensation-seeking personality traits strongly predict drug use. 
- Neuroticism correlates with depressant and stimulant drug consumption.  
- Higher education and age relate to lower overall drug frequency.
- Higher Impulsivity and Sensation Seeking scores correlate strongly with different types of drugs (stimulants, depressants, and hallucinogens).
- Neuroticism shows higher averages among depressant users (benzodiazepines).
- Older and more educated participants report lower frequency of illicit drug use.
- Openness personality trait also correlates correlate strongly with different types of drugs (stimulants, depressants, and hallucinogens).

### Recommendations
- Public health campaigns can target higher-risk personality groups with customized interventions.
- Behavioral research can incorporate personality analytics into early screening models.
- Future predictive modeling: Build classification models (Logistic Regression, Random Forest) to predict high-risk users.
- Integrate personality insights into early prevention and intervention strategies.

### Future Work/Research
- Extend analysis using predictive modeling and dashboard visualization.
- Include temporal data (usage frequency changes over time).
- Integrate social or economic factors like income and employment.
- Build an interactive dashboard with Plotly or Tableau for real-time analysis.

### Tools & Libraries
- Python, Pandas, Numpy  
- Matplotlib, Seaborn
- Scikit-learn(sklearn)

### Key Steps
1. Data cleaning and quantification of variables  
2. Exploratory Data Analysis (EDA) and correlation analysis  
3. Visual insights into behavior and drug patterns
4. Clustering or statistical modeling  
5. Key findings and recommendations  

### Reference
**Kaggle Dataset:** [Drug Consumption (UCI) — Kaggle](https://www.kaggle.com/datasets/obeykhadija/drug-consumptions-uci)  

### Contributors
**Team:** Jose R. Estrella Sr.  
**Program:** Galvanize Data Science & Analytics Bootcamp

### Contact
- **Author:** Jose R. Estrella Sr.
- **E-mail:** josephstar48@gmail.com
- **GitHub:** https://github.com/josephstar48 
