import paybase
txt_name=input("チェックするリンクが入ったtxtファイルを指定してください。\n拡張子まで入力してください。"+"\n>>")
try:
  f=open(txt_name,"r")
  paylink=f.read().split('\n')
  f.close()
except:
  print("読み込めませんでした。")
  exit()
