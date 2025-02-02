import os

def check_env() -> dict:
    check_list = {
        "result": False,
        "directories": {
            ".temp": False,
            "projects": False
            },
        }

    files = os.listdir(".")
    for dir in check_list["directories"]:
        if dir in files:
            check_list["directories"][dir] = True
        else:
            check_list["result"] = False

    return check_list

def check_and_repair_env():
    check = check_env()
    if check["result"] == False:
        make_dirs(check)

def make_dirs(check_list:dict) -> bool:
    dirs = check_list["directories"]
    for dir in dirs:
        if dirs[dir] == False:
            os.mkdir(f"./{dir}")
        