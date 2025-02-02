import json
import zipfile
import io
import os


"тут короче по идее будет код обработчика проектов"

EMPTY_DATA_STRUCT = {}
EMPTY_STRINGS_STRUCT = {
    "name": "unnamed",
    "strings": {

    }
}
REQUIRED_FILES = {
    "data.json": EMPTY_DATA_STRUCT,
    "strings.json": EMPTY_STRINGS_STRUCT
}


class Project:
    def __init__(self):
        self.name:str = "unnamed"
        self.json_file_data:str
        self.strings_file_data:str
        self.json_data:dict
        self.strings_data:dict
        
    def new(self, name:str = "unnamed"):
        "returns project"
        a = Project()
        a.name = name
        a.json_file_data = json.dumps(EMPTY_DATA_STRUCT)
        a.json_data = json.loads(a.json_file_data)
        a.strings_file_data = json.dumps(EMPTY_STRINGS_STRUCT)
        a.strings_data = json.loads(a.strings_file_data)

        return a
    
    def save_file(self, file:zipfile.ZipFile):
        cur_dir = os.getcwd()
        os.chdir(cur_dir+"/.temp")

        with open(f"data.json", "w+") as ass:
            ass.write(json.dumps(self.json_data))

        file.write(f"data.json")
        os.remove(f"data.json")
        with open(f"strings.json", "w+") as ass:
            ass.write(json.dumps(self.strings_data))
            
        file.write(f"strings.json")
        os.remove(f"strings.json")

        os.chdir(cur_dir)

    def open(self, file:zipfile.ZipFile):
        def is_valid(filelist:list) -> list:
            "returns not found files"
            required = [i for i in REQUIRED_FILES]
            for file in filelist:
                if file.filename in required:
                    required.remove(file.filename)
            
            return required

        def secured(from_dict:dict, key, placeholder=""):
            return from_dict[key] if key in from_dict else placeholder

        validation = is_valid(file.filelist)
        if "strings.json" not in validation:
            self.strings_file_data = file.read(f"strings.json")
            self.strings_data = json.loads(self.strings_file_data)
        if "data.json" not in validation:
            self.json_file_data = file.read(f"data.json")
            self.json_data = json.loads(self.json_file_data)
        
        return self