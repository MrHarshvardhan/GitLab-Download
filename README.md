# **Automate File Download from Private GitLab Repositories**

## **Overview**
This Python script automates the process of downloading files from **private GitLab repositories** without requiring manual login every time. Instead, it uses a **Personal Access Token (PAT)** for authentication and downloads files automatically.

## **Features**
- ✅ **Automated File Download** – No need to log in manually.
- ✅ **Secure Authentication** – Uses a **Personal Access Token (PAT)** instead of storing passwords.
- ✅ **Easy to Use** – Just specify the **repository name and file path**, and it downloads the file for you.

---

## **Prerequisites**
Before running the script, make sure you have:

1. **Python Installed** (Python 3.x recommended) – [Download Python](https://www.python.org/downloads/)
2. **GitLab Personal Access Token (PAT)** – Required for authentication.

---

## **Setup Guide**

### **Step 1: Generate a GitLab Personal Access Token (PAT)**
1. Log in to **GitLab**.
2. Navigate to **Preferences > Access Tokens**.
3. Create a new token with the following scopes:
   - `read_repository`
   - `read_api`
4. Copy the generated **PAT** and save it securely.

---

### **Step 2: Install Required Python Packages**
The script uses the `requests` library to interact with the GitLab API. If you don’t have it installed, run:
```bash
pip install requests
```

---

### **Step 3: Clone This Repository**
To use this script, clone the repository:
```bash
git clone git@github.com:MrHarshvardhan/GitLab-Download.git
cd GitLab-Download
```

---

### **Step 4: Configure Your Personal Access Token**
Replace `your_personal_access_token` in the script with your **GitLab PAT**:
```python
GITLAB_TOKEN = "your_personal_access_token"  # Replace with your token
```

---

## **Usage**
Run the script using the following command:
```bash
python GitLab-Download.py -r "RepoName" -f "path/to/file.txt" -b "main"
```

### **Example:**
```bash
python GitLab-Download.py -r "MyPrivateRepo" -f "docs/readme.md" -b "develop"
```

🚀 **Happy Coding!** 🎯

