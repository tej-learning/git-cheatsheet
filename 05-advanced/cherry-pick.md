# Cherry-pick

This guide explains how to apply a specific commit from one branch to another.

---

## 🍒 1. What is Cherry-pick?

Cherry-pick copies a specific commit and applies it to your current branch.

```text id="h4k2pz"
main    ───A────B────C
                   \
feature             D
```

Cherry-pick `C` into feature:

```text id="v7q3mn"
feature ───D────C'
```

👉 `C'` is a new commit (same changes, new hash)

---

## ⚡ 2. Cherry-pick a Commit

```bash id="p2r8jw"
git cherry-pick <commit-id>
```

---

## 🔍 3. Find Commit ID

```bash id="x5m1zy"
git log --oneline
```

---

## 🔁 4. Cherry-pick Multiple Commits

```bash id="y9d4kc"
git cherry-pick <commit1> <commit2>
```

Or range:

```bash id="n3q7lb"
git cherry-pick A^..B
```

---

## ⚠️ 5. Resolve Conflicts

If conflict occurs:

1. Fix files manually
2. Then:

```bash id="c6t2vx"
git add .
git cherry-pick --continue
```

---

## ❌ 6. Abort Cherry-pick

```bash id="u8f5qn"
git cherry-pick --abort
```

---

## 🧠 When to Use

* Apply bug fix to another branch
* Move specific feature without merging entire branch
* Backport changes

---

## ⚠️ Common Issues

### ❌ Duplicate changes

👉 Same commit applied twice → conflicts or duplication

---

### ❌ Wrong commit picked

Check:

```bash id="z2k6my"
git log --oneline
```

---

## 🧠 Mental Model

```text id="b5m7rx"
Cherry-pick = copy commit (not merge history)
```

👉 Only selected commit is applied
👉 No full branch integration

---

## 📌 Next Step

Proceed to:

👉 `reset-revert.md`
