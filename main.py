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
    with zipfile.ZipFile("test.jmproj", "w") as f:
        a.save_file(f)


if __name__ == "__main__":
    main()