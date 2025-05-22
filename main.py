from hello import hello
import os
from datetime import datetime
import random

if __name__ == "__main__":
    name = "Your Name" # 自行替換裡面的名字
    hello(name)
    
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n現在時間是 {time_str}")
    print("Random number:", random.randint(1, 100)) # 隨機產生 1 到 100 的整數並顯示出來
