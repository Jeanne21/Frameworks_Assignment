# 📊 CORD-19 Data Explorer

This project analyzes a **sample of the CORD-19 metadata dataset** and provides an interactive **Streamlit** web application to explore COVID-19 research trends.

---

## 📁 Project Structure


Frameworks_Assignment/
│
├─ data/
│ ├─ metadata.csv # Original dataset (not committed to GitHub)
│ └─ metadata_clean.csv # Cleaned & sampled dataset (used in analysis)
│
├─ notebooks/
│ └─ cord19_analysis.ipynb # Data cleaning, exploration, and visualization
│
├─ app/
│ └─ streamlit_app.py # Streamlit web application
│
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation


---

## ⚡ Setup Instructions
1. **Download the Dataset**  
   - Get `metadata.csv` from [Kaggle – CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).
   - Place it inside the `data/` folder.

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Data Cleaning & Exploration**
- Open `notebooks/cord19_analysis.ipynb` in Jupyter Notebook or VS Code.
- Execute all cells to clean the data and generate visualizations.
- A cleaned subset (`metadata_cleaned.csv`) will be saved in `data/`.

4. **Launch the Streamlit App**
    ```bash
    cd app
    streamlit run streamlit_app.py
    ```

## 🔍 Data Cleaning Summary

- **Sampling:**
The original metadata.csv (~1.5 GB) is too large to load on typical machines.
A __10,000-row__ sample was created using:

```bash
df = pd.read_csv("metadata.csv", nrows=10000)
```

This preserves key trends while remaining lightweight for GitHub and Streamlit.

- **Handling Missing Values:**
| Action     | Reason       |
|------------|--------------|
|Dropped columns `mag_id`, `who_covidence_id`, `arxiv_id`, `s2_id` | 100% missing |
|Filled `abstract` with "No abstract" | Preserve rows for word cloud |
|Filled `authors` & `journal` with "Unknown" | Retain valuable rows |
|Dropped unused columns `sha`, `pdf_json_files`, `pmc_json_files` | Not needed for analysis |
|Converted `publish_time` to datetime | Enable year-based trends |

## 📊 Key Findings

- __Publication Trend:__ Research output peaked in 2020–2021.
- __Top Journals:__ medRxiv and bioRxiv published the most papers.
- __Title Insights:__ Frequent words include cinfection, patient, and human

## 🌐 Visualizations

The Streamlit app provides:
- Publications by Year
- Top Journals bar chart
- Word Cloud of paper titles
- Distribution of papers by Source

## 💡 Reflection

Handling the large dataset and extensive missing values was the main challenge.
- This project strengthened skills in:
- pandas for data manipulation
- matplotlib / seaborn for visualization
- Streamlit for interactive web apps

## 🛠️ Requirements

Dependencies are listed in requirements.txt (versions not pinned for flexibility).