# Delete Branch

This guide explains how to safely delete local and remote branches.

---

## 🗑️ 1. Delete Local Branch

```bash id="g8w0lw"
git branch -d <branch-name>
```

👉 Deletes branch **only if it is fully merged**

---

## ⚠️ 2. Force Delete Local Branch

```bash id="1z6qvd"
git branch -D <branch-name>
```

👉 Deletes branch even if not merged (use carefully)

---

## 🌐 3. Delete Remote Branch

```bash id="7cdb0z"
git push origin --delete <branch-name>
```

---

## 📋 4. List Branches Before Deleting

```bash id="e0b3h3"
git branch
```

Remote branches:

```bash id="s3av0m"
git branch -r
```

---

## 🚫 5. Cannot Delete Current Branch

If you try:

```bash id="p5k1db"
git branch -d main
```

👉 Error: cannot delete checked-out branch

### ✔️ Fix:

```bash id="klq9ci"
git switch another-branch
```

---

## 🧠 6. Safe vs Force Delete

| Command | Behavior            |
| ------- | ------------------- |
| `-d`    | Safe (checks merge) |
| `-D`    | Force (no checks)   |

---

## ⚠️ Common Issues

### ❌ Branch not fully merged

```text id="t9qv0u"
error: The branch is not fully merged
```

👉 Use:

```bash id="9u7cby"
git branch -D <branch-name>
```

---

### ❌ Remote branch still visible

👉 Fetch latest state:

```bash id="0jxj9q"
git fetch -p
```

---

## 🧠 Mental Model

```text id="5pgvav"
Deleting a branch = removing a pointer
```

👉 Commits are not immediately deleted
👉 They remain until garbage collection

---

## 📌 When to Delete

* After merging feature branch
* Cleaning up old branches
* Removing unused work

---

## 📌 Next Step

Proceed to:

👉 `merge.md`
