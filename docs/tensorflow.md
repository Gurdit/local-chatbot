
**# 🧠 Installing TensorFlow on macOS (CPU-only)

This guide walks you through installing TensorFlow on **macOS** using `pip`. These instructions are based on the official [TensorFlow installation guide](https://www.tensorflow.org/install/pip#step-by-step_instructions).

---

## ✅ System Requirements

- macOS **10.12.6 (Sierra)** or higher (64-bit)
- **Python 3.9–3.11**
- **pip >= 20.3**

> **Note:**  
> - TensorFlow supports **Apple Silicon (M1)**, but many third-party TensorFlow packages (e.g., `tensorflow_decision_forests`) may not work natively on M1 and require **x86 emulation with Rosetta**.  
> - Currently, **no official GPU support** is available for TensorFlow on macOS. This setup is for **CPU-only** execution.

---

## 📦 Step 1: Check Your Python Environment

Open a terminal and verify your Python and pip versions:

```bash
python3 --version
python3 -m pip --version
```

## 📦 Step 2: Upgrade pip
To ensure compatibility, upgrade your pip to the latest version:

```bash
python3 -m pip install --upgrade pip
```

## 📦 Step 3:  Install TensorFlow
Now, install TensorFlow with pip:

```bash
pip install tensorflow
```

## 📦 Step 4: Verify Installation
Run the following Python command to check if TensorFlow was installed successfully:

```bash
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

---
# 🧠 Fix: TensorFlow Installation Error on macOS (M1/M2/M3 Chip)

If you're seeing this error when trying to install TensorFlow:

> **Note:**  
> - ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
> - ERROR: No matching distribution found for tensorflow

---

## ❗ Cause

This happens because:
- You are likely using **Python 3.13**, but  
- **TensorFlow only supports up to Python 3.12** (as of June-2025)

---

## ✅ Solution: Use Python 3.11 or 3.12

---

## 🛠 Option 1: Without pyenv

#### ➤ Download Python 3.12 from [Python Releases](https://www.python.org/downloads/macos/)

#### ➤ Verify Installation

```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 --version
```

Expected output:

```bash
Python 3.12.x
```

#### ➤ (Optional) Add it to your PATH or create a symlink

If you want easier access:

```bash
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /usr/local/bin/python3.12
```

Now you can run:

```bash
python3.12 --version
```

#### ➤ Create a virtual environment

```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -m venv local-chatbot
```
```bash
source local-chatbot/bin/activate
```

Then install TensorFlow:

```bash
 cd local-chatbot 
pip install --upgrade pip
pip install tensorflow
```

---

### 🛠 Option 2: With pyenv

> [TODO] – Guide coming soon for pyenv-based installation.

---

### 🛠 Option 3: Using Anaconda Distribution

> [TODO] – Instructions will be added for managing environments via Anaconda/Miniconda.