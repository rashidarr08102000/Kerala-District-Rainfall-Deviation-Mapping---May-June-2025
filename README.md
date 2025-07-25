# Kerala District Rainfall Deviation Mapping – May & June 2025

This project visualizes actual vs. normal rainfall in **Kerala** for **May and June 2025** using **GeoPandas and Matplotlib in Python**.  
It derives **deviation maps** by comparing actual and normal rainfall data to highlight **above- or below-normal rainfall zones** across districts.  
Intended solely for **educational purposes**.

---

## Core Project Idea 💡

The project aims to:
- Compare **actual rainfall** against **normal rainfall**
- Generate **district-wise deviation maps** for May and June 2025
- Help visualize rainfall anomalies (deficit/surplus) using Python-based spatial data analysis

---

## Data Source 🔍

- Rainfall data (actual and normal) was collected from the **Kerala WRIS**:  
  🔗 [https://wris.kerala.gov.in/](https://wris.kerala.gov.in/)

- District boundaries shapefile was manually prepared using ArcGIS and verified for alignments
---
## Folder Contents 📂

📂 Kerala_Rainfall_Deviation_2025/
├── Export_Output.shp, .shx, .dbf, .prj       ← Shapefile components (district boundaries)
│
├── rainfall_kerala_normal.xlsx               ← Normal rainfall data
├── rainfall_kerala_actual.xlsx               ← Actual rainfall data
├── rainfall_kerala.xlsx                      ← Original combined Excel sheet (optional)
│
├── rainfall_actual_map.py                    ← Script: Actual rainfall maps
├── rainfall_normal_map.py                    ← Script: Normal rainfall maps
├── rainfall_deviation_map.py                 ← Script: Deviation maps
│
│   📄 Individual output maps
├── Actual_May.png                            
├── Actual_June.png
├── Normal_May.png
├── Normal_June.png
├── Deviation_May.png
├── Deviation_June.png
│
├── Rainfall Map_25May.jpg                    ← Collage for May (Actual, Normal, Deviation)
├── Rainfall Map_25June.jpg                   ← Collage for June (Actual, Normal, Deviation)

## 📊 Output Maps

- May 2025 – Actual, Normal, and Deviation
- June 2025 – Actual, Normal, and Deviation

---

## 📜 License

This project is licensed under the **MIT License**.  
Note: Rainfall data belongs to **Kerala WRIS** and is used strictly for **educational purposes only**.

---

## ✍️ Author

Created by **Rashida RR**  
