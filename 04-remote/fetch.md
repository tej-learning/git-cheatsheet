# Fetch Changes

This guide explains how to download updates from a remote repository without modifying your working code.

---

## 📥 1. Fetch from Remote

```bash id="b9h3q2"
git fetch
```

👉 Downloads latest changes from remote
👉 Does NOT merge them into your branch

---

## 🌐 2. Fetch Specific Remote

```bash id="m2r8vd"
git fetch origin
```

---

## 🔍 3. See Fetched Changes

After fetch:

```bash id="t5xq91"
git log origin/<branch-name>
```

Example:

```bash id="r6k2zp"
git log origin/main
```

---

## 🆚 4. Compare with Local Branch

```bash id="n8z4cy"
git diff main origin/main
```

👉 See what changed before merging

---

## 🔄 5. Update Local Branch (After Fetch)

```bash id="v1y7lp"
git merge origin/<branch-name>
```

or

```bash id="w3f8rm"
git rebase origin/<branch-name>
```

---

## 🧹 6. Clean Deleted Remote Branches

```bash id="c4t9hx"
git fetch -p
```

👉 Removes stale references

---

## 🧠 Fetch vs Pull

```text id="d7k2mc"
git fetch → download only (safe)
git pull  → download + merge (automatic)
```

---

## ⚠️ Common Issues

### ❌ Don’t see new changes

👉 You forgot to fetch:

```bash id="y2v6kp"
git fetch
```

---

### ❌ Confusion after fetch

👉 Remember:

* Your code has NOT changed yet
* Only remote tracking branches updated

---

## 🧠 Mental Model

```text id="f8p3lw"
Remote Repo ── fetch ──> Local (origin/main)
                      └─ your branch unchanged
```

---

## 📌 When to Use

* Before merging → inspect changes
* Before rebasing → avoid surprises
* In team environments → safer workflow

---

## 📌 Next Step

Proceed to:

👉 `upstream.md`
