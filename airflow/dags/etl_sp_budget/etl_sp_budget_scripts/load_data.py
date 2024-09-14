from etl_sp_budget.etl_sp_budget_scripts.models.resource import Resource
from etl_sp_budget.etl_sp_budget_scripts.repositories.category_repository import CategoryRepository
from etl_sp_budget.etl_sp_budget_scripts.repositories.resource_repository import ResourceRepository
from etl_sp_budget.etl_sp_budget_scripts.repositories.source_repository import SourceRepository


class LoadData:
    
    def __init__(self, connection):
        self.category_repository = CategoryRepository(connection)
        self.source_repositroy = SourceRepository(connection)
        self.resource_repository  = ResourceRepository(connection)

    def load_all_resources(self, resources_json):
        for resource_json in resources_json:
            self.load_resources(resource_json)
        self.resource_repository.commit()
        
    def load_resources(self, resource_json):
        resource = Resource.from_json(resource_json)
        source_id = self.source_repositroy.insert_if_not_exist(resource.source)
        category_id = self.category_repository.insert_all_hierarchy_if_not_exist(resource.category)
        self.resource_repository.insert(resource, category_id, source_id)
        
        