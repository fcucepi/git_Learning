from hello import hello

import os
from datetime import datetime
import random

from datetime import datetime  #from dev分支的註解


if __name__ == "__main__":
    name = "Your Name" # 自行替換裡面的名字
    hello(name)

    
    now = datetime.now()


    now = datetime.now()  #加入時間顯示

    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n現在時間是 {time_str}")
    print("Random number:", random.randint(1, 100)) # 隨機產生 1 到 100 的整數並顯示出來
