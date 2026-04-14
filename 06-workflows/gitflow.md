# GitFlow Workflow

This guide explains the GitFlow branching model used for structured development and releases.

---

## 🧠 1. What is GitFlow?

GitFlow is a branching strategy with dedicated branches for development and releases.

---

## 🌳 2. Branch Structure

```text
main      → production-ready code  
develop   → integration branch  

feature/* → new features  
release/* → release preparation  
hotfix/*  → urgent production fixes  
```

---

## 🔀 3. Visual Flow

```text
main ────────●────────────●
              \          /
develop ──────●────●────●
               \    \
feature         ●    ●
```

---

## 🚀 4. Feature Development

```bash
git switch develop
git switch -c feature/<name>
```

After work:

```bash
git switch develop
git merge feature/<name>
```

---

## 📦 5. Create Release Branch

```bash
git switch develop
git switch -c release/v1.0
```

👉 Used for:

* Final testing
* Bug fixes

---

## 🚢 6. Merge Release

```bash
git switch main
git merge release/v1.0

git switch develop
git merge release/v1.0
```

👉 Keeps both branches updated

---

## 🚨 7. Hotfix (Production Fix)

```bash
git switch main
git switch -c hotfix/critical-bug
```

After fix:

```bash
git switch main
git merge hotfix/critical-bug

git switch develop
git merge hotfix/critical-bug
```

---

## 🧠 Why GitFlow?

* Structured releases
* Clear separation of environments
* Good for large teams

---

## ⚠️ Downsides

* Complex
* Slower workflow
* Overkill for small teams

---

## 🧠 Mental Model

```text
main    = production
develop = ongoing work
others  = temporary branches
```

---

## 📌 When to Use

* Enterprise projects
* Release cycles
* Multiple environments

---

## 📌 Next Step

Proceed to:

👉 `hotfix.md`
