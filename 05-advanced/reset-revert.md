# Reset vs Revert

This guide explains how to undo changes in Git using `reset` and `revert`.

---

## 🔄 1. Reset (Rewrite History)

`git reset` moves your branch pointer backward.

```bash
git reset --soft <commit-id>
git reset --mixed <commit-id>
git reset --hard <commit-id>
```

---

## 🧠 Reset Modes

### 🟢 Soft (keep staged changes)

```bash
git reset --soft <commit-id>
```

👉 Moves HEAD, keeps changes staged

---

### 🟡 Mixed (default)

```bash
git reset <commit-id>
```

👉 Moves HEAD, keeps changes in working directory

---

### 🔴 Hard (dangerous)

```bash
git reset --hard <commit-id>
```

👉 Deletes commits + working changes

---

## 🔁 Example

```text
A ── B ── C (HEAD)
```

After:

```bash
git reset --hard B
```

```text
A ── B (HEAD)
```

👉 Commit C is removed

---

## ⚠️ When to Use Reset

* Undo local commits
* Fix mistakes before pushing
* Clean history

---

## 🚫 Never Do This

❗ Do NOT use reset on shared branches

---

## 🔙 2. Revert (Safe Undo)

Creates a new commit that reverses changes

```bash
git revert <commit-id>
```

---

## 🔁 Example

```text
A ── B ── C
```

After revert C:

```text
A ── B ── C ── D
```

👉 D = undo of C

---

## 🧠 Reset vs Revert

| Reset              | Revert            |
| ------------------ | ----------------- |
| Rewrites history   | Preserves history |
| Dangerous (shared) | Safe              |
| Deletes commits    | Adds undo commit  |

---

## ⚠️ Common Issues

### ❌ Lost commits after reset

👉 Use:

```bash
git reflog
```

---

### ❌ Revert conflict

Resolve like merge conflict:

```bash
git add .
git revert --continue
```

---

## 🧠 Mental Model

```text
Reset  = move pointer (erase history)
Revert = add new commit (undo safely)
```

---

## 📌 When to Use What

* Local mistake → `reset`
* Shared repo → `revert`

---

## 📌 Next Step

Proceed to:

👉 `06-workflows/feature-branch.md`
