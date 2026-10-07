import os
import subprocess

print("WELCOME TO BAHRAM TOOLS")
print()
print("~$ app-bahram-net")
print("~$ K-tun tools")
print("~$ download tools from K-tun")
print()

folder = "/storage/emulated/0/bon/ri/tools/K-tun"
repo = "https://github.com/YOUR_USERNAME/K-tun.git"

os.makedirs("/storage/emulated/0/bon/ri/tools", exist_ok=True)

if not os.path.exists(folder):
    print("[+] Creating K-tun folder...")
    subprocess.run(["git", "clone", repo, folder], check=True)
else:
    print("[+] K-tun folder already exists.")
    subprocess.run(["git", "-C", folder, "pull"], check=True)

print()
print("Downloaded files:")
print(f".../bon/ri/tools/K-tun/index.html")