# 🧬 Reinforcement Learning for De Novo Generation of High-Affinity DNA Aptamers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Author**: Yahiaoui Raiane  
**ORCID**: [0009-0001-7900-6530](https://orcid.org/0009-0001-7900-6530)  
**Affiliation**: Independent Researcher, Blida, Algeria  

**Date**: April 2026

---

## 📖 Overview

This repository contains the code, data preprocessing scripts, and resources for the paper:

> **"Reinforcement Learning for De Novo Generation of High-Affinity DNA Aptamers from Sparse Experimental Data"**

We propose a **REINFORCE** policy-gradient method with a **GRU-based policy network** and a **Random Forest oracle** (trained on 3-mer features) to generate novel DNA aptamers for the small molecule **procaine** using the **AptaBench v2** dataset.

### 🔑 Key Results
- Mean oracle binding probability: **0.88** (vs. **0.22** for random sequences of the same length)
- Average Levenshtein distance to closest training binder: **19.4**
- Strong guanine enrichment: **>60%** with patterns consistent with **G-quadruplex** motifs
- Simulated biophysical signals (CD spectra and SPR curves) support realistic folding and binding behavior

---

## 📂 Repository Structure

RL-DNA-Aptamer-Generation/
├── README.md
├── LICENSE
├── code/
│   ├── data_preprocessing.py
│   ├── oracle_training.py
│   ├── generate_aptamers.py
│   └── requirements.txt
├── paper/
│   ├── main.pdf
│   └── main.tex
├── results/
│   ├── top10_aptamers.csv
│   ├── generated_sequences.fasta
│   └── figures/
├── notebooks/
│   └── exploration.ipynb
└── docs/
    └── methodology.md

## 📚 How to Cite

@misc{yahiaoui2026,
  author       = {Yahiaoui, Raiane},
  title        = {Reinforcement Learning for De Novo Generation of High-Affinity DNA Aptamers from Sparse Experimental Data},
  year         = {2026},
  howpublished = {GitHub},
  note         = {https://github.com/raianeyahiaoui/RL-DNA-Aptamer-Generation}
}


## 📬 Contact
** Email: yahiaouiraiane@gmail.com
** LinkedIn: Yahiaoui Raiane
** GitHub: @raianeyahiaoui 
** ORCID: 0009-0001-7900-6530

## ⚖️ License
** This project is licensed under the MIT License — see the LICENSE file for details.
