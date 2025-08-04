# 🧹 Task 1: Data Cleaning & Preprocessing

## 📌 Objective
Clean and prepare a raw dataset containing missing values, duplicate records, inconsistent formatting, and mixed data types.

## 🛠 Tools Used
- *Python (Pandas)* for automated data preprocessing
- *Excel* for manual inspection and validation

## 🔍 Process Overview
- Handled missing values using .fillna() and .dropna() as required
- Removed duplicate rows using .drop_duplicates() and Excel's "Remove Duplicates"
- Standardized text fields (e.g., gender, country names) to lowercase and stripped extra whitespace
- Unified date formats to dd-mm-yyyy using pd.to_datetime()
- Renamed column headers for consistency: lowercase letters, no spaces (replaced with underscores)
- Corrected data types (e.g., age → integer, registration_date → datetime)

## ✅ Deliverables
- A cleaned and structured dataset ready for further analysis or modeling
- Screenshots of Excel workflow (optional)
- This README summary

## 🙌 Learning Outcomes
- Gained hands-on experience fixing common data issues
- Understood best practices for data preprocessing
- Improved confidence working with raw datasets
