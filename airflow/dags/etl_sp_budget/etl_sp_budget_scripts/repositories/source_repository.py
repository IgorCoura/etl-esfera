from etl_sp_budget.etl_sp_budget_scripts.models.source import Source
from etl_sp_budget.etl_sp_budget_scripts.repositories.repository import Repository


class SourceRepository(Repository):
    def __init__(self, connection):
      super().__init__(connection)
      
    def insert_if_not_exist(self, source:Source):
        result = super().update(
         query="INSERT INTO sources (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name RETURNING id;",
         params=(source.name,)
        ) 
        return result[0]