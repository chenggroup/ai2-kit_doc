import requests
import os

project_name = "ai2-kit"

# 获取PyPI上的最新版本
response = requests.get(f"https://pypi.org/pypi/{project_name}/json")
latest_version = response.json()["info"]["version"]

# 读取当前version.txt中的版本
with open("version.txt", "r") as f:
    current_version = f.read().strip()

# 如果版本不同，更新version.txt
if latest_version != current_version:
    with open("version.txt", "w") as f:
        f.write(latest_version)
    print(f"Version updated from {current_version} to {latest_version}")
    # 设置GitHub Actions输出变量
    print(f"::set-output name=version_changed::true")
    print(f"::set-output name=new_version::{latest_version}")
else:
    print("Version is up to date")
    print(f"::set-output name=version_changed::false")