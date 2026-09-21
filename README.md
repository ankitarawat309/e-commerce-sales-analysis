# E-Commerce Sales Analysis

## 📌 Project Overview

This project analyzes an e-commerce sales dataset using Python to understand sales performance across products, countries, customers, and different months.

I used the Online Retail dataset from the UCI Machine Learning Repository and followed the basic data analysis process of data cleaning, analysis, and visualization.

## 📊 Dataset

- **Source:** UCI Machine Learning Repository
- **Dataset:** Online Retail
- **Records:** 541,909
- **Time Period:** December 2010 – December 2011
- **Business:** UK-based online retailer

Dataset source:  
https://archive.ics.uci.edu/dataset/352/online%2Bretail

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code

## 🧹 Data Cleaning

Before starting the analysis, I checked the dataset for duplicate records, cancelled transactions, missing values, and invalid prices.

The main cleaning steps were:

- Removed duplicate records
- Removed cancelled invoices
- Removed transactions with non-positive unit prices
- Created a new `Sales` column using `Quantity × UnitPrice`
- Checked missing values
- Used available Customer IDs for customer-level analysis

## 📈 Analysis Performed

The analysis covers:

- Total sales
- Total quantity sold
- Number of unique orders
- Average Order Value (AOV)
- Top 10 products by sales
- Top 10 countries by sales
- Monthly sales trends
- Top 10 customers by sales

## 🔍 Key Results

After cleaning and analyzing the data:

- **Total Sales:** £10.64 million
- **Total Quantity Sold:** 5.57 million
- **Unique Orders:** 19,960
- **Average Order Value:** £533.17
- **Highest Sales Month:** November 2011
- **Top Country by Sales:** United Kingdom

## 📊 Visualizations

I created charts to make the analysis easier to understand:

- Monthly Sales Trend
- Top 10 Products by Sales
- Top 10 Countries by Sales
- Top 10 Customers by Sales

The charts are available in the `charts` folder.

## ▶️ How to Run

1. Download the Online Retail dataset from the UCI Machine Learning Repository.
2. Keep `Online Retail.xlsx` in the same folder as `analysis.py`.
3. Install the required libraries:

```bash
pip install pandas openpyxl matplotlib
Run the Python script:
python analysis.py
👩‍💻 Project Purpose

I created this project to practice Python-based data analysis and understand how a real-world sales dataset can be cleaned, analyzed, and visualized.

This project is also part of my Data Analyst portfolio and demonstrates my use of Python, Pandas, and Matplotlib for working with real-world data.
