import random
import time
import json
import sys

for i in range(5):print()

print("ーーーーーーーーーープログラム開始ーーーーーーーーーー")

random.seed(time.time())

with open("data.json",encoding="utf-8") as f:
  data = json.load(f)

keys = list(data.keys())

print()

print("登録ならadd、リスト表示ならshow、除外ならremove、\nランダムピックアップならrandomと半角英数字で入力してください")

def program_stop():
  print("ーーーーーーーーーープログラム終了ーーーーーーーーーー")
  sys.exit()

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

  print("キーを追加するならkey、値を追加するならvalue\nと半角英数字で入力してください")

  while loop:
    mode = input(">>")
    
    if mode == "key":
      pass
    
    elif mode == "value":
      print("どのキーに値を追加するか入力してください。\nどのキーが存在するかわからないならshowと\n半角英数字で入力してください")
      while True:
        which_key = input(">>")
        if which_key in data:
          print("追加する値を入力してください")
          input_value = input(">>")
          data[which_key].append(input_value)
          with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
          print("値を追加しました。")
          loop = False
          break
        elif which_key == "show" and not(dont_need_show):
          show()
          print("どのキーに値を追加するか入力してください。")
          dont_need_show = True
        elif which_key == "show" and dont_need_show:
          print("もうリストは見せましたので\nどのキーに値を追加するか入力してください。")
          count += 1
        elif count < 10 and not(dont_need_show):
          print("指定したとおりに\nどのキーに値を追加するか入力してください。\nどのキーが存在するかわからないならshowと\n半角英数字で入力してください。")
          count += 1
        elif count < 10 and dont_need_show:
          print("もうリストは見せましたので\n指定したとおりに\nどのキーに値を追加するか入力してください。")
          count += 1
        elif count >= 10 and count < 20 and not(dont_need_show):
          print("存在するキーが本当にわからないのでしたら\nshowと半角英数字で入力してください\nわかる場合はちゃんと存在するキーを指定してください")
          count += 1
        elif count >= 10 and count < 20 and dont_need_show:
          print("わざとですか？\nもうリストは見せましたので\nちゃんと存在するキーを指定してください")
          count += 1
        elif count == 20:
          print("もうすねました\nさようなら")
          program_stop()
    
    else:
      if count < 10:
        print("指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で入力してください")
      elif count >= 10 and count < 20:
        print("わざとですか？\n指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で入力してください")
      elif count == 20:
        print("もうすねました\nさようなら")
        program_stop()
      count +=1
      
show()
add()