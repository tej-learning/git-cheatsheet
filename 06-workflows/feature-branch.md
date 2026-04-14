# Feature Branch Workflow

This guide explains the most commonly used Git workflow in teams.

---

## 🌿 1. What is Feature Branch Workflow?

Each feature or task is developed in its own branch.

```text
main ───●────●────────●
            \        /
feature      ●──────●
```

👉 Keeps `main` stable
👉 Enables parallel development

---

## 🚀 2. Step-by-Step Flow

### Step 1: Start from main

```bash
git switch main
git pull --rebase
```

---

### Step 2: Create Feature Branch

```bash
git switch -c feature/<name>
```

Example:

```bash
git switch -c feature/login-api
```

---

### Step 3: Work & Commit

```bash
git add .
git commit -m "Add login API"
```

---

### Step 4: Push Branch

```bash
git push -u origin feature/<name>
```

---

### Step 5: Create Merge Request (GitLab)

* Go to GitLab
* Open your repo
* Click **Create Merge Request**
* Select:

  * Source → feature branch
  * Target → main

---

### Step 6: Review & Merge

After approval:

```text
feature branch → merged into main
```

---

### Step 7: Delete Branch

```bash
git branch -d feature/<name>
git push origin --delete feature/<name>
```

---

## 🔁 3. Keep Branch Updated

```bash
git fetch
git rebase origin/main
```

👉 Avoids conflicts later

---

## 🧠 Best Practices

* Keep branches small
* Use meaningful names
* Commit frequently
* Rebase before merge

---

## ⚠️ Common Issues

### ❌ Branch behind main

Fix:

```bash
git pull --rebase origin main
```

---

### ❌ Merge conflicts

👉 Resolve manually before merging

---

### ❌ Large feature branch

👉 Hard to review, avoid this

---

## 🧠 Mental Model

```text
main = stable code
feature branches = isolated work
```

---

## 📌 Next Step

Proceed to:

👉 `gitflow.md`
