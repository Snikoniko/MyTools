import random
import time
import json
import sys

random.seed(time.time())

data,keys = {},[]

def program_stop():
  print("ーーーーーーーーーープログラム終了ーーーーーーーーーー")
  sys.exit()

def load_data():
  global data,keys
  with open("data.json",encoding="utf-8") as f:
    data = json.load(f)
    keys = list(data.keys())

def show():
  print("\n")
  for i in keys:
    print(i)
    for j in data[i]:
      print(f"|---{j}")
    print(f"\n要素数 : {len(data[i])}\n")

def add():
  print("\n")
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
          print("追加する値を入力してください。\n既存の値は入力しないでください")
          while True:
            input_value = input(">>")
            
            if not(input_value in data[which_key]):
              data[which_key].append(input_value)
              with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
              print("値を追加しました。")
              break
            elif dont_need_show:
              count += 1
              if count < 10:
                print("もうリストは表示してあるので\n既存の値は入力しないでください")
              elif count >= 10 and count < 20:
                print(f"わざとですか？\nもうリストは表示してあるので既存の値は入力しないでください{count}")
              elif count == 20:
                print("もうすねました。\nさようなら")
                program_stop()
            elif not dont_need_show and not input_value == "show":
              count += 1
              if count < 10:
                print("既存の値は入力しないでください\n既存の値がわからないならshowと\n半角英数字で入力してください")
              elif count >= 10 and count < 20:
                print(f"わざとですか？\n既存の値は入力しないでください{count}")
              elif count == 20:
                print("もうすねました。\nさようなら")
                program_stop()
            elif input_value == "show" and count > 0 and(not dont_need_show):
              show()
                
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

def remove_key_value():
  count = 0
  dont_need_show = False
  loop = True


  print("キーを削除するならkey、値を削除するならvalue\nと半角英数字で入力してください")

  while loop:
    mode = input(">>")
    
    if mode == "key":
      print("どのキーを削除しますか？")
      while True:
        input_key = input(">>")
        if input_key in data:
          del data[input_key]
          with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
          print("キーを削除しました。")
          loop = False
          break
        elif which_key == "show" and count > 0 and not(dont_need_show):
          show()
        elif not dont_need_show:
          count += 1
          if count < 10:
            print("存在しないキーを指定しないでください\n既存のキーがわからないならshowと\n半角英数字で入力してください")
          elif count >= 10 and count < 20:
            print(f"わざとですか？存在しないキーを指定しないでください{count}")
          elif count == 20:
            print("もうすねました\nさようなら。")
            program_stop
        elif dont_need_show:
          count += 1
          if count < 10:
            print("もうリストは表示してあるので\n存在しないキーを指定しないでください")
          elif count >= 10 and count < 20:
            print(f"わざとですか？\nもうリストは表示してあるので\n存在しないキーを指定しないでください{count}")
          elif count == 20:
            print("もうすねました\nさようなら。")
            program_stop
    
    elif mode == "value":
      print("どのキーの値を削除しますか？")
      while True:
        which_key = input(">>")
        
        
        if which_key in data:
          print("削除する値を入力してください")
          while True:
            input_value = input(">>")
            if input_value in data[which_key]:
              #data[which_key].pop(data[which_key].index([input_value]))
              # => これじゃエラーになるからリストから削除するならpopよりremoveを使う
              data[which_key].remove(input_value)
              with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
              print("値を削除しました。")
              break
            elif dont_need_show:
              count += 1
              if count < 10:
                print("もうリストは表示してあるので\n存在しない値を指定しないでください")
              elif count >= 10 and count < 20:
                print(f"わざとですか？\nもうリストは表示してあるので\n存在しない値を指定しないでください{count}")
              elif count == 20:
                print("もうすねました\nさようなら。")
                program_stop
            elif not dont_need_show and not input_value == "show":
              count += 1
              if count < 10:
                print("存在しない値を指定しないでください\n既存の値がわからないならshowと\n半角英数字で入力してください")
              elif count >= 10 and count < 20:
                print(f"わざとですか？存在しない値を指定しないでください{count}")
              elif count == 20:
                print("もうすねました\nさようなら。")
                program_stop
            elif input_value == "show" and count > 0 and not(dont_need_show):
              show()
          loop = False
          break
        elif which_key == "show" and count > 0 and not(dont_need_show):
          show()
        elif not dont_need_show:
          count += 1
          if count < 10:
            print("存在しないキーを指定しないでください\n既存のキーがわからないならshowと\n半角英数字で入力してください")
          elif count >= 10 and count < 20:
            print(f"わざとですか？存在しないキーを指定しないでください{count}")
          elif count == 20:
            print("もうすねました\nさようなら。")
            program_stop
        elif dont_need_show:
          count += 1
          if count < 10:
            print("もうリストは表示してあるので\n存在しないキーを指定しないでください")
          elif count >= 10 and count < 20:
            print(f"わざとですか？\nもうリストは表示してあるので\n存在しないキーを指定しないでください{count}")
          elif count == 20:
            print("もうすねました\nさようなら。")
            program_stop
          
    else:
      if count < 10:
        print("指定したとおりに\nキーを削除するならkey\n値を削除するならvalueと半角英数字で入力してください")
      elif count >= 10 and count < 20:
        print("わざとですか？\n指定したとおりに\nキーを削除するならkey\n値を削除するならvalueと半角英数字で入力してください({count}回目)")
      elif count == 20:
        print("もうすねました\nさようなら")
        program_stop()
      count +=1

def random_choice():
  print("comming soon...")

if __name__ == "__main__":
  for i in range(5):print()
  print("ーーーーーーーーーープログラム開始ーーーーーーーーーー")
  load_data()
  while True:
    print("\n登録ならadd、リスト表示ならshow、除外ならremove、\nランダムピックアップならrandom、終了するならexit\nと半角英数字で入力してください")
    overall_mode = input(">>")
    if overall_mode == "exit":
      program_stop()
    elif overall_mode == "add":
      add()
      load_data()
    elif overall_mode == "show":
      show()
    elif overall_mode == "remove":
      remove_key_value()
      load_data()
    elif overall_mode == "random":
      random_choice()
    print()