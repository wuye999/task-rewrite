#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import time
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## 抢券，但不知道抢的哪个券
cycles=2  #循环2遍
ask_sleep=0.1  #请求间隔为0.1秒
cksum=3   #ck总数
ck1=''
ck2=''
ck3=''

urlnum=2   #api总数
url1='https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22vN4YuYXS1mPse7yeVPRq4TNvCMR%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key=F3A09C1A5D4635C9AA07C28F0E43FA7F69548EE87DDF7EB6D2DBFA2006AB8D9188592FDAE04311D2D7D6D0F574FF2649_babel,roleId=F9A3ADE8EBE3CB76B48C7A29EFE2B2BF_babel%22%7D&client=wh5'
url2='https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22vN4YuYXS1mPse7yeVPRq4TNvCMR%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key=FDACB5EC256BA64B342D79618485D043A354E81B75D634DE1992390C701E70D51DAE2AB811FD3406E484E1DBB1FBE3D0_babel,roleId=7014304DFB7211DD1ED99AF4D8360DCD_babel%22%7D&client=wh5'

ua='okhttp/3.12.1;jdmall;apple;version/9.4.0;build/88830;screen/1440x3007;os/11;network/wifi'

cks=[]
for n in range(1,cksum+1):
    a='ck'+str(n)
    a = eval(a)
    cks.append(a)

urls=[]
for n in range(1,urlnum+1):
    a='url'+str(n)
    a = eval(a)
    urls.append(a)

d=0
def ask_api(d):

    if d==cycles:
        print('\n结束')
        return
    print(f'\n\n ----- 第 {d+1} 次循环 ----- ') 
    b=0
    for url in urls:    
        b+=1
        c=0
        for ck in cks:
            c+=1
            headers = {
            'cookie': ck,
            'User-Agent': ua,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'charset': 'UTF-8',
            'accept-encoding': 'br,gzip,deflate'
            }
            print(f'\n----- 账号 {c} 请求 url {b} -----')
            res = requests.post(url=url, headers=headers, verify=False)
            print(res.text)
            time.sleep(ask_sleep)
    d+=1
    return ask_api(d)

if __name__=='__main__':
   ask_api(d) 
