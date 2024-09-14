class Result:
    def __init__(self, response, has_success, error_message) -> None:
        self.response = response
        self.is_success = has_success
        self.is_fail = has_success == False
        self.error_message = error_message
    
    
    def Sucess(response):
        return Result(response, True, "")
    
    def Fail(error_message):
        return Result(None, False, error_message)