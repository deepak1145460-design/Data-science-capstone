# Data Science Capstone Project – SpaceX Falcon 9 (Notebook Set)

Yeh sab notebooks aapke screenshot ke grading criteria (1.5 – 1.15) ko cover karte hain.
Har notebook ke top pe **"GitHub URL"** ka placeholder hai — apna repo link daalna na bhoolein
(grading criteria mein har slide/notebook ke saath GitHub URL maanga gaya hai).

## Files
| File | Grading item covered |
|---|---|
| `01_data_collection_api.ipynb` | 1.5 – Data Collection (SpaceX API) |
| `02_data_collection_webscraping.ipynb` | 1.6 – Data Collection (Web Scraping) |
| `03_data_wrangling.ipynb` | 1.7 – Data Wrangling Methodology |
| `04_eda_visualization.ipynb` | 1.8, 1.11 – EDA with Data Visualization |
| `05_eda_sql.ipynb` | 1.9, 1.12 – EDA with SQL |
| `06_folium_launch_site_analysis.ipynb` | 1.10, 1.13 – Interactive Visual Analytics (Folium) |
| `07_spacex_dash_app.py` | 1.10, 1.14 – Interactive Visual Analytics (Plotly Dash) |
| `08_predictive_analysis_classification.ipynb` | 1.15 – Predictive Analysis |

## How to run
1. Install dependencies:
   ```bash
   pip install pandas numpy requests beautifulsoup4 matplotlib seaborn folium plotly dash scikit-learn --break-system-packages
   ```
2. Run notebooks **in order** (01 → 08) — each one saves a `.csv` that the next one reads:
   - `01` → saves `dataset_part_1.csv`
   - `02` → saves `dataset_part_2.csv` (independent scraped record set)
   - `03` → reads `dataset_part_1.csv`, saves `dataset_part_2_clean.csv`
   - `04`–`08` → all read `dataset_part_2_clean.csv`
3. Run the Dash app separately: `python 07_spacex_dash_app.py`, open `http://127.0.0.1:8050`.
4. Har notebook ke end mein "Summary" cell hai — usko apne **Data Science Capstone Project Report** mein copy kar sakte ho.

## Baaki jo manually karna hai (yeh notebooks nahi kar sakte)
- [ ] Apna GitHub repo banao, in sab files ko push karo, aur har notebook/file ke top wale placeholder mein woh URL daalo (1.5–1.10 grading item).
- [ ] In notebooks ke charts/results ko **presentation slides** (PowerPoint/PDF) mein daalo — Executive Summary, Introduction, Methodology, Results slides banao (1.3, 1.4, 1.11–1.15).
- [ ] Final PDF ka naam rakho: **"Data Science Capstone Project Report"** aur upload karo.
- [ ] `08_predictive_analysis_classification.ipynb` chalane ke baad, jo best model results table mein aaye uska naam Conclusion section ke placeholder mein bhar do.
