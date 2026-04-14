# Merge Conflicts

This guide explains why merge conflicts occur and how to resolve them safely.

---

## ⚠️ 1. What is a Merge Conflict?

A conflict happens when Git cannot automatically merge changes.

👉 Typically when:

* Same file
* Same lines
* Different changes

---

## 🔀 Example

```text id="c9k2ft"
Branch A:   price = 100
Branch B:   price = 200
```

👉 Git doesn’t know which one to keep

---

## 🧾 2. Conflict Markers

```text id="x4p8mq"
<<<<<<< HEAD
your changes
=======
incoming changes
>>>>>>> branch-name
```

---

## 🔧 3. Resolve Conflict (Step-by-Step)

### Step 1: Open file

### Step 2: Decide final code

### Step 3: Remove markers

---

### Step 4: Mark as resolved

```bash id="8k3t1x"
git add <file>
```

---

### Step 5: Complete merge

```bash id="p6m2zd"
git commit
```

---

## 🔍 4. Check Conflict Status

```bash id="n7r5q1"
git status
```

---

## ❌ 5. Abort Merge

```bash id="d3k8xp"
git merge --abort
```

---

## 🧠 6. Why Conflicts Happen

```text id="t5m1zx"
Multiple changes → same location → ambiguity
```

---

## 🛠️ 7. Tools for Conflict Resolution

* VS Code merge editor
* Git GUI tools
* diff tools

---

## ⚠️ Common Mistakes

### ❌ Forgetting to remove markers

👉 Causes syntax errors

---

### ❌ Blindly accepting one side

👉 May lose important changes

---

### ❌ Not testing after merge

👉 Hidden bugs

---

## 🧠 Best Practices

* Pull frequently
* Keep branches small
* Communicate with team

---

## 🧠 Mental Model

```text id="v3p8yk"
Conflict = Git asking you to decide
```

---

## 📌 Next Step

Proceed to:

👉 `permission-errors.md`
