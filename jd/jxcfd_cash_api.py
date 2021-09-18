#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import time
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## 京喜财富岛抢红包
cycles=3  #循环3遍
ask_sleep=0.1  #请求间隔为0.1秒
cksum=1   #ck总数
ck1=''


ddwPaperMoney=188  ##需要兑换的金额

ua='jdpingou;android;4.11.0;9;8dfb03d2ae0d7d5e;network/wifi;model/Redmi Note 7;appBuild/17304;partner/pingou_update1;;session/47;aid/8dfb03d2ae0d7d5e;oaid/697e77ebe3fde164;pap/JA2019_3111789;brand/Xiaomi;eu/8346662603334623;fv/1656034673465356;Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36'

## 组合cookie
cks=[]
for n in range(1,cksum+1):
    a='ck'+str(n)
    a = eval(a)
    cks.append(a)

d=0
def ask_api(d):
    if d==cycles:
        print('\n结束')
        return
    print(f'\n\n ----- 第 {d+1} 次循环 ----- ')   
    c=0
    for ck in cks:
        c+=1
        ## 计算时间戳
        timestamp1=timestamps()
        timestamp2=timestamps()
        timestamp3=timestamps()
        ## 计算红包金额
        global ddwPaperMoney
        if isinstance(ddwPaperMoney,int):
            ddwPaperMoney=int(ddwPaperMoney*100)
        else:
            ddwPaperMoney=int(ddwPaperMoney*1000)
        ## 合成api链接
        url='https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7'+'&_cfd_t='+str(timestamp1)+'&dwType=3&dwLvl=12'+'&ddwPaperMoney='+str(ddwPaperMoney)+'&strPoolName=jxcfd2_exchange_hb_202108'+'&strPgtimestamp='+str(timestamp2)+'&_stk=_cfd_t%2CbizCode%2CddwPaperMoney%2CdwEnv%2CdwLvl%2CdwType%2Cptag%2Csource%2CstrPgUUNum%2CstrPgtimestamp%2CstrPhoneID%2CstrPoolName%2CstrZone&_ste=1&h5st=20210918080859860%3B5615124578207162%3B10032%3Btk01w993e1c4430nI8KbYO%2FiTXGdSJhi39Vn6euL%2FcNimZ3MvYUJfoPjZfwp348Pi8xcFXXf4bodbhvLTahfCTo8j%2BFp%3Be216790d9d49e43fc2db67dbc6a6202191e75bbde97156d12cb6a8cf11c11ead'+'&_='+str(timestamp3)+'&sceneval=2'
        headers = {
            'Host': 'm.jingxi.com',
            'sec-fetch-mode': 'no-cors',
            'user-agent': ua,
            'accept': '*/*',
            'x-requested-with': 'com.jd.pingou',
            'sec-fetch-site': 'same-site',
            'referer': 'https://st.jingxi.com/fortune_island/index2.html?ptag=7155.9.47&sceneval=2',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': ck,
        }
        print(f'\n----- 账号 {c} 开始-----')
        ## 处理请求
        res = requests.post(url=url, headers=headers, verify=False)
        print(res.text)
        ## 延迟
        time.sleep(ask_sleep)
    d+=1
    return ask_api(d)

## 通过把秒转换毫秒的方法获得13位的时间戳
def timestamps():
    timestamp = int(round(time.time() * 1000))
    time.sleep(0.02)
    return timestamp


if __name__=='__main__':
   ask_api(d) 


