# Upstream (Tracking Branch)

This guide explains how local branches are linked to remote branches.

---

## 🔗 1. What is Upstream?

An upstream branch is the **remote branch your local branch is connected to**.

```text id="l2m8fd"
local branch  ─────►  remote branch
   main              origin/main
```

---

## ⚡ 2. Set Upstream (First Push)

```bash id="7p3nq1"
git push -u origin <branch-name>
```

👉 This links:

```text id="b9x4kt"
local <branch> → origin/<branch>
```

---

## 📌 3. After Upstream is Set

You can use:

```bash id="k1z8vr"
git push
git pull
```

👉 No need to specify branch or remote

---

## 🔍 4. Check Upstream

```bash id="w5r2dy"
git branch -vv
```

Example:

```text id="g3k9ps"
main   a1b2c3d [origin/main] commit message
```

---

## 🔄 5. Set Upstream Manually

```bash id="x8q4nt"
git branch --set-upstream-to=origin/<branch-name>
```

---

## ❌ 6. Remove Upstream

```bash id="p7d3mz"
git branch --unset-upstream
```

---

## ⚠️ Common Issues

### ❌ No upstream configured

```text id="n6r8wc"
fatal: no upstream branch
```

Fix:

```bash id="q2v9sl"
git push -u origin <branch-name>
```

---

### ❌ Wrong upstream branch

Fix:

```bash id="z4t1kp"
git branch --set-upstream-to=origin/<correct-branch>
```

---

## 🧠 Mental Model

```text id="c5m2vx"
Upstream = default destination/source for push & pull
```

👉 Stored in Git config
👉 Branch-to-branch relationship

---

## 📌 When It Matters

* First push of new branch
* Simplifying daily workflow
* Working with multiple remotes

---

## 📌 Next Step

Proceed to:

👉 `05-advanced/rebase.md`
