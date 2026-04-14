# Git Installation Guide

This guide helps you install Git and verify it is working correctly.

---

## ✅ 1. Check if Git is Already Installed

```bash
git --version
```

If installed, you will see something like:

```
git version 2.x.x
```

---

## 🪟 2. Install Git (Windows)

### Steps:

1. Download Git from:
   https://git-scm.com/download/win

2. Run the installer

### Recommended Options:

* Use Git from command line and 3rd-party software
* Use OpenSSH
* Checkout Windows-style, commit Unix-style line endings

---

## 🐧 3. Install Git (Linux)

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install git -y
```

### RHEL / CentOS

```bash
sudo yum install git -y
```

---

## 🍎 4. Install Git (Mac)

### Using Homebrew

```bash
brew install git
```

### Or using Xcode Command Line Tools

```bash
xcode-select --install
```

---

## 🔍 5. Verify Installation

```bash
git --version
```
