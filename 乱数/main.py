import random
import time
import json
import sys

for i in range(5):print()

print("ーーーーーーーーーープログラム開始ーーーーーーーーーー")

random.seed(time.time())

with open("data.json") as f:
  data = json.load(f)

keys = list(data.keys())

print()

print("登録ならadd、リスト表示ならshow、除外ならremove、\nランダムピックアップならrandomと半角英数字で打ってください")

def show():
  for i in range(2):print()
  for i in keys:
    print(i)
    for j in data[i]:
      print(f"|---{j}")
    print(f"\n要素数 : {len(data[i])}\n")

def add():
  for i in range(2):print()
  count = 0
  dont_need_show = False
  loop = True

  print("キーを追加するならkey、値を追加するならvalue\nと半角英数字で打ってください")

  while loop:
    mode = input(">>")
    
    if mode == "key":
      pass
    
    elif mode == "value":
      pass
    
    else:
      if count < 10:
        print("指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で打ってください")
      elif count >= 10 and count < 20:
        print("わざとですか？\n指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で打ってください")
      elif count == 20:
        print("もうすねました\nさようなら")
        program_stop
      count +=1

def program_stop():
  print("ーーーーーーーーーープログラム終了ーーーーーーーーーー")
  sys.exit()