# Pull Changes

This guide explains how to fetch and integrate changes from a remote repository.

---

## 📥 1. Pull from Remote

```bash
git pull
```

👉 Fetches + merges changes from remote into current branch

---

## 🔄 2. Pull Specific Branch

```bash
git pull origin <branch-name>
```

---

## 🧠 3. What Pull Actually Does

```text
git pull = git fetch + git merge
```

* `fetch` → downloads changes
* `merge` → integrates them

---

## ⚡ 4. Pull with Rebase (Recommended)

```bash
git pull --rebase
```

👉 Keeps history clean (no unnecessary merge commits)

---

## 🔍 5. Fetch Only (No Merge)

```bash
git fetch
```

👉 Downloads changes but does NOT apply them

---

## ⚠️ Common Issues

### ❌ Merge conflicts during pull

Fix:

1. Resolve conflicts manually
2. Then:

```bash
git add .
git commit
```

---

### ❌ Diverged branches

```text
Your branch and 'origin/main' have diverged
```

Fix:

```bash
git pull --rebase
```

---

### ❌ Uncommitted changes blocking pull

Fix:

```bash
git stash
git pull
git stash pop
```

---

## 🧠 Merge vs Rebase (Quick Insight)

| Merge                 | Rebase           |
| --------------------- | ---------------- |
| Keeps history as-is   | Rewrites history |
| Creates merge commits | Linear history   |

---

## 📌 Best Practices

* Use `git pull --rebase` for cleaner history
* Always commit or stash before pulling
* Pull frequently to avoid conflicts

---

## 🧠 Mental Model

```text
Remote Repo ── pull ──> Local Repo ──> Working Directory
```

---

## 📌 Next Step

Proceed to:

👉 `fetch.md`
