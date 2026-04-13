# oracle_training.py
# Train Random Forest Oracle on 3-mer features

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_oracle(data_path="processed_procaine_data.csv"):
    print("Loading preprocessed data...")
    df = pd.read_csv(data_path)
    
    # 3-mer feature extraction
    def get_kmers(seq, k=3):
        return " ".join([seq[i:i+k] for i in range(len(seq) - k + 1)])
    
    df['kmers'] = df['sequence'].apply(get_kmers)
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['kmers'])
    y = df['label'].values
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    
    print("Training Random Forest Oracle...")
    oracle = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    oracle.fit(X_train, y_train)
    
    # Evaluate
    train_acc = oracle.score(X_train, y_train)
    test_acc = oracle.score(X_test, y_test)
    print(f"Oracle Train Accuracy: {train_acc:.4f}")
    print(f"Oracle Test Accuracy:  {test_acc:.4f}")
    
    # Save model and vectorizer
    joblib.dump(oracle, "oracle_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("Oracle model and vectorizer saved.")
    
    return oracle, vectorizer


if __name__ == "__main__":
    train_oracle()
