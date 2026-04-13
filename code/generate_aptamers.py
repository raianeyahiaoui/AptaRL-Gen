# generate_aptamers.py
# Generate novel DNA aptamers using trained oracle + REINFORCE policy

import torch
import torch.nn as nn
import numpy as np
import joblib
import random
from tqdm import tqdm

# Load oracle and vectorizer
oracle = joblib.load("oracle_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

base_to_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
idx_to_base = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

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

# Simple generation function (replace with your full trained model if available)
def generate_aptamer(length=47, temperature=0.8):
    sequence = []
    for _ in range(length):
        # Random base for now - replace with your trained policy later
        base = random.choice(['A', 'C', 'G', 'T'])
        sequence.append(base)
    return ''.join(sequence)


if __name__ == "__main__":
    print("Generating novel DNA aptamers...")
    aptamers = []
    for i in range(10):   # Generate 10 examples
        seq = generate_aptamer()
        aptamers.append(seq)
        print(f"Aptamer {i+1}: {seq}")
    
    # Save generated sequences
    with open("generated_aptamers.fasta", "w") as f:
        for i, seq in enumerate(aptamers):
            f.write(f">Generated_Aptamer_{i+1}\n{seq}\n")
    
    print("\nGenerated sequences saved to generated_aptamers.fasta")
