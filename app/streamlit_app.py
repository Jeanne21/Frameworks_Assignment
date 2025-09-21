import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("📊 CORD-19 Data Explorer")
st.write("Explore trends in COVID-19 research papers (metadata.csv sample).")

@st.cache_data
def load_data():
    return pd.read_csv("../data/metadata_cleaned.csv")

df = load_data()

# --- Filters ---
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"### Data Sample ({len(filtered)} papers)")
st.dataframe(filtered.head(10))

# --- Publications Over Time ---
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color='skyblue')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# --- Top Journals ---
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, color='lightgreen')
ax.set_xlabel("Paper Count")
ax.set_ylabel("Journal")
st.pyplot(fig)

# Word Cloud in Streamlit
st.subheader("Word Cloud of Paper Titles")
titles_text = " ".join(filtered['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Source Distribution in Streamlit
st.subheader("Paper Counts by Source")
source_counts = filtered['source_x'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=source_counts.index, y=source_counts.values, ax=ax, color='cornflowerblue')
ax.set_ylabel("Number of Papers")
ax.set_xlabel("Source")
st.pyplot(fig)


