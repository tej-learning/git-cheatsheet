# Git Command Handbook

A structured, practical reference for Git commands, workflows, and troubleshooting.

---

## 🚀 How to Use This Repo

Follow this order if you're learning:

```text
01-setup → 02-basics → 03-branching → 04-remote → 05-advanced → 06-workflows → 07-troubleshooting
```

If you're experienced:

👉 Jump directly to the section you need

---

## 📂 Repository Structure

### 🧱 Setup

* Install Git
* Configure identity
* Setup SSH

📁 `01-setup/`

---

### ⚙️ Basics

* Initialize / clone repo
* Add & commit
* Status, log, diff

📁 `02-basics/`

---

### 🌿 Branching

* Create, switch, delete branches
* Merge branches

📁 `03-branching/`

---

### 🌐 Remote

* Push, pull, fetch
* Upstream tracking

📁 `04-remote/`

---

### 🧠 Advanced

* Rebase
* Stash
* Cherry-pick
* Reset vs revert

📁 `05-advanced/`

---

### 🔄 Workflows

* Feature branch workflow
* GitFlow
* Hotfix handling

📁 `06-workflows/`

---

### 🛠️ Troubleshooting

* Merge conflicts
* Permission issues
* Detached HEAD
* Undo mistakes

📁 `07-troubleshooting/`

---

## ⚡ Quick Commands

```bash
git status
git add .
git commit -m "message"
git push
git pull --rebase
```

---

## 🎯 Goal of This Repository

* Provide **clear, structured Git knowledge**
* Act as a **quick reference during real work**
* Help debug **real-world issues**
* Build strong understanding of **Git internals**

---

## 🧠 Core Concepts

```text
Working Directory → Staging Area → Repository
Branch = pointer
HEAD = current pointer
```

---

## ⚠️ Important Rules

* Do not use `git reset --hard` on shared branches
* Prefer `git pull --rebase` over merge
* Use feature branches (avoid direct commits to main)
* Always check `git status` before actions

---

## 🔥 Pro Tips

* Use `git log --oneline --graph` for visualization
* Use `git reflog` to recover lost work
* Keep commits small and meaningful
* Pull frequently to avoid conflicts

---

## 📌 Future Additions

* Real-world scenarios (debugging flows)
* Advanced Git internals
* Hooks and automation

---

## 🧠 Final Thought

Git is not just commands.

It is:

```text
A system to track, manage, and safely evolve code over time
```
