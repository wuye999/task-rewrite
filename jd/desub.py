#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# 在tg bot提交助力码后，要使用作者的脚本才能激活。
# 运行本脚本后即可激活已提交的助力码，无需运行作者的脚本。
# 暂支持 he1pu, JD_ShareCode ，PasserbyBot。

import os
import functools
import imp
import time
import re
from multiprocessing import Pool

try:
    import requests
except Exception as e:
    print(e, "\n缺少requests 模块，请执行命令安装：pip3 install requests")
    exit(3)

## 判断运行环境
class Judge_env(object):
    ## 判断助力码文件位置
    def getckfile(self):
        if os.path.exists('/ql/log/.ShareCode'):
            print("当前环境为新版code.sh\n")
            return '/ql/log/.ShareCode'
        elif os.path.exists('/ql/log/code'):
            print("当前环境为旧版code.sh\n")
            return '/ql/log/code'
        elif os.path.exists('/jd/log/jcode'):
            print("当前环境V4\n")
            return '/jd/log/jcode'
        else:
            print('暂不支持 青龙，v4 以外的环境\n')
            exit(0)

    ## 获取cookies的合集
    def account(self):
        cookies = os.environ["JD_COOKIE"]
        cookies=cookies.split('&')
        return cookies

    ## 提取单条cookie中的pin
    def pin_extract(self,cookie):
        pin = re.match(r'.+(pin\=)(.+)\;', cookie).group(2)
        return pin

    ## 批量提取pin,输出ckkk,path,pin_list
    def main_run(self):
        path=self.getckfile()
        cookies=self.account() 
        pin_list=list(map(self.pin_extract,cookies))
        ckkk=len(pin_list)
        return path,pin_list,ckkk


## 导入文件为模块
class Import_files(object):
    def __init__(self, path):
        self.path = path
        self.codes={}

    ## 导入单文件为模块
    def import2(self, a_file):
        self.codes = imp.load_source('foobar', a_file)

    ## 需要导入的文件组合成list
    def file_list(self, path):
        if path == '/ql/log/.ShareCode':
            files = [path+'/'+x for x in os.listdir(path) if os.path.isfile(path+'/'+x)]
        else:
            files = [path+'/'+x for x in os.listdir(path) if os.path.isfile(path+'/'+x)]
            files = sorted(files, reverse=True)
            files = [files[0]]
            ## 测试
            # print(files)
        return files

    ## 将list里的文件全部导入
    def main_run(self):
        files = self.file_list(self.path)
        list(map(self.import2, files))


## 根据key和ckkk组合出url合集
class Composite_urls(object):
    def __init__(self, data_pack, key, value, import_prefix, ckkk, biaozhi):
        self.data_pack=data_pack
        self.key=key
        self.value=value
        self.import_prefix=import_prefix
        self.ckkk=ckkk
        self.biaozhi = biaozhi

    ## 得到所有的助力码的list
    def generate_str_list(self):
        code_list=[]
        for n in range(1,self.ckkk+1):
            code_str = self.generate_str(self.key, n)  
            code_var = self.change_str(code_str)
            if code_var == 'zhan_wei_fu':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 不存在\n')
                continue
            if code_var == '' or code_var == ' ':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 为空\n')
                continue
            code_list.append(code_var)
        return code_list

    ## 得到单个code_str
    def generate_str(self, key, n):
        code_str = key+str(n)
        return code_str

    ## 把code_str和导入的助力码模块对应
    def change_str(self,code_str):
        try:
            code_str = eval(self.import_prefix+'.'+code_str)
            return code_str
        except AttributeError:
            code_str = 'zhan_wei_fu'
            return code_str
    
    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        code_list=self.generate_str_list()
        data_pack2=functools.partial(self.data_pack, value=self.value)
        url_list=list(map(data_pack2,code_list))
        return url_list, code_list


## 将url_list进行批量请求，判断结果
class Bulk_request(object):
    def __init__(self, url_list, code_list, value, biaozhi):
        self.url_list = url_list
        self.code_list = code_list
        self.value = value
        self.biaozhi = biaozhi
        self.g=0

    ##批量请求流程
    def main_run(self):
        for url in self.url_list:
            self.g = 1
            code=self.code_list[self.url_list.index(url)]
            self.request_process(url,code)

    ## 单个url进行请求得出结果
    def single_request(self,url):
        time.sleep(0.5)
        try:
            res = requests.get(url)
            return res.text
        except:
            res='Sever ERROR'
            return res

    ## 根据判断过的请求结果判断是否需要重新请求
    def judge_Retry(self,state,url):
        if state == 1:
            if self.g == 3:
                print(f'{self.biaozhi}_{self.value}：放弃挣扎')
                return
            self.g += 1
            print(f'{self.biaozhi}_{self.value}：第 {self.g} 次尝试提交')
            time.sleep(0.5)
            return self.request_process(self, url)

    ## 单个url请求，判断结果，是否重试的流程
    def request_process(self,url,code):  
        print(f'{self.biaozhi}_{self.value}：开始上报 {code}')
        res=self.single_request(url)
        state=self.processing_request_result(res)
        self.judge_Retry(state,url)

    ## 判断请求结果
    def processing_request_result(self,res):
        if 'Sever ERROR' in res:
            print(f'{self.biaozhi}_{self.value}：连接超时')
            state=1
            return state
        if self.biaozhi == 'he1pu':
            if 'Type ERROR' in res:
                print(f'{self.biaozhi}_{self.value}：提交类型无效\n')
                state=1
            elif '\"code\":300' in res:
                print(f'{self.biaozhi}_{self.value}：重复提交\n')
                state=0
            elif '\"code\":200' in res:
                print(f'{self.biaozhi}_{self.value}：提交成功\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}：服务器连接错误\n')
                state=1
        elif self.biaozhi=='helloworld':
            if '0' in res:
                print(f'{self.biaozhi}_{self.value}：请在tg机器人处提交助力码后再激活\n')
                state=0
            elif '1' in res:
                print(f'{self.biaozhi}_{self.value}：激活成功\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}：服务器连接错误\n')
                state=1
        elif self.biaozhi=='passerbyBot':
            if 'Cannot' in res:
                print(f'{self.biaozhi}_{self.value}：提交类型无效\n')
                state=1
            elif '激活成功' in res:
                print(f'{self.biaozhi}_{self.value}：激活成功\n')
                state=0
            elif '激活失败' in res:
                print(f'{self.biaozhi}_{self.value}：请在tg机器人处提交助力码后再激活\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}：服务器连接错误\n')
                state=1
        else:
            print(res)
            print('\n')
            state=0
        return state  


class He1pu_cfd_urls(Composite_urls):
    def __init__(self, data_pack, key, value, import_prefix, ckkk, biaozhi, pin_list):
        self.data_pack=data_pack
        self.key=key
        self.value=value
        self.import_prefix=import_prefix
        self.ckkk=ckkk
        self.biaozhi = biaozhi
        self.pin_list=pin_list

    ## 得到所有的助力码的list
    def generate_str_list(self):
        code_list=[]
        for n in range(1,self.ckkk+1):
            code_str = self.generate_str(self.key, n)  
            code_var = self.change_str(code_str)
            code_list.append(code_var)
        return code_list        

    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        code_list=self.generate_str_list()
        data_pack2=functools.partial(self.data_pack, value=self.value)
        if len(code_list)!=self.pin_list:
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
        url_list=[]
        for code in code_list:
            if code == 'zhan_wei_fu':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 不存在，本次请求取消\n')
                continue
            if code == '' or code == ' ':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 为空，本次请求取消\n')
                continue
            try:
                url=data_pack2(code,pin=self.pin_list[code_list.index(code)])
            except:
                print(f'{self.biaozhi}_{self.value}：该助力码对应的pin不存在，本次请求取消\n')
                continue
            url_list.append(url)
        return url_list, code_list


class He1pu_cfd_request(Bulk_request):
    ## 单个url请求，判断结果，是否重试的流程
    def request_process(self,url,code): 
        pin = re.match(r'.+(user\=)(.+)', url).group(2)
        print(f'{self.biaozhi}_{self.value}：开始上报 pin={pin}')
        res=self.single_request(url)
        state=self.processing_request_result(res)
        self.judge_Retry(state,url)    


class Helloworld_cfd_urls(Composite_urls):
    def __init__(self, data_pack, key, value, import_prefix, ckkk, biaozhi, pin_list):
        self.data_pack=data_pack
        self.key=key
        self.value=value
        self.import_prefix=import_prefix
        self.ckkk=ckkk
        self.biaozhi = biaozhi
        self.pin_list=pin_list

    ## 得到所有的助力码的list
    def generate_str_list(self,key):
        code_list=[]
        for n in range(1,self.ckkk+1):
            code_str = self.generate_str(key, n)  
            code_var = self.change_str(code_str)
            code_list.append(code_var)
        return code_list        

    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        jxcfd_code_list=self.generate_str_list('MyCfd')
        farm_code_list=self.generate_str_list('MyFruit')
        bean_code_list=self.generate_str_list('MyBean')
        data_pack2=functools.partial(self.data_pack, value=self.value)
        if len(jxcfd_code_list)!=self.pin_list:
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
            print(f'{self.biaozhi}_{self.value}：助力码数量与从pin数量不一致，上传可能会出现错误！！！\n')
        url_list=[]
        for jxcfd_code in jxcfd_code_list:
            if jxcfd_code == 'zhan_wei_fu':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 不存在，本次请求取消\n')
                continue
            if jxcfd_code == '' or jxcfd_code == ' ':
                print(f'{self.biaozhi}_{self.value}：{self.key}{str(n)} 为空，本次请求取消\n')
                continue

            if farm_code_list[jxcfd_code_list.index(jxcfd_code)] == 'zhan_wei_fu':
                print(f'{self.biaozhi}_{self.value}：MyFruit{str(n)} 不存在，本次请求取消\n')
                continue
            if farm_code_list[jxcfd_code_list.index(jxcfd_code)] == '' or farm_code_list[jxcfd_code_list.index(jxcfd_code)] == ' ':
                print(f'{self.biaozhi}_{self.value}：MyFruit{str(n)} 为空，本次请求取消\n')
                continue

            if bean_code_list[jxcfd_code_list.index(jxcfd_code)] == 'zhan_wei_fu':
                print(f'{self.biaozhi}_{self.value}：MyBean{str(n)} 不存在，本次请求取消\n')
                continue
            if bean_code_list[jxcfd_code_list.index(jxcfd_code)] == '' or bean_code_list[jxcfd_code_list.index(jxcfd_code)] == ' ':
                print(f'{self.biaozhi}_{self.value}：MyBean{str(n)} 为空，本次请求取消\n')
                continue           
            try:
                url=data_pack2(pin=self.pin_list[jxcfd_code_list.index(jxcfd_code)],farm_code=farm_code_list[jxcfd_code_list.index(jxcfd_code)],bean_code=bean_code_list[jxcfd_code_list.index(jxcfd_code)],jxcfd_code=jxcfd_code)
            except:
                print(f'{self.biaozhi}_{self.value}：该助力码对应的pin不存在，本次请求取消\n')
                continue
            url_list.append(url)
        return url_list, jxcfd_code_list


class Helloworld_cfd_request(Bulk_request):
    ## 单个url请求，判断结果，是否重试的流程
    def request_process(self,url,code): 
        pin = re.match(r'.+(pin\=)(.+)', url).group(2)
        print(f'{self.biaozhi}_{self.value}：开始上报 pin={pin}')
        res=self.single_request(url)
        state=self.processing_request_result(res)
        self.judge_Retry(state,url)

    def processing_request_result(self,res):
        if 'Sever ERROR' in res:
            print(f'{self.biaozhi}_{self.value}：连接超时')
            state=1
            return state
        if self.biaozhi=='helloworld':
            if '200' in res:
                print(f'{self.biaozhi}_{self.value}：已提交助力码\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}：提交失败！已提交farm和bean的cookie才可提交cfd\n')
                state=0
        else:
            print(res)
            print('\n')
            state=0
        return state  

## he1pu数据
def he1pu(decode, *, value):
    biaozhi = 'he1pu'
    correspond_data={'MyFruit':'farm','MyBean':'bean','MyPet':'pet','MyDreamFactory':'jxfactory','MyJdFactory':'ddfactory','MySgmh':'sgmh','MyHealth':'health','MyCfd':'jxcfd'}
    r=f'http://www.helpu.cf/jdcodes/submit.php?code={decode}&type={value}'
    if decode==0:
        return correspond_data, biaozhi
    else:
        return r   

## helloworld数据
def helloworld(decode, *, value):
    biaozhi='helloworld'
    correspond_data={'MyFruit':'farm','MyBean':'bean','MyPet':'pet','MyDreamFactory':'jxfactory','MyJdFactory':'ddfactory','MySgmh':'sgmh','MyHealth':'health','MyCfd':'jxcfd'}
    r=f'https://api.jdsharecode.xyz/api/runTimes?activityId={value}&sharecode={decode}'
    if decode==0:
        return correspond_data, biaozhi
    else:
        return r        

## passerbyBot数据
def passerbyBot(decode, *, value):
    biaozhi='passerbyBot'
    correspond_data={'MyFruit':'FruitCode','MyJdFactory':'FactoryCode', 'MyCfd':'CfdCode'}
    r=f'http://51.15.187.136:8080/activeJd{value}?code={decode}'
    if decode==0:
        return correspond_data, biaozhi
    else:
        return r 

## he1pu_cfd数据
def he1pu_cfd(decode, *, value, pin):
    biaozhi = 'he1pu'
    correspond_data={'MyCfd':'jxcfd'}
    r=f'http://www.helpu.cf/jdcodes/submit.php?code={decode}&type={value}&user={pin}'
    if value==0:
        return correspond_data, biaozhi
    else:
        return r

## helloworld_cfd数据
def helloworld_cfd(*, value, pin, farm_code, bean_code, jxcfd_code):
    biaozhi='helloworld'
    correspond_data={'MyCfd':'jxcfd'}
    r=f'https://api.jdsharecode.xyz/api/autoInsert/jxcfd?sharecode={jxcfd_code}&bean={bean_code}&farm={farm_code}&pin={pin}'
    if value==0:
        return correspond_data, biaozhi
    else:
        return r
     

## 主控制函数，组合各个类，完成请求任务
def main_run(data_pack, ckkk, import_prefix='import_1.codes'):
    correspond_data, biaozhi = data_pack(0, value=0)
    for key, value in correspond_data.items():
        ##将数据传入Composite_urls类，得出url_list
        url_list, code_list = Composite_urls(data_pack, key, value, import_prefix, ckkk, biaozhi).main_run()
        ## 批量请求url
        Bulk_request(url_list, code_list, value, biaozhi).main_run()

## he1pu_cfd控制函数
def he1pu_cfd_main_run(data_pack, ckkk, pin_list, import_prefix='import_1.codes'):
    correspond_data, biaozhi = data_pack(0,value=0,pin='0')
    for key, value in correspond_data.items():
        ##将数据传入He1pu_cfd_urls类，得出url_list
        url_list, code_list = He1pu_cfd_urls(data_pack, key, value, import_prefix, ckkk, biaozhi, pin_list).main_run()
        ## 批量请求url
        He1pu_cfd_request(url_list, code_list, value, biaozhi).main_run()   

## helloworld_cfd控制函数
def helloworld_cfd_main_run(data_pack, ckkk, pin_list, import_prefix='import_1.codes'):
    correspond_data, biaozhi = data_pack(value=0, pin=0, farm_code=0, bean_code=0, jxcfd_code=0)
    for key, value in correspond_data.items():
        ##将数据传入Helloworld_cfd_urls类，得出url_list
        url_list, code_list = Helloworld_cfd_urls(data_pack, key, value, import_prefix, ckkk, biaozhi, pin_list).main_run()
        ## 批量请求url
        Helloworld_cfd_request(url_list, code_list, value, biaozhi).main_run() 
 


if __name__=='__main__':
    p = Pool(3)
    path,pin_list,ckkk=Judge_env().main_run()
    import_1 = Import_files(path)
    import_1.main_run()
    p.apply_async(main_run(he1pu, ckkk))   ## 创建he1pu提交任务
    p.apply_async(main_run(helloworld, ckkk))  ## 创建helloworld提交任务
    p.apply_async(main_run(passerbyBot, ckkk))   ## 创建passerbyBot提交任务
    p.apply_async(he1pu_cfd_main_run(he1pu_cfd, ckkk, pin_list))   ## 创建he1pu_cfd提交任务
    p.apply_async(helloworld_cfd_main_run(helloworld_cfd, ckkk, pin_list))   ## 创建helloworld_cfd提交任务
    p.close()
    p.join()
    print('\nwuye9999')
    

