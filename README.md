# Git Upload Helper

A small tool to speed up Git workflows.  
With **`git upload`**, you can automatically add, commit, and push all changes – without typing each command individually.

---

## 🔧 Installation (Windows)

### 1. Create a scripts folder  
For example:


#### C:\Users<YourName>\scripts


### 2. Add the following files to the folder (find them in the reposetory)
- `git-upload.py` (Python script)  
- `git-upload.bat` (Batch file for Windows)

### 3. Add the folder to your PATH  
- Open: *Control Panel → System → Advanced System Settings → Environment Variables*
- Under **User Variables → Path → Edit → New**, add your path

### 4. Set up a Git alias  
So you can use `git upload` instead of `git-upload`:
type into the terminal:

### *git config --global alias.upload "!C:/Users/<YourName>/scripts/git-upload.bat"*

# Usage
Navigate to a Git repository and run:

git upload

What it does:
Checks if you are in a Git repository.

Prompts you for a commit message.

Automatically runs:

- git add -A
- git commit -m " your message "
- git push


✅ Why use it?
Because typing:

git add . && git commit -m "..." && git push

every time is too much work.

Now you just need one command:

# git upload
