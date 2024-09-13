from models.category import Category
from repositories.repository import Repository


class CategoryRepository(Repository):
    def __init__(self, connection):
      super().__init__(connection)
      
    def insert_if_not_exist(self, category:Category):
        name = category.name
        parent_category_id = None
        if category.parent_category != None:
            parent_category_id = category.parent_category.id
            
        result = super().update(
         query="INSERT INTO categories (name, parent_category_id) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name RETURNING id;",
         params=(name, parent_category_id)
        ) 
        return result[0]
    
    

    def insert_all_hierarchy_if_not_exist(self, category:Category):
        if(category.parent_category == None):
            return self.insert_if_not_exist(category)
        category.parent_category.id = self.insert_all_hierarchy_if_not_exist(category.parent_category)
        return self.insert_if_not_exist(category)