import json
import os
from colorama import init, Fore, Style

import control_nginx

init(autoreset=True)


def load_config():
    default_config = {{"nginx_directory": "D:/Toolbox/nginx"}}

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            print("配置加载成功。")
            return config
    except json.JSONDecodeError as e:
        print(f"读取JSON文件时出错：{e}")
        return default_config
    except FileNotFoundError as e:
        print(f"未找到配置文件：{e}")
        with open("config.json", "w") as f:
            json.dump(default_config, f, indent=4)
            print("已生成默认配置文件。")
        return default_config


def check_nginx_executable(nginx_directory):
    nginx_exe_path = os.path.join(nginx_directory, "nginx.exe")
    if os.path.isfile(nginx_exe_path):
        return True
    else:
        print(f"未找到nginx.exe在目录：{nginx_directory}")
        return False


def main():
    config = load_config()
    if not config:
        print("加载配置失败。")
        return

    nginx_directory = config["nginx_directory"]
    print(f"Nginx目录：{nginx_directory}")

    if not check_nginx_executable(nginx_directory):
        return

    while True:

        nginx_status = control_nginx.status()
        if "running" in nginx_status:
            status_colored = Fore.GREEN + nginx_status + Style.RESET_ALL
        else:
            status_colored = Fore.RED + nginx_status + Style.RESET_ALL

        os.system("cls")
        print("\nEasy Nginx on Windows")
        print(f"当前状态：{status_colored}")
        print("0. 刷新")
        print("1. 启动Nginx")
        print("2. 停止Nginx（快速）")
        print("3. 退出Nginx（标准）")
        print("4. 强制停止Nginx")
        print("5. 重新加载Nginx")
        print("6. 退出ENoW")
        choice = input("请输入你的选择：")

        if choice == "1":
            control_nginx.start(nginx_directory)
        elif choice == "2":
            control_nginx.stop(nginx_directory)
        elif choice == "3":
            control_nginx.quit(nginx_directory)
        elif choice == "4":
            control_nginx.taskkill()
        elif choice == "5":
            control_nginx.reload(nginx_directory)
        elif choice == "6":
            break
        else:
            pass


if __name__ == "__main__":
    main()
