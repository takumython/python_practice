print("Hello World!")

# pythonで扱うすべてのものを、"object"と言う

# 変数 => objectにつけるラベル
test = "Hello World!"

# データ型 => 全てのobjectには型がある
1 # int
1.0 # float
"Hello" # str
True, False # boolean
[0, 1, 2] # list: mutable
{"name": "komai", "age": "29", "gender": "man"} # dict: mutable
{1, 2, 3} # set: mutable
(1, 2, 3) # turple: immutable

def sample_func():
    print("Hello World!")
sample_func # function

class Sample:
    def __init__(self, name):
        self.name = name

    def sample_func(self):
        print(f"Hello World! {self.name}!")
Sample # class

# 四則演算
1 + 1
1 - 1
1 * 1
1 / 1

# 比較演算子, 論理演算子
2 > 1
1 < 2
2 >= 1
1 <= 2
1 == 1
1 != 2

# 関数
def say_hello(name):
    text = f"Hello World! {name}!"
    return text

# class
class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def say_myname(self):
        print(f"My name is {self.name}.\nI'm {self.gender}.")

# 組み込み関数
print("Hello World!")
str(1)
int("1")
len("test")
range(5)

# 標準ライブラリ
import datetime
today = datetime.datetime.today()
print(today)

# 外部ライブラリ
import termcolor
print(termcolor.colored("Hello World!", "red"))

# if
old = 19
if old >= 21:
    print("お酒OK!")
elif old == 20:
    print("お酒ギリOK!")
else:
    print("お酒OUT!")

# 繰り返し
name_list = ["komai", "sato", "kusumoto"]
for name in name_list:
    print(name)

for i in range(len(name_list)):
    print(name_list[i])

num = 0
while num < 5:
    num += 1
    print(num)