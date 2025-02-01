import json
import zipfile
import io

"тут короче по идее будет код обработчика проектов"


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
        a.json_file_data = "{}"
        a.json_data = json.loads(a.json_file_data)
        a.strings_file_data = "{}"
        a.strings_data = json.loads(a.strings_file_data)

        return a
    
    def save_file(self, file:zipfile.ZipFile):
        with open(f".temp/{self.name}_data", "w+") as ass:
            ass.write(json.dumps(self.json_data))
        file.write(f".temp/{self.name}_data")

    def open(self, file:bytes):
        file = io.BytesIO(file)
        archive = zipfile.ZipFile(file, "r")
        print(archive.filelist())