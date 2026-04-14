# Rebase

This guide explains how to reapply commits on top of another base branch.

---

## 🔁 1. What is Rebase?

Rebase moves your branch to a new base.

```text
Before:

main    ───A────B
             \
feature       C────D
```

After rebase:

```text
main    ───A────B
                  \
feature            C'───D'
```

👉 Commits are **recreated** (new hashes)

---

## ⚡ 2. Basic Rebase

```bash
git switch feature
git rebase main
```

👉 Applies feature commits on top of latest main

---

## 🔄 3. Rebase vs Merge

| Merge                | Rebase           |
| -------------------- | ---------------- |
| Keeps history        | Rewrites history |
| Creates merge commit | No merge commit  |
| Non-linear graph     | Linear history   |

---

## 🧪 4. Interactive Rebase (Powerful)

```bash
git rebase -i HEAD~3
```

👉 Lets you:

* edit commits
* squash commits
* reorder commits

---

## ✏️ Example (Squash)

```text
pick a1b2c3 add feature
squash d4e5f6 fix typo
```

👉 Combines commits into one

---

## ⚠️ 5. Resolve Conflicts During Rebase

If conflict occurs:

1. Fix file manually
2. Then:

```bash
git add .
git rebase --continue
```

---

## ❌ 6. Abort Rebase

```bash
git rebase --abort
```

---

## ⚠️ Important Rule

❗ **Never rebase shared/public branches**

👉 Only rebase your own feature branches

---

## 🧠 Mental Model

```text
Rebase = replay commits on new base
```

👉 History is rewritten
👉 Commit IDs change

---

## 📌 When to Use

* Clean up commit history
* Update feature branch with latest main
* Before merging (for linear history)

---

## 📌 Next Step

Proceed to:

👉 `stash.md`
