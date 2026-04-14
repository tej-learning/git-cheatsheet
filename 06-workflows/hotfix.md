# Hotfix Workflow

This guide explains how to quickly fix production issues using hotfix branches.

---

## 🚨 1. What is a Hotfix?

A hotfix is a **critical fix applied directly to production code**.

👉 Used when:

* Bug in production
* System failure
* Urgent patch required

---

## 🌳 2. Where Hotfix Starts

Hotfix branches are created from `main` (production branch)

```text
main ───●────●
           \
hotfix      ●
```

---

## 🚀 3. Create Hotfix Branch

```bash
git switch main
git pull --rebase
git switch -c hotfix/<issue-name>
```

Example:

```bash
git switch -c hotfix/payment-failure
```

---

## 🔧 4. Fix & Commit

```bash
git add .
git commit -m "Fix payment failure bug"
```

---

## ⬆️ 5. Push Hotfix

```bash
git push -u origin hotfix/<issue-name>
```

---

## 🔀 6. Merge Hotfix

### Merge into main (production)

```bash
git switch main
git merge hotfix/<issue-name>
```

---

### Merge into develop (important)

```bash
git switch develop
git merge hotfix/<issue-name>
```

👉 Ensures fix is not lost in future releases

---

## 🗑️ 7. Cleanup

```bash
git branch -d hotfix/<issue-name>
git push origin --delete hotfix/<issue-name>
```

---

## ⚠️ Common Mistakes

### ❌ Creating hotfix from develop

👉 Wrong base → not production state

---

### ❌ Not merging into develop

👉 Fix disappears in next release

---

### ❌ Delayed hotfix

👉 Always prioritize production issues

---

## 🧠 Mental Model

```text
Hotfix = emergency branch from production
```

👉 Fast → isolated → merged back everywhere

---

## 📌 When to Use

* Critical bugs
* Production outages
* Immediate fixes

---

## 📌 Next Step

Proceed to:

👉 `07-troubleshooting/merge-conflicts.md`
