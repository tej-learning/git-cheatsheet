# Switch / Checkout Branch

This guide explains how to move between branches safely.

---

## 🔄 1. Switch to Existing Branch

```bash
git checkout <branch-name>
```

or (modern way):

```bash
git switch <branch-name>
```

---

## 🆕 2. Create and Switch

```bash
git checkout -b <branch-name>
```

or:

```bash
git switch -c <branch-name>
```

---

## 🔙 3. Switch to Previous Branch

```bash
git checkout -
```

👉 Quickly toggles between last two branches

---

## 📋 4. List Branches Before Switching

```bash
git branch
```

---

## ⚠️ 5. Uncommitted Changes Issue

If you have changes and try switching:

```bash
git checkout another-branch
```

👉 Git may block the switch

---

### ✔️ Solutions

#### Option 1: Commit changes

```bash
git add .
git commit -m "save work"
```

#### Option 2: Stash changes

```bash
git stash
git switch <branch>
git stash pop
```

---

## 🔍 6. Check Current Branch

```bash
git branch
```

👉 `*` indicates current branch

---

## 🧠 Checkout vs Switch

| Command        | Use                  |
| -------------- | -------------------- |
| `git checkout` | Older, multi-purpose |
| `git switch`   | New, branch-specific |

👉 Prefer `git switch` for clarity

---

## ⚠️ Common Issues

### ❌ Pathspec error

```text
pathspec 'branch-name' did not match any file(s)
```

👉 Branch does not exist
Check:

```bash
git branch
```

---

### ❌ Detached HEAD (advanced)

```bash
git checkout <commit-id>
```

👉 You are not on a branch

Fix:

```bash
git switch -c new-branch
```

---

## 🧠 Mental Model

```text
Switching = moving HEAD pointer to another branch
```

👉 Your working directory updates accordingly

---

## 📌 Next Step

Proceed to:

👉 `delete-branch.md`
