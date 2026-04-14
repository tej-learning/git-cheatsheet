# Status & Log

This guide helps you inspect the current state and history of your repository.

---

## 📌 1. Check Current Status

```bash
git status
```

Shows:

* Modified files
* Untracked files
* Staged changes
* Current branch

---

## 🔍 2. Short Status (Compact View)

```bash
git status -s
```

Example output:

```text
M  file1.py
?? file2.py
```

Legend:

* `M` → Modified
* `A` → Added
* `??` → Untracked

---

## 📜 3. View Commit History

```bash
git log
```

Shows:

* Commit hash
* Author
* Date
* Message

---

## ⚡ 4. Compact Log

```bash
git log --oneline
```

Example:

```text
a1b2c3d Fix bug in pipeline
e4f5g6h Add new feature
```

---

## 🌳 5. Visual Graph (Very Useful)

```bash
git log --oneline --graph --all
```

👉 Helps visualize branches and merges

---

## 🔎 6. Show Changes in a Commit

```bash
git show <commit-id>
```

---

## 👤 7. Filter by Author

```bash
git log --author="Your Name"
```

---

## 📅 8. Filter by Time

```bash
git log --since="2 days ago"
```

---

## ⚠️ Common Issues

### ❌ Too many logs

Limit output:

```bash
git log -n 5
```

---

### ❌ Hard to read logs

Use:

```bash
git log --oneline
```

---

## 🧠 Mental Model

```text
git status → current state (working area)
git log    → history (committed snapshots)
```

---

## 📌 Next Step

Proceed to:

👉 `diff.md`
