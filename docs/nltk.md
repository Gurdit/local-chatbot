
# 🧠 Installing Natural Language Toolkit (NLTK)

This guide walks you through installing NLTK on **macOS** using `pip`. These instructions are based on the official [NLTK installation guide](https://pypi.org/project/nltk/).

---

## 📦 Step 1:  Install Natural Language Toolkit (NLTK)
Install NLTK with pip:

```bash
pip install nltk
```

## 📦 Step 4: Verify Installation
After installing NLTK, verify the installation by running the following in a Python shell or script:

```bash
pip show nltk
```
If NLTK is installed, it will show package metadata:
```text
Name: nltk
Version: 3.9.1
Summary: Natural Language Toolkit
...
```

---

## NLTK Resources Script

Before running any NLP-related scripts, you need to download the necessary NLTK resources.

### Purpose
The `download_nltk_data.py` script sets up your environment for Natural Language Processing tasks by:
1. Fixing SSL certificate issues (if any) for securing HTTPS downloads.
2. Downloading required NLTK resources like:
   - Tokenization support (`punkt_tab`)
   - WordNet (`wordnet`) for lemmatization and lexical analysis
   - Multilingual extensions for WordNet (`omw-1.4`)

### Usage
Run the script using the following command:

```bash
 python3 download_nltk_data.py
```