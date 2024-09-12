import sys
sys.path.append(".")
sys.path.append("src/lambda_func/module_a")
from src.lambda_func.module_a.usecase import func_module_a
from src.lambda_func.module_a.app import lambda_handler

def test_func_module_a():
    print("test_func_module_a called")