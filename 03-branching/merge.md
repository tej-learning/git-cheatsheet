# Merge Branch

This guide explains how to combine changes from one branch into another.

---

## 🔀 1. What is Merge?

Merging integrates changes from one branch into another.

```text id="9z9y2y"
main ───●────●
            \
feature ─────●────●
```

After merge:

```text id="3l2k3m"
main ───●────●────●
            \    /
feature ─────●──●
```

---

## 📥 2. Merge a Branch

Step 1: Switch to target branch (usually main)

```bash id="c2p4ai"
git switch main
```

Step 2: Merge feature branch

```bash id="2y6m7x"
git merge <branch-name>
```

---

## ⚡ 3. Fast-Forward Merge

If no divergence:

```text id="gq7n6d"
main ───●────●
feature         ↑
```

👉 Git moves pointer forward (no extra commit)

---

## 🔗 4. Merge Commit (Non Fast-Forward)

If both branches changed:

👉 Git creates a **merge commit**

---

## ⚠️ 5. Merge Conflicts

Occurs when same lines are modified in both branches

```text id="u8wq5p"
<<<<<<< HEAD
your changes
=======
incoming changes
>>>>>>> branch
```

---

### ✔️ Resolve Conflict

1. Open file
2. Edit manually
3. Remove conflict markers
4. Save file

Then:

```bash id="6z3p8k"
git add <file>
git commit
```

---

## 🔍 6. Check Merge Status

```bash id="k8d3yq"
git status
```

---

## ❌ 7. Abort Merge (if needed)

```bash id="8x3v6n"
git merge --abort
```

---

## 🧠 Best Practices

* Always pull latest before merging
* Keep branches small and focused
* Resolve conflicts carefully

---

## ⚠️ Common Issues

### ❌ Already up to date

👉 No new changes to merge

---

### ❌ Conflict confusion

Use:

```bash id="l5f7pq"
git status
```

---

## 🧠 Mental Model

```text id="d3xv7w"
Merge = combining histories of two branches
```

---

## 📌 Next Step

Proceed to:

👉 `04-remote/push.md`
