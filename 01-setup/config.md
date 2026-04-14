# Git Configuration Guide

This step sets your identity and default behavior in Git.

---

## ✅ 1. Set Your Identity (Required)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

📌 These values are attached to every commit you make.

---

## 🔍 2. Verify Configuration

```bash
git config --list
```

Or check individually:

```bash
git config user.name
git config user.email
```

---

## 🌍 3. Global vs Local Config

### Global (applies to all repos)

```bash
git config --global user.name "Your Name"
```

### Local (only current repo)

```bash
git config user.name "Project Specific Name"
```

📌 Local overrides global.

---

## ⚙️ 4. Set Default Branch Name

```bash
git config --global init.defaultBranch main
```

---

## 🧰 5. Useful Configurations

### Enable colored output

```bash
git config --global color.ui auto
```

### Set default editor (VS Code)

```bash
git config --global core.editor "code --wait"
```

### Cache credentials (HTTPS)

```bash
git config --global credential.helper cache
```

---

## 📂 6. Where Config is Stored

* Global config → `~/.gitconfig`
* Local config → `.git/config` (inside repo)

---

## ⚠️ Common Issues

### Wrong email in commits

Fix it:

```bash
git config --global user.email "correct-email@example.com"
```

### Editor not opening

Check:

```bash
git config core.editor
```

---

## 📌 Next Step

Proceed to:

👉 `ssh-setup.md` (recommended for GitLab/GitHub access)
