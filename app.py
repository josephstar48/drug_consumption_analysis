import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans



# --- PAGE SETUP ---
st.set_page_config(
    page_title="Drug Consumption Analysis Dashboard", 
    layout="wide",
     page_icon="💊"
     )

st.title("💊 Drug Consumption Analysis Dashboard")
st.markdown("""
Explore how **personality traits** and **demographics** influence **drug use patterns** using the University of California Drug Consumption dataset.
---
""")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_drug_consumption.csv') 
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🎚️ Filter Options")

# Dropdown filters

selected_trait = st.sidebar.selectbox(
    "Select Personality Trait:",  [
        'neuroticism_nscore', 'extraversion_escore', 'openness_oscore',
        'agreeableness_ascore', 'conscientiousness_cscore',
        'impulsivity_impulsive', 'sensation_seeking_ss'
    ])

selected_gender = st.sidebar.multiselect(
    "Select Gender:", df["gender"].unique(), default=df["gender"].unique()
    )

selected_age = st.sidebar.multiselect(
    "Select Age Group:", df["age"].unique(), default=df["age"].unique())

selected_education = st.sidebar.multiselect(
    "Select Education Level:", df["education"].unique(), default=df["education"].unique()
    )

# Apply filters

filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["age"].isin(selected_age)) &
    (df["education"].isin(selected_education))
]

st.markdown("### 📊 Data Overview")
st.write(f"Showing **{filtered_df.shape[0]}** participants after filters applied.")
st.dataframe(filtered_df.head())

selected_drug = st.sidebar.selectbox("Select Drug:", ['alcohol', 'amphetamine', 'amyl_nitrate', 'benzodiazepines', 'caffeine', 'cannabis', 'chocolate', 'cocaine', 'crack_cocaine', 'ecstasy', 'heroin', 'ketamine', 'legal_highs', 'lsd', 'methamphetamine', 'magic_mushrooms', 'nicotine', 'semer', 'volatile_solvent_abuse'])

# --- MAIN DASHBOARD ---
st.subheader(f"{selected_trait} vs {selected_drug} Usage")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=selected_drug, y=selected_trait, data=df, errorbar=None, palette="coolwarm")
plt.title(f"{selected_trait} vs {selected_drug} Usage", fontsize=14, fontweight="bold")
st.pyplot(fig)

# --- ADD SUMMARY STATS ---
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# --- ADD INSIGHT ---
st.markdown("""
**Insight:**  
Higher impulsivity and sensation seeking scores are often linked to higher usage levels of substances like cannabis, cocaine, and LSD.
""")

# ---------------- CORRELATION HEATMAPS ----------------
st.markdown("## 📈 Correlation Heatmaps: Personality Traits vs Drug Use")

trait_cols = [
        'neuroticism_nscore', 'extraversion_escore', 'openness_oscore',
        'agreeableness_ascore', 'conscientiousness_cscore',
        'impulsivity_impulsive', 'sensation_seeking_ss'
    ]

drug_cols = [
    'alcohol', 'amphetamine', 'amyl_nitrate', 'benzodiazepines', 'caffeine', 'cannabis', 'chocolate', 'cocaine', 'crack_cocaine', 'ecstasy', 'heroin', 'ketamine', 'legal_highs', 'lsd', 'methamphetamine', 'magic_mushrooms', 'nicotine', 'semer', 'volatile_solvent_abuse'
    ]

corr = filtered_df[trait_cols + drug_cols].corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Correlation Between Personality Traits and Drug Use", fontsize=14, fontweight="bold")
st.pyplot(fig)

st.markdown("""
**Interpretation:**  
- Impulsivity and sensation seeking show the strongest positive correlations with stimulant and hallucinogen use.  
- Conscientiousness tends to be negatively correlated with overall drug use frequency.
""")

# ---------------- CLUSTER VISUALIZATION ----------------
st.markdown("## 🧠 Cluster Visualization: Grouping Users by Drug Use Intensity")

# Select columns for clustering
cluster_features = filtered_df[trait_cols + drug_cols].dropna()

# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(cluster_features)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
filtered_df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize clusters (using impulsivity and sensation seeking)
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    data=filtered_df,
    x='impulsivity_impulsive',
    y='sensation_seeking_ss',
    hue='Cluster',
    palette='Set2'
)
plt.title("Clusters Based on Personality and Drug Use", fontsize=14, fontweight='bold')
st.pyplot(fig)

st.markdown("""
**Interpretation:**  
- Cluster 0: Higher impulsivity and sensation-seeking individuals — heavy drug users.  
- Cluster 1: Moderate trait levels — occasional users.  
- Cluster 2: Low impulsivity and sensation seeking — minimal or non-users.
""")

# ---------------- DEMOGRAPHIC INSIGHTS ----------------
st.markdown("## 🎚️ Demographic Influence on Drug Use Intensity")

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

sns.boxplot(x="age", y="drug_intensity_position", data=filtered_df, ax=ax[0], hue="age", legend=False, palette="Blues")
ax[0].set_title("Drug Use Intensity by Age Group")

sns.boxplot(x="gender", y="drug_intensity_position", data=filtered_df, ax=ax[1], hue="gender", legend=False, palette="Set2")
ax[1].set_title("Drug Use Intensity by Gender")

sns.boxplot(x="education", y="drug_intensity_position", data=filtered_df, ax=ax[2], hue="education", legend=False, palette="viridis")
ax[2].set_title("Drug Use Intensity by Education")

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
**Key Takeaways:**  
- Older participants report lower drug use intensity.  
- Males tend to have slightly higher drug use intensity than females.  
- Higher education levels are linked with lower overall drug consumption.
""")

# ---------------- PROJECT INSIGHTS ----------------
st.markdown("## 🧩 Key Findings & Insights")

st.markdown("""
- **Impulsivity** and **Sensation Seeking** strongly predict stimulant and hallucinogen use.  
- **Neuroticism** correlates with depressant and stimulant use (e.g., benzodiazepines).  
- **Education** and **Age** inversely correlate with drug frequency — higher values lead to lower usage.  
- **Clusters** reveal three main user profiles: non-users, moderate users, and heavy users.

**Public Health Impact:**  
- Personality analytics could help target prevention programs for high-risk groups.  
- Behavioral insights can guide smarter intervention strategies and early screening.

**Future Work:**  
- Develop predictive models (Logistic Regression, Random Forest) to estimate high-risk users.  
- Integrate socioeconomic and behavioral data for improved prediction accuracy.
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Developed by Jose R. Estrella (DDI Bootcamp | Galvanize)  |  GitHub: [drug_consumption_analysis](https://github.com/josephstar48/drug_consumption_analysis)")