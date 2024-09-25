import sys
import logging

#This function is used to generate a detailed error message. 
# When an error occurs, the function collects information about: File name where the error occurred. 
# Line number where the error was generated. Error message (the error itself).

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

# This is a custom exception class. 
# When an error occurs in your program, you can use this class to throw and handle an error in more detail 
# (using the error_message_detail function that was defined earlier).    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


        