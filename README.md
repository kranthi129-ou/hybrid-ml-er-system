# hybrid-ml-er-system

A modular and scalable machine learning-based entity resolution pipeline using **PostgreSQL**, and **LightGBM**. This system performs **blocking**, **feature extraction**, **supervised classification**, and **clustering** to resolve duplicate entities across large structured datasets.

---

## 📁 Project Structure

```
├── data/
│   ├── Abt.csv
│   ├── Buy.csv
│   ├── abt_cleaned.csv
│   ├── buy_cleaned.csv
│   ├── data_cleaning.py
│   └── blocking_parallel.py
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- ✅ Data cleaning with price and text normalization
- ✅ Soundex-based phonetic blocking with intra-block full comparison
- ✅ PostgreSQL integration (reads/writes directly from DB)
- ✅ Spark compatibility for scalable processing (optional for advanced scale-up)
- ✅ CSV and PostgreSQL outputs for each stage

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/kranthi129-ou/hybrid-ml-er-system.git
cd hybrid-ml-er-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. PostgreSQL Setup

- Ensure PostgreSQL is running on `localhost:5432`
- Create a database named: `er_db`
- Create raw tables: `abt_products`, `buy_products`
- Import `Abt.csv` and `Buy.csv` into those tables manually or via script

### 4. Run Data Cleaning

```bash
python data/data_cleaning.py
```

Cleansed data will be:
- Saved as `abt_cleaned.csv`, `buy_cleaned.csv` locally
- Optionally pushed to PostgreSQL as `abt_cleaned`, `buy_cleaned`

---

## 📌 Current Pipeline Status

| Component              | Status       | Notes |
|------------------------|--------------|-------|
| Data Cleaning          | ✅ Completed | With flagging, normalization |
| Soundex Blocking       | 🟡 Designing | Phonetic buckets, intra-block full-join |
| TF-IDF Feature Extract | ⏳ Pending   | For similarity features |
| LightGBM Classifier    | ⏳ Pending   | Supervised match prediction |
| Entity Clustering      | ⏳ Planned   | Threshold-based matching |
| Final Export           | ⏳ Planned   | High-confidence matches |

---

## 🧪 Tech Stack

- Python 3.10
- Pandas, NumPy
- SQLAlchemy, psycopg2
- PostgreSQL
- PySpark (optional but integrated)
- scikit-learn (planned)
- LightGBM (planned)

---

## 📚 References

- [1] ERBlox – Integrating ML and Matching Dependencies
- [4] Papadakis et al. – Blocking Techniques Survey
- [5] ML Comparison for Entity Resolution – Feature Benchmarks

---

## 👨‍💻 Author

**Kranthi Teja** – Graduate student @ University of Oklahoma  
💼 Interests: Data Science, Web Dev, ML, Distributed Systems  
📫 Reach out via GitHub or LinkedIn

---
