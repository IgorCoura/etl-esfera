import logging
import io
import csv

from etl_sp_budget.etl_sp_budget_scripts.models.category import Category
from etl_sp_budget.etl_sp_budget_scripts.models.resource import Resource
from etl_sp_budget.etl_sp_budget_scripts.models.source import Source

class TransformData:
    def transform_resources(data, is_expenses, has_header):
        
        logging.info("Transform Init")
        csv_string_io = io.StringIO(data)
        reader = csv.reader(csv_string_io)
        line_number = 0
        result = []
        if has_header:
                next(reader)
        for row in reader:
            line_number += 1

            # Get Source Data
            source_result = Source.create_from_csv_item(row[0])
            if(source_result.is_fail):
                TransformData.warning(line_number, row[0], source_result.error_message)
                continue
            source = source_result.response
            
            # Get Resource Categories Data
            category_result = Category.create_from_csv_item(row[1])
            if(category_result.is_fail):
                TransformData.warning(line_number, row[1], category_result.error_message)
                continue
            categories = category_result.response
            
            # Get Resources Data
            resource_result = Resource.create_from_csv_item_coin_brl(row[1], row[2], source, categories, is_expenses)
            if(resource_result.is_fail):
                TransformData.warning(line_number, row[1], resource_result.error_message)
                continue
            
            resource_json  = resource_result.response.to_json()
            result.append(resource_json)
        logging.info("Transform Finished")    
        return result
    
    def warning(line, name, error):
        logging.warning(f"Line: {line} - Source: {name} - Erro: {error}")