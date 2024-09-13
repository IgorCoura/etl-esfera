import re

from models.result import Result
from util.value_converter import ValueConverter


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
        
        result_id = ValueConverter.convert_to_integer(match.group(1))
        if(result_id.is_fail):
            return result_id
        
        name = match.group(2).strip()
        amount = result_amount.response
        if(is_expenses):
            amount = -amount
 
        return Result.Sucess(Resource(id, name, amount, "BRL", source, category))
            
        
