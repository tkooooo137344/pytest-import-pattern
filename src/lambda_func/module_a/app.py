import os 
if "src" in os.getcwd():
    from usecase import func_module_a
else:
    from .usecase import func_module_a

def lambda_handler():
    print("called a")