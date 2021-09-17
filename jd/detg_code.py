#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#填写
api_id = 12345 #申请的TG API ID
api_hash = '0123456789abcdef0123456789abcdef' #申请的TG API hash
# 青龙 or v4
xitong="qinglong"

# 脚本为自动读取验证码，发送到tg bot上，暂支持 JD_ShareCode ，PasserbyBot。
# 申请api_id 和 api_hash ，前往：https://my.telegram.org/auth?to=apps
# 第一次在命令行进入脚本目录，运行python3 detg_code.py 登陆tg获取密钥
# 屏幕显示Please enter your phone (or bot token）的时候，输入手机号获取验证码
# 验证码会发送到tg

import os
import functools
import imp
import time

try:
    from telethon import TelegramClient, events, sync
except:
    print("\n缺少telethon 模块，请执行命令安装：pip3 install telethon")
    exit(3)

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

def tg_send(tg_information,biaozhi):
    print(f'开始向 {biaozhi} 发送消息 {tg_information} ')
    try:
        global client
        client.send_message(biaozhi, tg_information)
        print('完成\n')
    except ValueError:
        print(f'失败，请手动向 {biaozhi} 发送一条消息，等待它回消息后尝试\n')

def logit(enurlnums):
    @functools.wraps(enurlnums)
    def run2num(*args, **kwargs):
        a,b=0,0
        zlm_leixing_list,biaozhi=enurlnums(a,b)
        print(f'########在tg向 {biaozhi} 发送消息########\n')
        for key,value in zlm_leixing_list.items():
            g=0
            for n in nnum(key):
                if n==ckkk+1:
                    break
                encode=zinum(key,n)
                decode=strnum(encode)
                if decode=='zhan_wei_fu':
                    continue
                if decode=='' or decode==' ':
                    continue
                #print(decode+' 测试1')
                def tg_code(decode):
                    global tg_codes
                    nonlocal g
                    if g==0:
                        tg_codes=decode
                        g+=1
                    elif tg_codes.count('&')<4:
                        tg_codes=tg_codes+'&'+decode
                tg_code(decode)
                #print(tg_codes+'测试2')
            tg_information=enurlnums(tg_codes,value)
            #print(tg_information+'测试3')
            tg_send(tg_information,biaozhi)
    return run2num


@logit
def enurlnum1(tg_codes,value):
    biaozhi='@JD_ShareCode_Bot'
    zlm_leixing_list={'MyFruit':'farm','MyBean':'bean','MyPet':'pet','MyDreamFactory':'jxfactory','MyJdFactory':'ddfactory','MySgmh':'sgmh','MyHealth':'health'}
    tg_information=f'/{value} {tg_codes}'
    if tg_codes==0:
        return zlm_leixing_list,biaozhi
    else:
        return tg_information

@logit
def enurlnum2(tg_codes,value):
    biaozhi='@passerbybbot'
    zlm_leixing_list={'MyFruit':'jd_fruit','MyDreamFactory':'jx_factory'}
    tg_information=f'/{value} {tg_codes}'
    if tg_codes==0:
        return zlm_leixing_list,biaozhi
    else:
        return tg_information





if __name__=='__main__':
    ckkk=10
    client = TelegramClient('anon', api_id, api_hash)
    client.start()
    print('第一次在命令行进入脚本目录，运行python3 detg_code.py 登陆tg获取密钥')
    #client.send_message('@JD_ShareCode_Bot', 'Hello, myself!')
    #rint('测试向收藏夹发送 Hello, myself! 这段话')
    run1num()
    enurlnum1(0,0)
    enurlnum2(0,0)
    
        

