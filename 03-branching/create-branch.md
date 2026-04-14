# Create Branch

This guide explains how to create and manage branches in Git.

---

## 🌿 1. What is a Branch?

A branch is an independent line of development.

```text
main ────●────●────●
             \
feature ──────●────●
```

👉 Allows you to work without affecting main code

---

## ➕ 2. Create a New Branch

```bash
git branch <branch-name>
```

Example:

```bash
git branch feature/login
```

---

## 🔄 3. Switch to a Branch

```bash
git checkout <branch-name>
```

---

## ⚡ 4. Create + Switch (Recommended)

```bash
git checkout -b <branch-name>
```

Example:

```bash
git checkout -b feature/api
```

---

## 🆕 5. Modern Alternative (Preferred)

```bash
git switch -c <branch-name>
```

---

## 📋 6. List Branches

```bash
git branch
```

Current branch will have `*`

---

## 🌐 7. Push Branch to Remote

```bash
git push -u origin <branch-name>
```

👉 `-u` sets upstream tracking

---

## 🧠 Naming Best Practices

```text
feature/login
bugfix/null-pointer
hotfix/payment-error
```

---

## ⚠️ Common Issues

### ❌ Branch already exists

```bash
git branch
```

---

### ❌ Changes lost when switching

👉 Commit or stash before switching

---

### ❌ Forgot to switch branch

Check:

```bash
git branch
```

---

## 🧠 Mental Model

```text
Branch = pointer to a commit
```

👉 Creating a branch does NOT copy files
👉 It just creates a new reference

---

## 📌 Next Step

Proceed to:

👉 `switch-checkout.md`
