import random
import time
import json
import sys

random.seed(time.time())

with open("data.json",encoding="utf-8") as f:
  data = json.load(f)

keys = list(data.keys())

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
      print("追加するキーを入力してください\nただし、既存のキーは指定しないでください")
      while True:
        input_key = input(">>")
        if input_key in data:
          count += 1
          if not(dont_need_show):
            if count < 10:
              print("既存のキーは指定しないでください\n何が既存のキーかわからないときは\nshowと半角英数字で書いてください")
            elif count >= 10 and count < 20:
              print(f"わざとですか?\n既存のキーは指定しないでください\n何が既存のキーかわからないときは\nshowと半角英数字で書いてください({count}回目)")
            elif count == 20:
              print("もうすねました\nさようなら")
              program_stop()
          else:
            if count < 10:
              print("もう既存のキーは表示しましたので\n既存のキー以外を指定してください")
            elif count >= 10 and count < 20:
              print(f"わざとですか?\nもう既存のキーは表示しましたので\n既存のキー以外を指定してください({count}回目)")
            elif count == 20:
              print("もうすねました\nさようなら")
              program_stop()
        elif input_key == "show" and not(dont_need_show) and count > 0:
          show()
          dont_need_show = True
        else:
          data[input_key] = []
          with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
          print("キーを追加しました。")
          loop = False
          break
    
    elif mode == "value":
      print("どのキーに値を追加するか入力してください。")
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
        elif which_key == "show" and not(dont_need_show) and count > 0:
          show()
          print("どのキーに値を追加するか入力してください。")
          dont_need_show = True
        else:
          count += 1
          if which_key == "show" and dont_need_show:
            print("もうリストは見せましたので\nどのキーに値を追加するか入力してください。")
            
          elif count < 10 and not(dont_need_show):
            print("指定したとおりに\nどのキーに値を追加するか入力してください。\nどのキーが存在するかわからないならshowと\n半角英数字で入力してください。")
            
          elif count < 10 and dont_need_show:
            print("もうリストは見せましたので\n指定したとおりに\nどのキーに値を追加するか入力してください。")
            
          elif count >= 10 and count < 20 and not(dont_need_show):
            print("存在するキーが本当にわからないのでしたら\nshowと半角英数字で入力してください\nわかる場合はちゃんと存在するキーを指定してください({count}回目)")
            
          elif count >= 10 and count < 20 and dont_need_show:
            print("わざとですか？\nもうリストは見せましたので\nちゃんと存在するキーを指定してください({count}回目)")
            
          elif count == 20:
            print("もうすねました\nさようなら")
            program_stop()
    
    else:
      if count < 10:
        print("指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で入力してください")
      elif count >= 10 and count < 20:
        print("わざとですか？\n指定したとおりに\nキーを追加するならkey\n値を追加するならvalueと半角英数字で入力してください({count}回目)")
      elif count == 20:
        print("もうすねました\nさようなら")
        program_stop()
      count +=1

def remove():
  print("comming soon...")

def random_choice():
  print("comming soon...")

if __name__ == "__main__":
  for i in range(5):print()
  print("ーーーーーーーーーープログラム開始ーーーーーーーーーー")
  print()
  while True:
    print("登録ならadd、リスト表示ならshow、除外ならremove、\nランダムピックアップならrandom、終了するならexit\nと半角英数字で入力してください")
    overall_mode = input(">>")
    if overall_mode == "exit":
      program_stop()
    elif overall_mode == "add":
      add()
    elif overall_mode == "show":
      show()
    elif overall_mode == "remove":
      remove()
    elif overall_mode == "random":
      random_choice()