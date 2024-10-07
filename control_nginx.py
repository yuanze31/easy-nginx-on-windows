import os
import subprocess
import time


def status():
    result = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq nginx.exe"], capture_output=True, text=True
    )
    if "nginx.exe" in result.stdout:
        return "running"
    else:
        return "stopped"


# 1
def start(nginx_directory):
    os.chdir(nginx_directory)
    subprocess.Popen(["nginx"], capture_output=True, text=True)


# 2
def stop(nginx_directory):
    os.chdir(nginx_directory)
    if status() == "running":
        subprocess.run(["nginx", "-s", "stop"], capture_output=True, text=True)
        time.sleep(0.5)


# 3
def quit(nginx_directory):
    os.chdir(nginx_directory)
    if status() == "running":
        subprocess.run(["nginx", "-s", "quit"], capture_output=True, text=True)
        time.sleep(0.5)


# 4
def taskkill():
    if status() == "running":
        subprocess.run(
            ["taskkill", "/F", "/IM", "nginx.exe"], capture_output=True, text=True
        )


# 5
def reload(nginx_directory):
    os.chdir(nginx_directory)
    if status() == "running":
        subprocess.run(["nginx", "-s", "reload"], capture_output=True, text=True)
