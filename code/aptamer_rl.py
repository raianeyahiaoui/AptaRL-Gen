# aptamer_rl.py
# Reinforcement Learning for De Novo DNA Aptamer Generation
# Author: Yahiaoui Raiane
# Date: April 2026

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import random

# ==========================
# 1. Load and Prepare Data
# ==========================
print("Loading AptaBench dataset...")
df = pd.read_csv("AptaBench_dataset_v2.csv")

# Focus on DNA and the target molecule (procaine)
target_smiles = "CCN(CC)CCOC(=O)c1ccc(N)cc1"   # procaine SMILES
target_df = df[(df['canonical_smiles'] == target_smiles) & (df['type'] == 'DNA')].copy()

print(f"Number of sequences for target: {len(target_df)}")

# 3-mer feature extraction
def get_kmers(seq, k=3):
    return " ".join([seq[i:i+k] for i in range(len(seq)-k+1)])

target_df['kmers'] = target_df['sequence'].apply(get_kmers)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(target_df['kmers'])
y = target_df['label'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# ==========================
# 2. Train Oracle (Random Forest)
# ==========================
print("Training Random Forest Oracle...")
oracle = RandomForestClassifier(n_estimators=200, random_state=42)
oracle.fit(X_train, y_train)

# Evaluate oracle
train_acc = oracle.score(X_train, y_train)
test_acc = oracle.score(X_test, y_test)
print(f"Oracle Train Accuracy: {train_acc:.4f}")
print(f"Oracle Test Accuracy:  {test_acc:.4f}")

# ==========================
# 3. Reinforcement Learning Agent (REINFORCE + GRU)
# ==========================
class GRUPolicy(nn.Module):
    def __init__(self, vocab_size=4, embed_dim=64, hidden_dim=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.gru = nn.GRU(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, x):
        x = self.embedding(x)
        output, _ = self.gru(x)
        logits = self.fc(output[:, -1, :])
        return logits

# Base mapping
base_to_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
idx_to_base = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

# Simple REINFORCE training loop (placeholder - replace with your full working code)
# ... (Add your actual training loop here from the successful 3rd code)

print("Model and training setup ready.")

# ==========================
# 4. Generate Aptamers
# ==========================
def generate_aptamer(model, length=47, temperature=0.8):
    # Your generation function here
    pass

print("Ready to generate novel DNA aptamers.")
