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
  count_second = 0
  dont_need_show = False
  loop = True

  print("キーを追加するならkey、値を追加するならvalue\nと半角英数字で打ってください")

def program_stop():
  print("ーーーーーーーーーープログラム終了ーーーーーーーーーー")
  sys.exit()