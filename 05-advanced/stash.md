# Stash

This guide explains how to temporarily save uncommitted changes.

---

## 📦 1. What is Stash?

Stash saves your working changes and cleans your working directory.

```text id="k3v9ht"
Working changes → stash → clean workspace
```

---

## ➕ 2. Save Changes to Stash

```bash id="x8w2kp"
git stash
```

👉 Saves:

* Modified files
* Staged changes

---

## 📝 3. Stash with Message

```bash id="q4t7dz"
git stash push -m "work in progress"
```

---

## 📋 4. View Stashes

```bash id="r1n8mc"
git stash list
```

Example:

```text id="z7f2qp"
stash@{0}: WIP on main
stash@{1}: feature changes
```

---

## 🔄 5. Apply Stash

```bash id="v6k3yt"
git stash apply
```

👉 Keeps stash after applying

---

## 📤 6. Apply and Remove Stash

```bash id="n5d9bw"
git stash pop
```

---

## 🗑️ 7. Delete Stash

```bash id="a3m8xj"
git stash drop stash@{0}
```

Clear all:

```bash id="t2p6qz"
git stash clear
```

---

## 📄 8. Stash Specific Files

```bash id="h8y4lc"
git stash push <file>
```

---

## ⚠️ Common Issues

### ❌ Stash not applying cleanly

👉 Conflict may occur → resolve manually

---

### ❌ Lost track of stash

Check:

```bash id="d4r9we"
git stash list
```

---

### ❌ Untracked files not stashed

Use:

```bash id="u7p2vx"
git stash -u
```

---

## 🧠 Mental Model

```text id="f9k3lp"
Stash = temporary hidden commit
```

👉 Stored outside your branch
👉 Can be reapplied later

---

## 📌 When to Use

* Switching branches quickly
* Pulling latest changes safely
* Experimenting without committing

---

## 📌 Next Step

Proceed to:

👉 `cherry-pick.md`
