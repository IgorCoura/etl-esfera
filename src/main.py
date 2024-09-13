

from extract_data import ExtractData
from models.category import Category
from models.resource import Resource
from models.source import Source
from repositories.category_repository import CategoryRepository
from repositories.db_pool_connection import DatabaseConnection
from repositories.resource_repository import ResourceRepository
from repositories.source_repository import SourceRepository
from resource_service import ResourceService

print("Inicio")

relative_path_expenses = '/data/gdvDespesasExcel.csv'
relative_path_recipes = '/data/gdvReceitasExcel.csv'


extractorExpenses = ExtractData(relative_path=relative_path_expenses, has_header=True)
expenses = extractorExpenses.extract_resource(is_expenses= True)

extractorRecipes = ExtractData(relative_path=relative_path_recipes, has_header=True)
recipes = extractorRecipes.extract_resource(is_expenses= False)

connection_string = "postgres://admin:5up3rS3nha@localhost:8080/RESOURCE_DB"
connection_pool = DatabaseConnection(connection_string, 1, 5)
connection = connection_pool.get_connection()

category_repository = CategoryRepository(connection)
source_repositroy = SourceRepository(connection)
resource_repository = ResourceRepository(connection)

resource_service = ResourceService(category_repository, source_repositroy, resource_repository)

resource_service.insert_all(expenses)
resource_service.insert_all(recipes)

resource_repository.commit()

print("Fim")