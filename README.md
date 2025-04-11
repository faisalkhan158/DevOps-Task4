# 🚀 DevOps Task 4 – Build a Version-Controlled DevOps Project with Git

## 📌 Objective  
Implement a version-controlled DevOps project using Git and GitHub best practice

---

## 🛠️ Tools & Technologies  
- Git  
- GitHub  
- Python  

---

## ✅ Project Overview  
This project is a **To-Do List CLI App** built in Python and version-controlled using **Git best practices** such as branching, pull requests, commit hygiene, tags, and a `.gitignore` file.

---

## 🔁 Git Workflow  
- Initialized local repo and pushed to GitHub  
- Branches created:
  - `main` – production/stable
  - `dev` – development
  - `feature/reset-file-if-empty` – feature enhancement  
- Pull Request flow:
  1. `feature/reset-file-if-empty` → `dev`
  2. `dev` → `main`  
- Created version tag after merge

---

## 🧪 How to Run the App
```bash
cd app
python todo.py
