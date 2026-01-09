# GitHub Setup Instructions

## After you've created your GitHub repository, follow these steps:

### 1. Extract the tar.gz file to your computer

### 2. Open Terminal/Command Prompt and navigate to the project:
```bash
cd path/to/pendant_map_project
```

### 3. Initialize Git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit: Medieval pendants map with Spurlock styling"
```

### 4. Connect to your GitHub repository:
```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual GitHub username and repository name.

### 5. Now open in PyCharm Pro:
- File → New → Project from Version Control
- Paste your GitHub URL: https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
- Choose where to save locally
- Click Clone

PyCharm will handle everything else!

## Alternative: Let PyCharm Handle the Git Push

1. Extract the tar.gz file
2. Open the folder in PyCharm (File → Open)
3. VCS → Enable Version Control Integration → Git
4. VCS → Share Project on GitHub
5. PyCharm will create the repo and push for you automatically!
