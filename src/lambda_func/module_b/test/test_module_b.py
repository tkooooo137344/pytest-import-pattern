import sys
import os
# import moduleモード呼び出しを想定, このモードで呼び出された場合はsys.pathに実行ファイルのパスが入っていないため、"src"が入っているかどうかでlambdaでの動作かpytest上での動作が変更可能
if "src" in os.getcwd():
    module_pth = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(module_pth) 
    from usecase import func_module_b
    from app import lambda_handler
# import moduleモード呼び出しを想定, このモードで呼び出された場合はsys.pathに実行ファイルのパスが入っていないため、"src"が入っているかどうかでlambdaでの動作かpytest上での動作が変更可能
else:
    sys.path.append(".")
    from src.lambda_func.module_b.usecase import func_module_b
    from src.lambda_func.module_b.app import lambda_handler
def test_func_module_b():
    print("test_func_module_b called")