import os

root = "git-cheatsheet"

structure = {
    "00-overview": ["README.md"],
    "01-setup": ["install.md", "ssh-setup.md", "config.md"],
    "02-basics": ["init-clone.md", "add-commit.md", "status-log.md", "diff.md"],
    "03-branching": ["create-branch.md", "switch-checkout.md", "delete-branch.md", "merge.md"],
    "04-remote": ["push.md", "pull.md", "fetch.md", "upstream.md"],
    "05-advanced": ["rebase.md", "stash.md", "cherry-pick.md", "reset-revert.md"],
    "06-workflows": ["feature-branch.md", "gitflow.md", "hotfix.md"],
    "07-troubleshooting": ["merge-conflicts.md", "permission-errors.md", "detached-head.md", "undo-mistakes.md"],
    "08-templates": ["commit-message.md", "pr-template.md"]
}

os.makedirs(root, exist_ok=True)

for folder, files in structure.items():
    folder_path = os.path.join(root, folder)
    os.makedirs(folder_path, exist_ok=True)

    for file in files:
        open(os.path.join(folder_path, file), "w").close()

print("✅ Ordered skeleton created")