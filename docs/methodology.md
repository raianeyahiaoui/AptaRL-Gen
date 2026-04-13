# Methodology

## 1. Dataset
- Source: AptaBench v2 dataset
- Filtered to DNA sequences only (`type == "DNA"`)
- Target molecule: Procaine (SMILES: `CCN(CC)CCOC(=O)c1ccc(N)cc1`)
- Number of sequences for target: ~160
- Length filter: 30–80 nucleotides

## 2. Oracle Reward Model
- Model: Random Forest Classifier
- Features: 3-mer frequency vectors (using `CountVectorizer`)
- Labels: Binary binding (1 = binder, 0 = non-binder)
- Train/Test split: 80/20 stratified
- Output: Binding probability (used as reward)

## 3. Reinforcement Learning Agent
- Algorithm: REINFORCE (policy gradient)
- Policy Network: GRU-based recurrent network
- Action space: 4 DNA bases (A, C, G, T)
- Sequence length: Fixed at 47 nucleotides (modal length in dataset)
- Reward: Terminal only (oracle binding probability)
- Novelty enforcement: Exact-match penalty during training

## 4. Evaluation Metrics
- Oracle binding probability (mean 0.88 vs 0.22 random)
- Novelty: Average Levenshtein distance = 19.4
- Nucleotide composition (guanine enrichment >60%)
- Simulated biophysical signals:
  - Circular Dichroism (CD) spectrum
  - Surface Plasmon Resonance (SPR) curve
  - Gel Electrophoresis (EMSA) affinity shift

## 5. Implementation Details
- Language: Python
- Libraries: pandas, scikit-learn, PyTorch, RDKit
- Training timesteps: 70,000
- Batch size: 64

---

Last updated: April 2026
