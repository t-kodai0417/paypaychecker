import requests,os,json,uuid

def check(code,filea):
    code=code.replace("https://pay.paypay.ne.jp/","")
    client_uuid=str(uuid.uuid4())
    #リンクの情報を取得
    getp2pinfo={
        "Accept":"application/json, text/plain, */*",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }
    aaaaaa=requests.get(f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo?verificationCode={code}&client_uuid={client_uuid}",headers=getp2pinfo)
    dataf=aaaaaa.json()
    try:
        if dataf["payload"]["orderStatus"]=="PENDING":
            print(f"[+]https://pay.paypay.ne.jp/{code}")
            try:
                f = open(f"{filea}.txt", 'r', encoding='utf-8')
                aaa=f.read()
                f.close()
            except:
                aaa=""
            f = open(f"{filea}.txt", 'a', encoding='utf-8')
            if aaa=="":
                f.write(f"https://pay.paypay.ne.jp/{code}")
            else:
                f.write('\n'+f"https://pay.paypay.ne.jp/{code}")
            f.close()
            return(f"success")
        else:
            print(f"[-]https://pay.paypay.ne.jp/{code}  NoPending")
            return("died")
    except:
        print(f"[-]https://pay.paypay.ne.jp/{code}  NotExist")
        return("died")
    #値段 dataf["payload"]["pendingP2PInfo"]["amount"]
    #orderStatus dataf["payload"]["orderStatus"] PENDING
    
#check_price("https://pay.paypay.ne.jp/aC4jMnNa","test")
