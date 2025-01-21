import sys
import logging

def error_message_detail(error_message, error_detail):
    file_name, line_no, _ = error_detail
    error_message = f"Error occurred in Python script name [{file_name}] line number [{line_no}] error message [{error_message}]"
    return error_message


# Inside exception.py
class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message


    