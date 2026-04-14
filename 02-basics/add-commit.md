# Add & Commit Changes

This guide covers how to stage and commit changes in Git.

---

## 📌 1. Check Current Status

```bash
git status
```

Shows:

* Modified files
* New (untracked) files
* Staged files

---

## ➕ 2. Stage Changes

### Stage a specific file

```bash
git add <file>
```

### Stage all changes

```bash
git add .
```

### Stage all tracked files only

```bash
git add -u
```

---

## 💾 3. Commit Changes

```bash
git commit -m "your message"
```

📌 This saves a snapshot of staged changes

---

## ⚡ 4. Add + Commit in One Step

```bash
git commit -am "your message"
```

⚠️ Only works for already tracked files

---

## 🧠 5. Best Practices for Commit Messages

* Be clear and concise
* Use present tense
* Focus on *what* and *why*

### Examples:

```text
Add login API validation
Fix null pointer issue in data pipeline
Refactor ETL job for performance
```

---

## 🔍 6. View Commit History

```bash
git log
```

Short format:

```bash
git log --oneline
```

---

## ⚠️ Common Issues

### ❌ Nothing to commit

👉 You forgot to add files:

```bash
git add .
```

---

### ❌ File not staged

Check:

```bash
git status
```

---

### ❌ Wrong commit message

Fix last commit:

```bash
git commit --amend -m "new message"
```

---

## 🧠 Mental Model

```text
Working Directory → Staging Area → Repository
```

* `git add` → moves to staging
* `git commit` → saves permanently

---

## 📌 Next Step

Proceed to:

👉 `status-log.md`
