import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # this variable will store the info like on which file and line the error has occurred
    file_name = exc_tb.tb_frame.f_code.co_filename  # read the custom exception handling doc for this
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message
     

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# Wherever we use try and catch block along with custom exception, we will get the error details