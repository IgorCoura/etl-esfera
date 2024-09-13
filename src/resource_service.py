from models.resource import Resource
from repositories.category_repository import CategoryRepository
from repositories.resource_repository import ResourceRepository
from repositories.source_repository import SourceRepository


class ResourceService:
    
    def __init__(self, category_repository: CategoryRepository, source_repositroy: SourceRepository, resource_repository: ResourceRepository):
        self.category_repository = category_repository
        self.source_repositroy = source_repositroy
        self.resource_repository = resource_repository

    def insert_all(self, resources):
        for resource in resources:
            self.insert(resource)
        self.resource_repository.commit()
        
    def insert(self, resource: Resource):
        source_id = self.source_repositroy.insert_if_not_exist(resource.source)
        category_id = self.category_repository.insert_all_hierarchy_if_not_exist(resource.category)
        self.resource_repository.insert(resource, category_id, source_id)
        
        