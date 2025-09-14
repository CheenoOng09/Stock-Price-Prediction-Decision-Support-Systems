
# DSS LSTM Stock Price Prediction

This repository contains our **Decision Support System** class project:  
a **Long Short-Term Memory (LSTM)** deep learning model to predict stock prices and classify risk levels for **SSMI** and **GDAXI** indices.

---

## 📂 Project Structure

```
DSS-LSTM-Stock-Prediction/
├─ notebooks/                 # Jupyter notebooks for training each stock
│  ├─ ssmi_stock_prediction_version_2.ipynb
│  └─ gdaxi_stock_preditcion.ipynb
├─ models/                    # Trained Keras models
│  ├─ ssmi_model.keras
│  ├─ gdaxi_model.keras
├─ data/ (gitignored)         # Cleaned input data (local only)
│  ├─ cleaned_ssmi.csv
│  └─ cleaned_gdaxi.csv
├─ results/                   # Classification results & plots per stock
│  ├─ gdaxi/
│  └─ ssmi/
├─ docs/                      # Report and presentation
│  ├─ Report_DSS_Group_1A.docx
│  └─ PPT_DSS_Group_1A.pdf
├─ src/                       # Application UI
│  └─ main.py
├─ requirements.txt           # Dependencies
├─ .gitignore
└─ README.md
```

---

## 🧠 Overview  

- **Goal**: Predict daily stock prices and classify risk (Conservative / Moderate / Risky) using LSTM neural networks.  
- **Stocks**: SSMI & GDAXI (trained separately).  
- **Risk Classification**: Rolling volatility-based classification on daily and monthly aggregates.  
- **UI**: Tkinter app to compare stocks and visualize risk levels interactively.  

---

## ⚙️ Setup  

Create and activate a virtual environment (example with conda):  

```bash
conda create -n dss-lstm python=3.9 -y
conda activate dss-lstm
pip install -r requirements.txt
```

---

## 🚀 How to Use  

### 1. View Notebooks  
Open notebooks in `notebooks/` to see the full training pipeline for SSMI and GDAXI.  

### 2. Load Trained Models  
Trained models are in `models/ssmi_model.keras` and `models/gdaxi_model.keras`.  
You can load them in Python:  

```python
from tensorflow import keras
ssmi_model = keras.models.load_model("models/ssmi_model.keras")
```

### 3. Explore Results  
- **Classification CSVs** and **plots** per stock under `results/ssmi/` and `results/gdaxi/`.  
- Each folder contains:
  - `monthly_classification.csv`
  - `daily_classification.csv`
  - `future_predictions_ssmi.csv`
  - Plots `1.png` … `7.png`

### 4. Run the UI  
```bash
python src/main.py
```
Load one of the classification CSVs and explore risk categories and attributes.

---

## 📊 Dataset  

We used cleaned daily close prices from two stock indices:  
- `cleaned_ssmi.csv`  
- `cleaned_gdaxi.csv`  



---

## 📝 Requirements  

See `requirements.txt` for the full list (TensorFlow, Pandas, Scikit-Learn, Matplotlib, Joblib).  

---

## 📄 Documentation  

- [Report_DSS_Group_1A.docx](docs/Report_DSS_Group_1A.docx)  
- [PPT_DSS_Group_1A.pdf](docs/PPT_DSS_Group_1A.pdf)

---

### 🔹 License  
Educational / Non-commercial use.

---