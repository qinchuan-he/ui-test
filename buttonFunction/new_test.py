
import os
from common.comfunction import com_path
import time
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(com_path())

path = "D:\work\8python\Cyprex-ui\自动化验证文档\截图\零散\1568803424.0703933.png"
new_path = "\Cyprex-ui"+path.split("Cyprex-ui", 2)[1]
print(new_path)











