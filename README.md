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

---

## 🧪 Git Commands

### Commands used during the task:
```bash
git init
git add .
git remote add origin https://github.com/your-username/DevOps-Task4.git
git branch -M main
git push -u origin main

git checkout -b dev
git push -u origin dev
git checkout -b feature/reset-file-if-empty
git add .
git commit -m "Add reset functionality"
git push origin feature/reset-file-if-empty

# Create Pull Request on GitHub: feature → dev
# Merge dev → main

git add .gitignore
git commit -m "Add .gitignore to exclude cache and tasks file"
git push

git tag v1.0
git tag v1.1
git push origin --tags
