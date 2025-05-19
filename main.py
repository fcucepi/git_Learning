from hello import hello
from datetime import datetime

if __name__ == "__main__":
    name = "Your Name" # 自行替換裡面的名字
    hello(name)

    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n現在時間是 {time_str}")