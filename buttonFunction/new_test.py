
import os
from common.comfunction import com_path
import time
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(com_path())
create_path = com_path()+"截图\\"+str(time.time())
os.makedirs(create_path)
print(create_path)












