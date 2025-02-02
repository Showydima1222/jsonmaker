import zipfile

import ctypes
import locale

from app import strings



from core import env
from core.handler.project import Project

from app.project_list import ProjectWindow

# абек шёл нахуй)))0

def init_lang():
    LOCALES = {"ru_RU" : strings.RU}
    lang = locale.windows_locale[ ctypes.windll.kernel32.GetUserDefaultUILanguage() ]
    if lang in LOCALES:
        return LOCALES[lang]
    return strings.EN

def main():
    env.check_and_repair_env()
    strings = init_lang()
    a = ProjectWindow(strings)
    a.start()
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