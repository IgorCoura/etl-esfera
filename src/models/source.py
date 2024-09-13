import re

from models.result import Result
from util.value_converter import ValueConverter

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