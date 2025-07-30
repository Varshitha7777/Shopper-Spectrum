# 🛒 Shopper Spectrum

**Customer Segmentation and Product Recommendation System for E-Commerce**

---

## 📌 Problem Statement

The global e-commerce industry generates vast transaction data daily. Analyzing this data helps in identifying meaningful customer segments and offering personalized product recommendations to enhance customer satisfaction and business performance.

This project aims to:
- Segment customers using **RFM Analysis**
- Recommend products using **Collaborative Filtering**
- Deploy the entire solution using **Streamlit**

---

## 💡 Skills Gained

- Public Dataset Exploration & Preprocessing
- Data Cleaning & Feature Engineering
- Exploratory Data Analysis (EDA)
- Clustering Algorithms (K-Means)
- Item-based Collaborative Filtering
- Model Evaluation & Deployment
- Streamlit Web App Development

---

## 🧠 Project Type

- **Unsupervised Learning** (Clustering)
- **Recommendation System** (Collaborative Filtering)

---

## 📊 Dataset Description

| Column      | Description                          |
|-------------|--------------------------------------|
| InvoiceNo   | Transaction number                   |
| StockCode   | Unique product/item code             |
| Description | Product name                         |
| Quantity    | Number of products purchased         |
| InvoiceDate | Date and time of transaction         |
| UnitPrice   | Price per product                    |
| CustomerID  | Unique ID per customer               |
| Country     | Customer’s country                   |

---

## 🔧 Project Pipeline

### Step 1: Dataset Preparation
- Explore data structure
- Handle missing values, duplicates, and invalid entries

### Step 2: Preprocessing
- Remove rows with missing `CustomerID`
- Remove canceled invoices (`InvoiceNo` starts with 'C')
- Exclude negative or zero quantities/prices

### Step 3: Exploratory Data Analysis (EDA)
- Country-wise transaction volume
- Top-selling products
- Time-based purchase trends
- RFM distributions
- Elbow curve for optimal clusters

### Step 4: RFM Feature Engineering & Clustering
- Recency = Days since last purchase
- Frequency = Number of purchases
- Monetary = Total amount spent
- Standardize features
- Apply K-Means clustering
- Label segments:
  - High-Value
  - Regular
  - Occasional
  - At-Risk
- Visualize customer clusters

### Step 5: Product Recommendation
- Item-based collaborative filtering
- Compute cosine similarity matrix (CustomerID × StockCode)
- Recommend top 5 similar products to a given product



