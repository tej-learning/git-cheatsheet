# Initialize & Clone Repository

This guide covers how to start working with Git repositories.

---

## 🆕 1. Initialize a New Repository (Local Project)

Use this when you already have a project folder and want to track it with Git.

```bash
git init
```

📌 This creates a `.git/` directory (Git starts tracking this folder)

---

### Add first commit

```bash
git add .
git commit -m "Initial commit"
```

---

## 🌐 2. Connect Local Repo to Remote (GitLab)

```bash
git remote add origin git@gitlab.com:<username>/<repo>.git
```

Verify:

```bash
git remote -v
```

---

## ⬆️ Push to Remote

```bash
git branch -M main
git push -u origin main
```

---

## 📥 3. Clone an Existing Repository

Use this when repo already exists on GitLab/GitHub.

```bash
git clone git@gitlab.com:<username>/<repo>.git
```

This will:

* Download code
* Set remote automatically
* Create project folder

---

## 📂 Clone into Specific Folder

```bash
git clone git@gitlab.com:<username>/<repo>.git my-folder
```

---

## 🔍 Verify Setup

```bash
git status
git remote -v
```

---

## ⚠️ Common Issues

### ❌ Permission denied (publickey)

👉 SSH not configured
Fix → check `ssh-setup.md`

---

### ❌ Remote already exists

```bash
git remote remove origin
git remote add origin <url>
```

---

### ❌ Wrong branch name

```bash
git branch -M main
```

---

## 🧠 When to Use What

| Scenario             | Command     |
| -------------------- | ----------- |
| New project          | `git init`  |
| Existing remote repo | `git clone` |

---

## 📌 Next Step

Proceed to:

👉 `add-commit.md`
