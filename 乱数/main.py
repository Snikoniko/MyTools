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

  print("キーを追加するならkey、値を追加するならvalue\nと半角英数字で打ってください")

  while True:
    add_type = input(">>")
    if add_type == "key":

      pass

    elif add_type == "value":

      dont_need_show = False
      print("どのキーに追加しますか？")
      which_key = input(">>")

      while True:
        if which_key in data:
          print("追加するデータを入力してください")
          add_value = input(">>")
          data[which_key].append(add_value)
          print("ファイルに保存しています")
          with open("data.json","w") as f:
            json.dump(data, f, indent=2)

        else:
          if count == 10:
            print(f"わざとですか？\nちゃんと存在するキーを入力してください({count}回目)")

          elif count == 10 and count_second == 10:

            print("そうですかもうすねましたさようなら")
            program_stop()

          elif not(dont_need_show):
            print("存在するキーを入力してください\nどのキーが存在するかわからないならshowと\n半角英数字で入力してください\nわかるんだったら何も入力しないでエンターキーを押してください")
            need_show = input(">>")

            if need_show == "show":
              show()
              dont_need_show = True

          count += 1

    else:

      if count == 10 and count_second < 10:
        count_second += 1
        print(f"わざとですか？\nちゃんと指定した通り\nキーを追加するならkey、値を追加するならvalue\nと半角英数字で打ってください(警告{count_second}回目)")

      elif count == 10 and count_second == 10:
        print("そうですかもうすねましたさようなら")
        program_stop()

      else:
        count += 1
        print(f"ちゃんと指定した通り\nキーを追加するならkey、値を追加するならvalue\nと半角英数字で打ってください({count}回目)")

def program_stop():
  print("ーーーーーーーーーープログラム終了ーーーーーーーーーー")
  sys.exit()