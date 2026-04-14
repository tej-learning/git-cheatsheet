# Undo Mistakes

This guide covers common ways to undo changes in Git safely.

---

## 🔄 1. Undo Unstaged Changes

```bash
git checkout -- <file>
```

👉 Discards changes in working directory

---

## 🔄 2. Unstage Files

```bash
git reset <file>
```

👉 Removes file from staging area

---

## 🔄 3. Undo Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```

👉 Commit removed, changes remain staged

---

## 🔄 4. Undo Last Commit (Unstage Changes)

```bash
git reset HEAD~1
```

👉 Changes move back to working directory

---

## 🔄 5. Undo Last Commit (Delete Everything)

```bash
git reset --hard HEAD~1
```

👉 ⚠️ Permanent deletion

---

## 🔙 6. Undo Pushed Commit (Safe Way)

```bash
git revert <commit-id>
```

👉 Creates new commit that reverses changes

---

## 🔍 7. Recover Lost Work

```bash
git reflog
```

Example:

```text
a1b2c3 HEAD@{0}: reset: moving to HEAD~1
d4e5f6 HEAD@{1}: commit: added feature
```

Restore:

```bash
git reset --hard <commit-id>
```

---

## 🧹 8. Remove Untracked Files

```bash
git clean -f
```

Include folders:

```bash
git clean -fd
```

---

## ⚠️ Common Mistakes

### ❌ Using `reset --hard` accidentally

👉 Always double-check before running

---

### ❌ Undoing pushed commits with reset

👉 Breaks team history

---

### ❌ Not using reflog

👉 Most recovery is possible via reflog

---

## 🧠 Mental Model

```text
Working Dir → Staging → Commit History
```

Undo depends on **where the mistake is**

---

## 📌 Quick Reference

| Problem              | Command            |
| -------------------- | ------------------ |
| Undo file changes    | `checkout -- file` |
| Unstage file         | `git reset file`   |
| Undo commit (local)  | `git reset`        |
| Undo commit (remote) | `git revert`       |
| Recover lost work    | `git reflog`       |

---

## 📌 End of Cheatsheet 🎯

You now have:

* Setup
* Basics
* Branching
* Remote
* Advanced
* Workflows
* Troubleshooting

---

# 🧠 Final Thought

Git is not about commands.

👉 It’s about:

```text
tracking changes + managing history safely
```
