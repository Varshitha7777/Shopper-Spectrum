import streamlit as st
import pandas as pd
from utils.recommender import build_similarity_matrix, recommend_products
from utils.cluster_predict import predict_cluster

# Load dataset
df = pd.read_csv("data/online_retail_cleaned.csv")
df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Precompute similarity matrix
similarity_df = build_similarity_matrix(df)

# UI
st.title("🛒 Shopper Spectrum")

tab1, tab2 = st.tabs(["📦 Product Recommender", "👤 Customer Segmentation"])

with tab1:
    st.header("📦 Product Recommendation")
    product_input = st.text_input("Enter Product Name")
    if st.button("Get Recommendations"):
        if product_input:
            recommendations = recommend_products(product_input, similarity_df)
            if recommendations:
                st.success("Top 5 Recommended Products:")
                for i, prod in enumerate(recommendations, 1):
                    st.markdown(f"**{i}. {prod}**")
            else:
                st.error("Product not found. Try another.")

with tab2:
    st.header("👤 Predict Customer Segment")
    recency = st.number_input("Recency (days)", min_value=0)
    frequency = st.number_input("Frequency (transactions)", min_value=0)
    monetary = st.number_input("Monetary (total spend)", min_value=0.0)
    
    if st.button("Predict Cluster"):
        label = predict_cluster(recency, frequency, monetary)
        st.success(f"🧠 Predicted Customer Segment: **{label}**")
