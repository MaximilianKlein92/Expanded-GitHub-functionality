#!/usr/bin/env python3
import subprocess
import sys
import os

def run(cmd, check=True):
    result = subprocess.run(cmd, shell=True)
    if check and result.returncode != 0:
        sys.exit(result.returncode)

def has_changes():
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    return bool(result.stdout.strip())

def main():
    # Check if inside a Git repo
    if not os.path.exists(".git"):
        print("❌ Not a Git repository.")
        sys.exit(1)

    if not has_changes():
        print("✅ Nothing to commit, working tree clean.")
        sys.exit(0)

    commit_message = input("Enter commit message: ")

    run("git add -A")
    run(f'git commit -m "{commit_message}"')
    run("git push")

if __name__ == "__main__":
    main()

