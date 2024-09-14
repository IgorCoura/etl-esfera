import re
import json

from etl_sp_budget.etl_sp_budget_scripts.models.result import Result
from etl_sp_budget.etl_sp_budget_scripts.util.value_converter import ValueConverter

class Source:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def create_from_csv_item(source_item):
        match = re.match(r"(\d+) - (.+)", source_item)
        if match:
            name = match.group(2).strip()
            return Result.Sucess(Source(None, name))
        else:
            return Result.Fail(f"Error ao tentar criar Source de: {source_item}")
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def from_dict(data):
        return Source(data["id"], data["name"])
    
    def to_json(self):
        return json.dumps(self.to_dict())

    def from_json(json_str):
        data = json.loads(json_str)
        return Source.from_dict(data)