import paybase
txt_name=input("チェックするリンクが入ったtxtファイルを指定してください。\n拡張子まで入力してください。"+"\n>>")
try:
  f=open(txt_name,"r")
  paylink=f.read().split('\n')
  f.close()
except:
  print("読み込めませんでした。")
  exit()
hozon=input("workedなリンクの保存先を入力してください。\n拡張子は入力しなくてよいです。\n>>")
for i in paylink:
  paybase
