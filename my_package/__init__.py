# my_package/__init__.py
import ctypes
import os

# Load the shared library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "libhello.so"))

# Define the function prototype
lib.say_hello.restype = ctypes.c_char_p

def get_hello_message():
    return lib.say_hello().decode("utf-8")
    
