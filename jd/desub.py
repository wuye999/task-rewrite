#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#填写
# cookie数量
ckkk=18  ##cookie为18个
# 青龙 or v4
xitong="qinglong"



import os
import functools
import imp
import time
import requests
def import2(a):
    global zhulima
    zhulima = imp.load_source('foobar',a)

def xitongnum(xitong):
    if xitong=='qinglong':
        if os.path.exists('/ql/log/.ShareCode'):
            mulu='/ql/log/.ShareCode/'
        else:
            mulu='/ql/log/code/'
    else:
        mulu="/jd/log/jcode/"
    return mulu

def zlmmululistnum(mulu):
    if mulu=='/ql/log/.ShareCode/':
        mulu_list = os.listdir(mulu)
    else:
        mulu_list = os.listdir(mulu)
        mulu_list=sorted(mulu_list, reverse=True)
        mulu_list=[mulu_list[0]]
    if '__pycache__' in mulu_list:
        mulu_list.remove('__pycache__')
    return mulu_list

def alistnum(mulu_list,mulu):
    alist=[]
    for i in mulu_list:
        alist.append(mulu+i)
    return alist

def daorunum(alist):
    list(map(import2,alist))

def run1num():
    mulu=xitongnum(xitong)
    mulu_list=zlmmululistnum(mulu)
    alist=alistnum(mulu_list,mulu)
    daorunum(alist)

def strnum(c):
    try:
        c = eval('zhulima.'+c)
        return c
    except AttributeError:
        print(f'助力码 {c} 不存在\n')
        c='zhan_wei_fu'
        return c

def nnum(zlm_leixing):
    n=0
    while True:
        n=n+1
        yield n

def zinum(zlm_leixing,n):
    encode=zlm_leixing+str(n)
    return encode

def logit(enurlnums):
    @functools.wraps(enurlnums)
    def run2num(*args, **kwargs):
        a,b=0,0
        zlm_leixing_list,biaozhi=enurlnums(a,b)
        for key,value in zlm_leixing_list.items():
            print(f'########上报{biaozhi} {value} 的助力码########\n') 
            for n in nnum(key):
                if n==ckkk+1:
                    break
                encode=zinum(key,n)
                decode=strnum(encode)
                if decode=='zhan_wei_fu':
                    continue
                if decode=='' or decode==' ':
                    print(f'第 {n} 个助力码为空\n')
                    continue
                print(f'开始上报{decode}')
                r=enurlnums(decode,value)
                g=1
                def url_set_num(r,biaozhi):
                    res=qingqiunum(r)
                    state=deurlnum(res,biaozhi)
                    if state==1:
                        nonlocal g
                        if g==3:
                            return
                        g+=1
                        print(f'第 {g} 次尝试提交')
                        time.sleep(2)
                        return url_set_num(r,biaozhi)
                url_set_num(r,biaozhi)               
    return run2num

def qingqiunum(r):
    time.sleep(1)
    url = r
    res = requests.get(url)
    #res = json.loads(res.text)
    return res.text

def deurlnum(res,biaozhi):
    if biaozhi=='he1':
        if 'Type ERROR' in res:
            print('he1助力码【提交类型无效】\n')
            state=1
        elif '\"code\":300' in res:
            print('he1助力码【重复提交】\n')
            state=0
        elif '\"code\":200' in res:
            print('he1助力码【提交成功】\n')
            state=0
        else:
            print('he1【服务器连接错误】\n')
            state=1
    elif biaozhi=='helloworld':
        if '0' in res:
            print('helloworld【助力池无你的助力码，请在tg机器人处提交助力码后再激活】\n') 
            state=0
        elif '1' in res:
            print('helloworld上报正常【助力码已在助力池】\n')
            state=0
        else:
            print('helloworld【服务器连接错误】\n')
            state=1
    elif biaozhi=='PasserbyBot':
        if 'Cannot' in res:
            print('PasserbyBot【提交类型无效】\n')
            state=1
        elif '激活成功' in res:
            print('PasserbyBot【激活成功】\n')
            state=0
        elif '激活失败' in res:
            print('PasserbyBot【助力池无你的助力码，请在tg机器人处提交助力码后再激活】\n')
            state=0
        else:
            print('PasserbyBot【服务器连接错误】\n')
            state=1
    return state

@logit
def enurlnum1(decode,value):
    biaozhi='he1'
    zlm_leixing_list={'MyFruit':'farm','MyBean':'bean','MyPet':'pet','MyDreamFactory':'jxfactory','MyJdFactory':'ddfactory','MySgmh':'sgmh','MyHealth':'health','MyCfd':'jxcfd'}
    r=f'http://152.70.115.213/jdcodes/submit.php?code={decode}&type={value}'
    if decode==0:
        return zlm_leixing_list,biaozhi
    else:
        return r   

@logit
def enurlnum2(decode,value):
    biaozhi='helloworld'
    zlm_leixing_list={'MyFruit':'farm','MyBean':'bean','MyPet':'pet','MyDreamFactory':'jxfactory','MyJdFactory':'ddfactory','MySgmh':'sgmh','MyHealth':'health','MyCfd':'jxcfd'}
    r=f'https://api.jdsharecode.xyz/api/runTimes?activityId={value}&sharecode={decode}'
    if decode==0:
        return zlm_leixing_list,biaozhi
    else:
        return r        

@logit
def enurlnum3(decode,value):
    biaozhi='PasserbyBot'
    zlm_leixing_list={'MyFruit':'FruitCode','MyJdFactory':'FactoryCode', 'MyCfd':'CfdCode'}
    r=f'http://51.15.187.136:8080/activeJd{value}?code={decode}'
    if decode==0:
        return zlm_leixing_list,biaozhi
    else:
        return r 


if __name__=='__main__':
    run1num()
    enurlnum1(0,0)
    enurlnum2(0,0)
    enurlnum3(0,0)
        