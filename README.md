# Amazon-Sales-Analytics
Developed an interactive Power BI dashboard to analyze and visualize Amazon product sales performance. The project focused on creating dynamic measures and slicers (including Top N analysis, ranking, and dynamic titles) to allow users to explore sales trends across categories, products, and time periods.
# Amazon Sales Analytics — Python, Julius AI & Power BI

**Short:** End-to-end e-commerce analytics pipeline: fetch raw Amazon sales data from Kaggle, clean & preprocess using Julius AI, analyze with Python, and visualize with an interactive Power BI dashboard.

---

## 🔎 Project Overview
This repo contains code, notebooks and artifacts for an end-to-end data analyst workflow:
- **Data fetch:** scripts to download the dataset from Kaggle via the Kaggle API.
- **Data cleaning:** cleaned with Julius AI (exported CSV used here).
- **Exploration & analysis:** Python notebooks / scripts with EDA and sample charts.
- **Dashboard:** Power BI `.pbix` file and exported visuals.
- **Report:** A PDF summary of key insights (in `/docs`).

**Note:** raw data files are *not* stored in the repo. Use the `fetch_data.py` script (below) to download the dataset locally.

---

## ⚙️ Tech stack
- Python (pandas, numpy, matplotlib, jupyter)
- Julius AI (data cleaning & rapid EDA / charts). :contentReference[oaicite:0]{index=0}
- Power BI Desktop (`.pbix`) for the interactive dashboard.
- Kaggle (dataset source) — downloaded via Kaggle API. :contentReference[oaicite:1]{index=1}

---

## 📂 Recommended repo structure
