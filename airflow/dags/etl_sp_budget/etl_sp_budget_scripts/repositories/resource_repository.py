from etl_sp_budget.etl_sp_budget_scripts.models.resource import Resource
from etl_sp_budget.etl_sp_budget_scripts.repositories.repository import Repository


class ResourceRepository(Repository):
    def __init__(self, connection):
      super().__init__(connection)
      
    def insert(self, resource: Resource, category_id, source_id):
        result = super().update(
         query="INSERT INTO resources (name, amount, currency_code, category_id, source_id) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
         params=(resource.name, resource.amount, resource.currency_code, category_id, source_id)
        ) 
        return result