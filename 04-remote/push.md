# Push Changes

This guide explains how to upload your commits to a remote repository.

---

## ⬆️ 1. Push to Remote

```bash
git push origin <branch-name>
```

👉 Sends your local commits to remote (GitLab)

---

## 🔗 2. First Push (Set Upstream)

```bash
git push -u origin <branch-name>
```

👉 Sets tracking so future pushes can use just:

```bash
git push
```

---

## 📌 3. Push Current Branch

```bash
git push
```

👉 Works only if upstream is already set

---

## 🌐 4. Check Remote

```bash
git remote -v
```

---

## 🔄 5. Push All Branches

```bash
git push --all
```

---

## ⚠️ Common Issues

### ❌ Permission denied (publickey)

👉 SSH not configured properly
Fix → check `ssh-setup.md`

---

### ❌ Failed to push (non-fast-forward)

```text
! [rejected] -> main (fetch first)
```

👉 Remote has new commits

Fix:

```bash
git pull --rebase
git push
```

---

### ❌ Wrong remote URL

Fix:

```bash
git remote set-url origin <correct-url>
```

---

## ⚠️ Force Push (Dangerous)

```bash
git push --force
```

👉 Overwrites remote history

Safer option:

```bash
git push --force-with-lease
```

---

## 🧠 Mental Model

```text
Local Repository ── git push ──> Remote Repository
```

👉 Only committed changes are pushed

---

## 📌 Best Practices

* Always pull before push
* Avoid force push on shared branches
* Use feature branches

---

## 📌 Next Step

Proceed to:

👉 `pull.md`
