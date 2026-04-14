# Diff (View Changes)

This guide explains how to see differences between files, stages, and commits.

---

## 🔍 1. View Unstaged Changes

```bash
git diff
```

👉 Shows changes in working directory (not yet staged)

---

## 📌 2. View Staged Changes

```bash
git diff --staged
```

👉 Shows what will be included in next commit

---

## 📄 3. Diff for Specific File

```bash
git diff <file>
```

---

## 🆚 4. Compare Two Commits

```bash
git diff <commit1> <commit2>
```

---

## 🔁 5. Compare Branches

```bash
git diff branch1 branch2
```

---

## 📊 6. Summary of Changes

```bash
git diff --stat
```

👉 Shows number of changes per file

---

## 🔢 7. Word-Level Diff

```bash
git diff --word-diff
```

👉 Useful for small text changes

---

## 🧠 How to Read Diff Output

```diff
- old line (removed)
+ new line (added)
```

---

## ⚠️ Common Issues

### ❌ No output from `git diff`

👉 Means no unstaged changes
OR changes already staged

---

### ❌ Confused between staged vs unstaged

Use both:

```bash
git diff
git diff --staged
```

---

## 🧠 Mental Model

```text
Working Directory ── git diff ──> unstaged changes
Staging Area      ── git diff --staged ──> staged changes
```

---

## 📌 When to Use

* Before committing → verify changes
* During debugging → see exact modifications
* During code review → understand differences

---

## 📌 Next Step

Proceed to:

👉 `03-branching/create-branch.md`
