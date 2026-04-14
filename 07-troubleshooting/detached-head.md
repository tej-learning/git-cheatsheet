# Detached HEAD

This guide explains what a detached HEAD state is and how to handle it.

---

## 🧠 1. What is HEAD?

HEAD is a pointer to your current branch.

```text
HEAD → main → latest commit
```

---

## ⚠️ 2. What is Detached HEAD?

Detached HEAD means:

```text
HEAD → commit (not a branch)
```

👉 You are not on any branch

---

## 🔍 3. How It Happens

```bash
git checkout <commit-id>
```

or

```bash
git switch --detach <commit-id>
```

---

## 📊 Example

```text
A ── B ── C (main)
```

If you checkout `B`:

```text
HEAD → B
main → C
```

👉 HEAD is detached

---

## ⚠️ 4. Problem with Detached HEAD

If you make commits:

```text
HEAD → B ── D
```

👉 Commit `D` is not attached to any branch
👉 Can be lost later

---

## ✔️ 5. Fix (Create Branch)

```bash
git switch -c new-branch
```

👉 Now:

```text
new-branch → D
```

---

## 🔙 6. Go Back to Normal

```bash
git switch main
```

---

## 🔍 7. Check Current State

```bash
git status
```

👉 Shows:

```text
HEAD detached at <commit-id>
```

---

## ⚠️ Common Issues

### ❌ Lost work

👉 Use:

```bash
git reflog
```

---

### ❌ Confusion during debugging

👉 Detached HEAD is normal when inspecting history

---

## 🧠 Mental Model

```text
Branch = named pointer
HEAD   = current pointer
```

Detached HEAD = HEAD without branch

---

## 📌 When It’s Useful

* Inspect old commits
* Debug issues
* Temporary experimentation

---

## 📌 Next Step

Proceed to:

👉 `undo-mistakes.md`
