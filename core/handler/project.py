import json

"тут короче по идее будет код обработчика проектов"


class Project:
    def __init__(self):
        self.name:str = "unnamed"
        self.json_file_data:str
        self.strings_file_data:str
        self.json_data:dict
        self.strings_data:dict
        
    def new(self, name:str) -> self:
        "returns project"
        a = Project()
        a.name = name
        a.json_file_data = "{}"
        a.json_data = json.loads(a.json_file_data)
        a.strings_file_data = "{}"
        a.strings_data = json.loads(a.strings_file_data)

        return a

    def open(self, file:bytes) -> self:
        ...
    