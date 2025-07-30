import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_similarity_matrix(df):
    user_item = df.pivot_table(index='CustomerID', columns='Description', values='Quantity', aggfunc='sum', fill_value=0)
    similarity = cosine_similarity(user_item.T)
    sim_df = pd.DataFrame(similarity, index=user_item.columns, columns=user_item.columns)
    return sim_df

def recommend_products(product_name, similarity_df, top_n=5):
    if product_name not in similarity_df.columns:
        return []
    sim_scores = similarity_df[product_name].sort_values(ascending=False)
    return sim_scores.iloc[1:top_n+1].index.tolist()
