# BPE and WordPiece Tokenization Lab

## Overview

This project implements a basic version of the Byte Pair Encoding (BPE) algorithm and explores WordPiece tokenization using a pretrained model.

The objective is to understand how modern NLP models transform text into subword units to efficiently handle vocabulary and unknown words.

---

## Academic Information

Academic project for the course Artificial Intelligence Topics  
Professor: Dimmy Magalhães  
Institution: Faculdade iCEV  

---

## Objectives

* Implement the BPE algorithm from scratch
* Perform iterative pair merging
* Analyze token formation
* Explore WordPiece tokenization using Hugging Face

---

## Project Structure

```text
bpe-wordpiece-tokenizer-lab
│
├── core/
│   ├── bpe.py
│   └── wordpiece.py
│
├── main.py
└── README.md
```

---

## How to Run

Install dependencies:

```bash
pip install transformers
```

Run:

```bash
python main.py
```

---

## Example Output

* Most frequent pairs per iteration
* Updated vocabulary after merges
* WordPiece tokenization result

---

## WordPiece Analysis

During tokenization, some tokens appear with the prefix `##`, such as:

* `##mente`
* `##er`

These indicate that the token is a continuation of a previous subword.

This approach allows the model to:

* break unknown words into known sub-parts
* avoid out-of-vocabulary issues
* generalize better across different words

---

## AI-Assisted Complementary Support

AI tools were used in a limited way to assist with:

* minor debugging of the BPE merge logic
* clarification of tokenization behavior

All implementations were reviewed and adapted manually.

Final review:

Carlos Murilo Nogueira Portela

---

## Version

v1.0
