import os 
if "src" in os.getcwd():
    from usecase import func_module_b
else:
    from .usecase import func_module_b

def lambda_handler():
    print("called b")