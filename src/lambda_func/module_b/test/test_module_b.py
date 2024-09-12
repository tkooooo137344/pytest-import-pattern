import sys
sys.path.append(".")
sys.path.append("src/lambda_func/module_b")
from src.lambda_func.module_b.usecase import func_module_b
from src.lambda_func.module_b.app import lambda_handler

def test_func_module_b():
    print("test_func_module_b called")