import csv
import os

from models.category import Category
from models.resource import Resource
from models.source import Source

class ExtractData:
    
    def __init__(self, relative_path, has_header) -> None:
        self.data = []
        self.errors = []
        self.get_data_from_csv(relative_path, has_header)

    def extract_resource(self, is_expenses):
        line_number = 0
        result = []
        for row in self.data:
            line_number += 1
            
            # Get Source Data
            source_result = Source.create_from_csv_item(row[0])
            if(source_result.is_fail):
                self.add_error(line_number, row[0], source_result.error_message)
                continue
            source = source_result.response
            
            # Get Resource Categories Data
            category_result = Category.create_from_csv_item(row[1])
            if(category_result.is_fail):
                self.add_error(line_number, row[1], category_result.error_message)
                continue
            categories = category_result.response
            
            # Get Resources Data
            resource_result = Resource.create_from_csv_item_coin_brl(row[1], row[2], source, categories, is_expenses)
            if(resource_result.is_fail):
                self.add_error(line_number, row[1], resource_result.error_message)
                continue
            result.append(resource_result.response)
        return result
            

    def get_data_from_csv(self, relative_path, has_header):
        workdir = os.getcwd()
        file_path = workdir + relative_path
        with open( file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            if has_header:
                next(csv_reader)
            for row in csv_reader:
                self.data.append(row)
                
    def add_error(self, line, name, error):
        self.errors.append(f"Line: {line} - Source: {name} - Erro: {error}")