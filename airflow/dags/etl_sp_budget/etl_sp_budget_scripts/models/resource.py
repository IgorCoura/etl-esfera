import json
import re
import logging

from etl_sp_budget.etl_sp_budget_scripts.models.result import Result
from etl_sp_budget.etl_sp_budget_scripts.util.value_converter import ValueConverter
from etl_sp_budget.etl_sp_budget_scripts.models.category import Category
from etl_sp_budget.etl_sp_budget_scripts.models.source import Source


class Resource:
    def __init__(self, id, name, amount, currency_code, source, category):
        self.id = id
        self.name = name
        self.amount = amount
        self.currency_code = currency_code
        self.source = source
        self.category = category
        
    def create_from_csv_item_coin_brl(item_resource, item_amount, source, category, is_expenses):
        
        result_amount = ValueConverter.convert_to_float(item_amount)
        
        if(result_amount.is_fail):
            return Result.Fail(f"Error ao tentar converte o valor {item_amount}")  
        
        match = re.match(r"(\d+) - (.+)", item_resource)
        if match == False:
            return Result.Fail(f"Error ao tentar criar resoucer de: {item_resource}")
        

        name = match.group(2).strip()
        amount = result_amount.response
        if(is_expenses):
            amount = -amount
 
        return Result.Sucess(Resource(None, name, amount, "BRL", source, category))
            
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "currency_code": self.currency_code,
            "source": self.source.to_dict() if self.source else None,
            "category": self.category.to_dict() if self.category else None
        }

    def from_dict(data):
        source = Source.from_dict(data["source"]) if data["source"] else None
        category = Category.from_dict(data["category"]) if data["category"] else None
        return Resource(
            data["id"], 
            data["name"], 
            data["amount"], 
            data["currency_code"], 
            source, 
            category
        )
    
    def to_json(self):
        logging.info(f"dic to json: {self.to_dict()}")
        return json.dumps(self.to_dict())
    
    def from_json(json_str):
        data = json.loads(json_str)
        return Resource.from_dict(data)
