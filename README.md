# E-Commerce Sales Analysis

## 📌 Project Overview

This project focuses on analyzing real-world e-commerce sales data using Python. The goal was to clean the data, understand sales performance, identify useful patterns, and present the findings through visualizations.

The project uses the Online Retail dataset from the UCI Machine Learning Repository. The dataset contains transactions from a UK-based online retailer between December 2010 and December 2011.

---

## 🎯 Project Purpose

I created this project to practice Python-based data analysis using a real-world dataset and understand the complete data analysis process — from raw data cleaning to analysis and visualization.

This project is also part of my Data Analyst portfolio and demonstrates my practical use of Python, Pandas, and Matplotlib.

---

## 📂 Dataset

Dataset: Online Retail  
Source: UCI Machine Learning Repository  
Original Records: 541,909  
Time Period: December 2010 – December 2011  
Country: United Kingdom

The dataset contains information such as:

- Invoice number
- Product code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

The original dataset is not included in this repository because it is a large file. It can be downloaded from the UCI Machine Learning Repository.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

---

## 🧹 Data Cleaning

Before starting the analysis, I cleaned the dataset by:

- Removing duplicate records
- Identifying and excluding cancelled invoices
- Removing transactions with zero or negative unit prices
- Creating a new Sales column using Quantity × UnitPrice
- Checking missing values
- Preparing the data for analysis

After cleaning, the dataset contained 524,878 transaction records.

---

## 📊 Analysis Performed

The analysis focuses on several important business questions:

- What are the total sales?
- How many products were sold?
- How many unique orders were placed?
- Which products generated the highest sales?
- Which countries generated the highest sales?
- How did sales change month by month?
- Which customers generated the highest sales?
- What was the average order value?

---

## 📈 Key Results

Some of the main results from the analysis are:

- Total Sales: £10.64 million
- Total Quantity Sold: 5.57 million units
- Unique Orders: 19,960
- Average Order Value: £533.17
- Top Country by Sales: United Kingdom
- Highest Sales Month: November 2011
- Top Product by Sales: DOTCOM POSTAGE
- Top Customer by Sales: Customer ID 14646

These results helped me understand how sales were distributed across products, countries, customers, and different months.

---

## 📉 Visualizations

I created the following charts to make the analysis easier to understand:

- Monthly Sales Trend
- Top 10 Products by Sales
- Top 10 Countries by Sales
- Top 10 Customers by Sales

The charts are included in this repository.

---

## ▶️ How to Run

### 1. Download the Dataset

Download the Online Retail dataset from the UCI Machine Learning Repository.

### 2. Place the Dataset

Keep Online Retail.xlsx in the same folder as analysis.py.

### 3. Install Required Libraries

    pip install pandas openpyxl matplotlib

### 4. Run the Python Script

    python analysis.py

The script will clean the data, perform the analysis, and generate the charts.

---

## 📁 Project Structure

    e-commerce-sales-analysis/
    │
    ├── analysis.py
    ├── README.md
    ├── .gitignore
    ├── monthly_sales.png
    ├── top_products.png
    ├── top_countries.png
    └── top_customers.png

---

## 💡 What I Learned

Through this project, I practiced:

- Working with a real-world dataset
- Data cleaning using Pandas
- Handling missing and duplicate data
- Creating calculated columns
- Grouping and aggregating data
- Finding business insights from data
- Working with dates and monthly trends
- Creating visualizations using Matplotlib
- Documenting a data analysis project
- Using GitHub to present a project

---

## 🔎 Conclusion

This project gave me practical experience with the complete data analysis workflow — starting with raw transaction data, cleaning and preparing it, performing analysis, and presenting the findings through visualizations.

It also helped me understand how Python can be used to answer practical business questions from real-world data.
