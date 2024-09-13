from models.result import Result
import re

class Category:
    def __init__(self, id, name, parent_category) -> None:
        self.id = id
        self.name = name
        self.parent_category = parent_category
        
    def create_from_csv_item(item):
        match = re.match(r"(\d+) - (.+)", item)
        if match == False:
            return Result.Fail(f"Error ao tentar criar Category de: {item}")
        categories = match.group(2).split("-")
        category = Category.create_category(categories, 0, None)
        return Result.Sucess(category)
            
    def create_category(categories_array, index, category):
        name_category = categories_array[index].strip()
        category = Category(None, name_category, category)
        len_array = len(categories_array)
        if(index >= len_array - 1): 
            return category
        return Category.create_category(categories_array, index+1, category)