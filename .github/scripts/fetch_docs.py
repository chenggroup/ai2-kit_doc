import os
import requests
from git import Repo

gitlab_token = os.environ['GITLAB_TOKEN']
gitlab_repo_url = os.environ['GITLAB_REPO_URL']

# 使用GitLab API获取最新的文档文件
headers = {'PRIVATE-TOKEN': gitlab_token}
response = requests.get(f"{gitlab_repo_url}/repository/tree", headers=headers, params={'path': 'docs'})
files = response.json()

# 下载每个文件
for file in files:
    file_path = file['path']
    file_content = requests.get(f"{gitlab_repo_url}/repository/files/{file_path}/raw", headers=headers).content
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(file_content)

print("Documentation files fetched successfully.")