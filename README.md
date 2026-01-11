# 📊 **Data Pipeline Assignment – AccuKnox**


This repository contains **Python-based solutions** for an end-to-end **data pipeline** assignment that demonstrates API integration, data processing, visualization, and database management.

---

## 🧩 **Project Overview**

This project implements a complete data pipeline consisting of three core components:

---

### 🔹 **1. API Data Retrieval & Storage (`books_api.py`)**

* Fetches book information from the **OpenLibrary REST API**
* Parses JSON responses to extract:

  * Book title
  * Author
  * Publication year
* Stores processed data in a local **SQLite database (`books.db`)**
* Displays stored records in a clean console format

**Key Features**

* Automated database & table creation
* Data validation and cleaning
* Structured storage & retrieval

---

### 🔹 **2. Data Processing & Visualization (`student_scores.py`)**

* Retrieves student score data from an external API
* Processes the dataset and calculates average scores
* Generates a professional **bar chart visualization** (`scores_chart.png`) using `matplotlib`

**Key Features**

* Data aggregation & transformation
* Statistical analysis (average computation)
* Visual reporting for quick insights

---

### 🔹 **3. CSV to Database Ingestion (`csv_to_db.py`)**

* Reads structured user data from a CSV file (`users.csv`)
* Transfers records into a local **SQLite database (`users.db`)**
* Verifies inserted data via console output

**Key Features**

* Schema validation
* Duplicate prevention (`INSERT OR IGNORE`)
* Reliable ETL-style ingestion pipeline

---

## 🚀 **Getting Started**

### 🧰 Prerequisites

* Python 3.x
* Required libraries:

```bash
pip install requests matplotlib
```

---

### 🛠️ Installation

```bash
git clone https://github.com/Vinay889900/data_pipeline.git
cd data_pipeline
```

---

## ▶️ **Running the Pipelines**

### 📚 Run Book Data Pipeline

```bash
python books_api.py
```

### 📈 Generate Student Score Visualization

```bash
python student_scores.py
```

### 🧾 Import CSV Data into Database

```bash
python csv_to_db.py
```

---

## 🧪 **Technology Stack**

| Layer         | Tools                  |
| ------------- | ---------------------- |
| Language      | Python 3               |
| Database      | SQLite3                |
| APIs          | OpenLibrary REST API   |
| Visualization | Matplotlib             |
| Data Handling | Requests, CSV, SQLite3 |

---

## 🔍 **Verification & Inspection**

You may verify stored data using:

* Script output logs
* **DB Browser for SQLite** to inspect:

  * `books.db`
  * `users.db`

This enables easy validation of database integrity and stored records.

---

## 🧠 **What This Project Demonstrates**

✔ Real REST API integration
✔ End-to-end data pipeline design
✔ Database creation & management
✔ Data processing & analytics
✔ Professional visualization & reporting
✔ Clean, reproducible, evaluation-ready code
