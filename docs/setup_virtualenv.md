# 🛠️ How to Set Up a Python Virtual Environment

A virtual environment helps keep your project dependencies isolated, ensuring that packages from one project don’t affect others.

---

## 📘 What is a Virtual Environment?

A **virtual environment** in Python is an isolated workspace on your computer. It allows you to manage dependencies specific to a project without affecting other Python projects or system-wide packages.

---

## 🧱 Creating a Virtual Environment

Python includes a built-in module called `venv` for creating virtual environments.

### 📍 Steps to Create:

1. **Open a terminal or command prompt.**
2. **Navigate** to the folder where you want to create your project.
3. **Run the command below based on your OS:**

#### 🪟 Windows:
```bash
C:\Users\YourName> python -m venv local-chatbot
```

#### 🍏 macOS / Linux:
```bash
python3 -m venv local-chatbot
```

 This will create a folder named `local-chatbot` with subfolders and files, such as:

```
local-chatbot/
├── bin/ (or Scripts/ on Windows)
├── include/
├── lib/
└── pyvenv.cfg
```
