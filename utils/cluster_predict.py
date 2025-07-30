import numpy as np
import pickle

def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

def predict_cluster(recency, frequency, monetary):
    model, scaler = load_model()
    values = np.array([[recency, frequency, monetary]])
    values_scaled = scaler.transform(values)
    cluster = model.predict(values_scaled)[0]

    label_map = {
        0: "High-Value",
        1: "Regular",
        2: "Occasional",
        3: "At-Risk"
    }
    return label_map.get(cluster, f"Cluster {cluster}")
