from etl_sp_budget.etl_sp_budget_scripts.models.result import Result


class ValueConverter:
    def convert_to_float(string):
        string = string.strip()
        string = string.replace('.', '').replace(',', '.')
        try:
            response = float(string)
            return Result.Sucess(response)
        except Exception:
            raise Exception(f"Não foi possivel converter a string {string} para float.")
        
    def convert_to_integer(string):
        string = string.strip()
        string = string.replace('.', '').replace(',', '.')
        try:
            response = int(string)
            return Result.Sucess(response)
        except Exception:
            raise Exception(f"Não foi possivel converter a string {string} para float.")