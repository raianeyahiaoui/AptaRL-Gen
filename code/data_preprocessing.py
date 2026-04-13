# data_preprocessing.py
# Preprocessing for AptaBench v2 dataset

import pandas as pd

def load_and_preprocess_data(file_path="AptaBench_dataset_v2.csv"):
    """
    Load and preprocess the AptaBench dataset for procaine target.
    """
    print("Loading dataset...")
    df = pd.read_csv(file_path, low_memory=False)
    
    # Filter DNA sequences only
    df = df[df['type'] == 'DNA'].copy()
    df['sequence'] = df['sequence'].str.upper()
    
    # Target molecule: procaine
    target_smiles = "CCN(CC)CCOC(=O)c1ccc(N)cc1"
    
    target_df = df[df['canonical_smiles'] == target_smiles].copy()
    
    print(f"Total sequences for procaine target: {len(target_df)}")
    print(f"Binding (1) count: {target_df['label'].sum()}")
    print(f"Non-binding (0) count: {len(target_df) - target_df['label'].sum()}")
    
    return target_df


if __name__ == "__main__":
    data = load_and_preprocess_data()
    data.to_csv("processed_procaine_data.csv", index=False)
    print("Preprocessed data saved to processed_procaine_data.csv")
