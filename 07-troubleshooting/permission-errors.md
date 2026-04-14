# Permission Errors

This guide helps diagnose and fix common Git permission and authentication issues.

---

## ⚠️ 1. Common Errors

### ❌ Permission denied (publickey)

```text id="r7m2kp"
Permission denied (publickey)
```

👉 SSH key issue

---

### ❌ Could not read from remote repository

```text id="k3p9zx"
fatal: Could not read from remote repository
```

👉 Access or SSH problem

---

### ❌ Authentication failed (HTTPS)

```text id="v2n8qy"
fatal: Authentication failed
```

👉 Credentials issue

---

## 🔍 2. Check Remote URL

```bash id="b4y6zt"
git remote -v
```

👉 Ensure you are using SSH:

```text id="q9x2mv"
git@gitlab.com:username/repo.git
```

---

## 🔑 3. Verify SSH Key Exists

```bash id="m7z4cp"
ls ~/.ssh
```

Look for:

```text id="d5p8wr"
id_ed25519
id_ed25519.pub
```

---

## ▶️ 4. Add Key to SSH Agent

```bash id="n6t3qx"
ssh-add ~/.ssh/id_ed25519
```

---

## 🧪 5. Test SSH Connection

```bash id="z8k1hp"
ssh -T git@gitlab.com
```

Expected:

```text id="x4p7sd"
Welcome to GitLab
```

---

## ⚠️ 6. Wrong SSH Path (Your Issue)

If Git is using wrong drive (e.g., H: instead of C:)

Check:

```bash id="w1q9rc"
ssh -vT git@gitlab.com
```

---

### ✔️ Fix using config

```bash id="y3n6kf"
nano ~/.ssh/config
```

Add:

```text id="t8k2zp"
Host gitlab.com
  HostName gitlab.com
  User git
  IdentityFile C:/Users/YourUser/.ssh/id_ed25519
```

---

## 🔄 7. Fix HTTPS Credential Issues

```bash id="f6r2qw"
git config --global credential.helper cache
```

Or switch to SSH (recommended)

---

## 🧠 8. Multiple Accounts Issue

Use SSH config:

```text id="p9m4xz"
Host gitlab-work
  HostName gitlab.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

---

## ⚠️ Common Mistakes

* SSH key not added to GitLab
* Wrong remote URL
* SSH agent not running
* Using HTTPS unknowingly

---

## 🧠 Mental Model

```text id="g5x8mv"
Local machine → SSH key → GitLab authentication
```

---

## 📌 Debug Checklist

1. `git remote -v`
2. `ls ~/.ssh`
3. `ssh-add`
4. `ssh -T git@gitlab.com`

---

## 📌 Next Step

Proceed to:

👉 `detached-head.md`
