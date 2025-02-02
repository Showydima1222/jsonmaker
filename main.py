import zipfile

from core import env
from core.handler.project import Project

# абек шёл нахуй)))0

def main():
    env.check_and_repair_env()
    test()

def test():
    a:Project = Project().new()
    a.json_data = {"test":"ass"}
    with zipfile.ZipFile("./projects/test.jmproj", "w") as f:
        a.save_file(f)
    with zipfile.ZipFile("./projects/test.jmproj", "r") as f:
        a.open(f)
    
    print(a.json_data, a.strings_data)


if __name__ == "__main__":
    main()