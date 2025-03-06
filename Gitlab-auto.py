import argparse
import requests
import os

# GitLab Personal Access Token (PAT)
GITLAB_TOKEN = "your_personal_access_token"  # Replace with your token
GITLAB_URL = "https://gitlab.com/api/v4"

def download_file(repo_name, file_path, branch="main"):
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    
    # Get project ID
    project_url = f"{GITLAB_URL}/projects"
    response = requests.get(project_url, headers=headers, params={"search": repo_name})
    
    if response.status_code != 200:
        print(f"Error fetching project: {response.text}")
        return
    
    projects = response.json()
    project = next((p for p in projects if p["name"] == repo_name), None)
    
    if not project:
        print(f"Repository '{repo_name}' not found.")
        return
    
    project_id = project["id"]
    
    # Get file content
    file_url = f"{GITLAB_URL}/projects/{project_id}/repository/files/{file_path.replace('/', '%2F')}/raw"
    params = {"ref": branch}
    response = requests.get(file_url, headers=headers, params=params)
    
    if response.status_code == 200:
        file_name = os.path.basename(file_path)
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Error downloading file: {response.text}")

# Command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download file from GitLab")
    parser.add_argument("-r", "--repo", required=True, help="GitLab repository name")
    parser.add_argument("-f", "--file", required=True, help="File path in repo")
    parser.add_argument("-b", "--branch", default="main", help="Branch name (default: main)")
    args = parser.parse_args()
    
    download_file(args.repo, args.file, args.branch)
