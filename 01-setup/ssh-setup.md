# SSH Setup for Git

This guide helps you configure SSH so you can securely connect to GitLab/GitHub without entering passwords.

---

## ✅ 1. Check Existing SSH Keys

```bash
ls -al ~/.ssh
```

Look for files like:

* id_rsa / id_rsa.pub
* id_ed25519 / id_ed25519.pub

---

## 🔑 2. Generate New SSH Key

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Press Enter for:

* File location (default is fine)
* Passphrase (optional)

---

## ▶️ 3. Start SSH Agent

```bash
eval "$(ssh-agent -s)"
```

---

## ➕ 4. Add Key to SSH Agent

```bash
ssh-add ~/.ssh/id_ed25519
```

---

## 📋 5. Copy Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output.

---

## 🌐 6. Add SSH Key to GitLab

1. Go to GitLab → Profile Settings
2. Open **SSH Keys**
3. Paste the key
4. Click **Add key**

---

## 🧪 7. Test Connection

```bash
ssh -T git@gitlab.com
```

Expected output:

```bash
Welcome to GitLab, @your-username!
```

---

## 🔄 8. Use SSH Instead of HTTPS

Check remote:

```bash
git remote -v
```

If HTTPS:

```bash
git remote set-url origin git@gitlab.com:username/repo.git
```

---

## ⚠️ Common Issues

### ❌ Permission denied (publickey)

Fix:

```bash
ssh-add ~/.ssh/id_ed25519
```

---

### ❌ SSH key in wrong location (like your H drive issue)

Check where Git is looking:

```bash
ssh -vT git@gitlab.com
```

👉 If path is wrong, create config:

```bash
nano ~/.ssh/config
```

Add:

```bash
Host gitlab.com
  HostName gitlab.com
  User git
  IdentityFile C:/Users/YourUser/.ssh/id_ed25519
```

---

### ❌ Multiple SSH keys

Use config file:

```bash
Host gitlab-work
  HostName gitlab.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

---

## 📌 Next Step

Proceed to:

👉 `02-basics/init-clone.md`
