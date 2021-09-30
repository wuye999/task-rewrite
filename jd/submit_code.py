# 在tg bot提交助力码后，要使用作者的脚本才能激活。
# 运行本脚本后即可激活已提交的助力码，无需运行作者的脚本。
# 暂支持 he1pu, helloworld ，PasserbyBot。

import os
import logging
import functools
import time
import re
from  multiprocessing import Pool
try:
    import requests
except Exception as e:
    logging.info(e, "\n缺少requests 模块，请执行命令安装: pip3 install requests")
    exit(3)
logging.basicConfig(level=logging.INFO)

## 判断运行环境
class Judge_env(object):
    ## 判断助力码文件位置
    def getcodefile(self):
        if os.path.exists('/ql/log/.ShareCode'):
            logging.info("当前环境为新版code.sh\n")
            return '/ql/log/.ShareCode'
        elif os.path.exists('/ql/log/code'):
            logging.info("当前环境为旧版code.sh\n")
            return '/ql/log/code'
        elif os.path.exists('/jd/log/jcode'):
            logging.info("当前环境V4\n")
            return '/jd/log/jcode'
        else:
            logging.info('暂不支持 青龙，v4 以外的环境\n')
            exit(0)

    ## 批量提取pin,输出ckkk,path,pin_list
    def main_run(self):
        path=self.getcodefile()
        cookie_list=os.environ["JD_COOKIE"].split('&')       # 获取cookie_list的合集
        pin_list=[re.match(r'.+pin=(.+)\;', cookie).group(1) for cookie in cookie_list]  # 提取cookie中的pin
        ckkk=len(cookie_list)      
        return path,pin_list,ckkk

# 生成助力码合集
class Import_files(object):
    def __init__(self, path, match_list,name_list=[]):
        self.path = path
        self.match_list=sorted(match_list)
        if len(name_list)==0:
            self.name_list=self.match_list
        else:
            self.name_list=sorted(name_list)
        self.codes={}

    ## 需要导入的文件组合成list
    def file_list(self):
        if self.path == '/ql/log/.ShareCode':
            files = [self.path+'/'+x for x in os.listdir(self.path) if os.path.isfile(self.path+'/'+x)]
        else:
            files = [self.path+'/'+x for x in os.listdir(self.path) if os.path.isfile(self.path+'/'+x)]
            files = sorted(files, reverse=True)
            files = [files[0]]
        return sorted(files)

    ## 将list里的文件全部读取
    def main_run(self):     
        files_list = self.file_list()
        match_files_dict=dict(zip(self.match_list,files_list))
        for match,files in match_files_dict.items():
            self.read_code(match,files)
        
    # 根据self.match_list中的关键字读取文件中的助力码
    def read_code(self,match,files):
        a=[]
        n=1
        with open(files, 'r') as f:
            for line in f.readlines():
                try:
                    regular=re.match(r'.*?'+match+'.*?\'(.*?)\'', line).group(1)
                    a.append(regular)
                    n+=1
                except:
                    pass
                if n==ckkk+1:
                    break
        self.codes[self.name_list[self.match_list.index(match)]]=a

# 生成助力码合集
class Look_log_code(Import_files):
    # 根据self.match_list中的关键字读取文件中的助力码
    def read_code(self,match,files):
        a=[]
        n=1
        with open(files, 'r') as f:
            for line in f.readlines():
                try:
                    regular=re.match(r'.*?'+match+'.*?\】(.*?)\n', line).group(1)
                    a.append(regular)
                    n+=1
                except:
                    pass
                if n==ckkk+1:
                    break
        self.codes[self.name_list[self.match_list.index(match)]]=a   

# 合成url
class Composite_urls(object):
    def __init__(self, data_pack, import_prefix):
        self.data_pack=data_pack
        self.import_prefix=import_prefix
        self.name_value_dict,self.biaozhi = data_pack(0)
    
    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        url_list=[]
        for name,value in self.name_value_dict.items():
            data_pack2=functools.partial(self.data_pack, value=value)
            decode_list=eval(f'{self.import_prefix}.codes[\'{name}\']')
            n=0
            for decode in decode_list:
                n+=1
                if decode == '' or decode == ' ':
                    print(f'{self.biaozhi}_{value}: My{name}{str(n)} 为空\n')
                    continue
                url=data_pack2(decode)
                url_list.append(url)
        return url_list,self.biaozhi

# He1pu_cfd的url合集
class He1pu_cfd_urls(Composite_urls):
    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        url_list=[]
        for name,value in self.name_value_dict.items():
            data_pack2=functools.partial(self.data_pack, value=value)
            decode_list=eval(f'{self.import_prefix}.codes[\'{name}\']')
            n=0
            for decode in decode_list:
                n+=1
                try:
                    pin=pin_list[n-1]
                except:
                    print(f'{self.biaozhi}_{value}: My{name}{str(n)} 对应的pin不存在\n')
                    continue
                if decode == '' or decode == ' ':
                    print(f'{self.biaozhi}_{value}: My{name}{str(n)} 为空\n')
                    continue
                url=data_pack2(decode,pin=pin)
                url_list.append(url)
        return url_list,self.biaozhi


# Helloworld_cfd的url合集
class Helloworld_cfd_urls(Composite_urls):
    ## 根据助力码和self.value通过data_pack组合出url_list,输出结果
    def main_run(self):
        url_list=[]
        for name,value in self.name_value_dict.items():
            data_pack2=functools.partial(self.data_pack, value=value)
            decode_list=eval(f'{self.import_prefix}.codes[\'{name}\']')
            farm_code_list=eval(f'{self.import_prefix}.codes[\'Fruit\']')
            bean_code_list=eval(f'{self.import_prefix}.codes[\'Bean\']')        
            n=0
            for decode in decode_list:
                n+=1
                try:
                    pin=pin_list[n-1]
                    farm_code=farm_code_list[n-1]
                    bean_code=bean_code_list[n-1]
                except:
                    print(f'{self.biaozhi}_{value}: My{name}{str(n)} 对应的pin或farm_code或bean_code不存在\n')
                    continue
                if decode == '' or decode == ' ':
                    print(f'{self.biaozhi}_{value}: My{name}{str(n)} 为空\n')
                    continue
                url=data_pack2(decode,pin=pin,farm_code=0, bean_code=bean_code)
                url_list.append(url)
        return url_list,self.biaozhi


## he1pu_cfd控制函数
def helloworld_cfd_main_run(data_pack, import_prefix='law_code'):
    url_list,biaozhi=Helloworld_cfd_urls(data_pack, import_prefix).main_run()
    Bulk_request(url_list, biaozhi).main_run()

## he1pu_cfd控制函数
def he1pu_cfd_main_run(data_pack, import_prefix='law_code'):
    url_list,biaozhi=He1pu_cfd_urls(data_pack, import_prefix).main_run()
    Bulk_request(url_list, biaozhi).main_run()

## 将url_list进行批量请求，判断结果
class Bulk_request(object):
    def __init__(self, url_list, biaozhi):
        self.url_list = url_list
        self.biaozhi = biaozhi
        self.g=0
    
    ##批量请求流程
    def main_run(self):
        for url in self.url_list:
            self.g = 1
            self.request_process(url)

    ## 单个url请求，判断结果，是否重试的流程
    def request_process(self,url):  
        code,self.value,pin=self.regular_extract(url)
        biaozhi=self.biaozhi.split('_')[0]
        print(f'{biaozhi}_{self.value}: 开始上报 {code} {pin}')
        res=self.single_request(url)
        state=self.processing_request_result(res)
        self.judge_Retry(state,url) 

    # 正则提取信息
    def regular_extract(self,url):
        if self.biaozhi=='he1pu' or self.biaozhi=='helloworld':
            a=re.match(r'.*?=(.*?)\&.*?=(.*)',url)
            code=a.group(1)
            value=a.group(2)
            pin=''
        elif self.biaozhi=='passerbyBot':
            a=re.match(r'.*?activeJd(.*?)\?.*?=(.*)',url)
            code=a.group(2)
            value=a.group(1)
            pin='' 
        elif self.biaozhi=='he1pu_cfd':
            a=re.match(r'.*?=(.*?)\&.*?=(.*?)\&(.*)',url)
            code=''
            value=a.group(2)
            pin=a.group(3)    
        elif self.biaozhi=='helloworld_cfd':
            a=re.match(r'.*?sert\/(.*?)\?.*=(.*?)\&.*?=(.*?)\&.*?=(.*?)\&(.*)',url)
            code=''
            value=a.group(1) 
            pin=a.group(5)
        return code,value,pin

    # 单个url进行请求得出结果
    def single_request(self,url):
        time.sleep(0.5)
        try:
            res = requests.get(url)
            return res.text
        except:
            res='Sever ERROR'
            return res

    # 判断请求结果
    def processing_request_result(self,res):
        if 'Sever ERROR' in res:
            print(f'{self.biaozhi}_{self.value}: 连接超时\n')
            state=1
            return state
        if self.biaozhi == 'he1pu' or self.biaozhi == 'he1pu_cfd':
            if 'Type ERROR' in res:
                print(f'{self.biaozhi}_{self.value}: 提交类型无效\n')
                state=1
            elif '\"code\":300' in res:
                print(f'{self.biaozhi}_{self.value}: 重复提交\n')
                state=0
            elif '\"code\":200' in res:
                print(f'{self.biaozhi}_{self.value}: 提交成功\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}: 服务器连接错误\n')
                state=1
        elif self.biaozhi=='helloworld' or self.biaozhi=='helloworld_cfd':
            if '0' in res:
                print(f'{self.biaozhi}_{self.value}: 请在tg机器人处提交助力码后再激活\n')
                state=0
            elif '1' in res:
                print(f'{self.biaozhi}_{self.value}: 激活成功\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}: 服务器连接错误\n')
                state=1
        elif self.biaozhi=='passerbyBot':
            if 'Cannot' in res:
                print(f'{self.biaozhi}_{self.value}: 提交类型无效\n')
                state=1
            elif '激活成功' in res:
                print(f'{self.biaozhi}_{self.value}: 激活成功\n')
                state=0
            elif '激活失败' in res:
                print(f'{self.biaozhi}_{self.value}: 请在tg机器人处提交助力码后再激活\n')
                state=0
            else:
                print(f'{self.biaozhi}_{self.value}: 服务器连接错误\n')
                state=1
        else:
            print(res)
            print('\n')
            state=0
        return state  

    # 根据判断过的请求结果判断是否需要重新请求
    def judge_Retry(self,state,url):
        if state == 1:
            if self.g == 3:
                print(f'{self.biaozhi}_{self.value}: 放弃挣扎')
                return
            self.g += 1
            print(f'{self.biaozhi}_{self.value}: 第 {self.g} 次尝试提交')
            time.sleep(0.5)
            return self.request_process(url)


## he1pu数据
def he1pu(decode, *, value=0):
    biaozhi = 'he1pu'
    name_value_dict={'Fruit':'farm','Bean':'bean','Pet':'pet','DreamFactory':'jxfactory','JdFactory':'ddfactory','Sgmh':'sgmh','Health':'health'}
    r=f'http://www.helpu.cf/jdcodes/submit.php?code={decode}&type={value}'
    if decode==0:
        return name_value_dict, biaozhi
    else:
        return r  

## helloworld数据
def helloworld(decode, *, value=0):
    biaozhi='helloworld'
    name_value_dict={'Fruit':'farm','Bean':'bean','Pet':'pet','DreamFactory':'jxfactory','JdFactory':'ddfactory','Sgmh':'sgmh','Health':'health','Cfd':'jxcfd'}
    r=f'https://api.jdsharecode.xyz/api/runTimes?sharecode={decode}&activityId={value}'
    if decode==0:
        return name_value_dict, biaozhi
    else:
        return r        

## passerbyBot数据
def passerbyBot(decode, *, value=0):
    biaozhi='passerbyBot'
    name_value_dict={'Fruit':'FruitCode','JdFactory':'FactoryCode', 'Cfd':'CfdCode'}
    r=f'http://51.15.187.136:8080/activeJd{value}?code={decode}'
    if decode==0:
        return name_value_dict, biaozhi
    else:
        return r 

## he1pu_cfd数据
def he1pu_cfd(decode, *, pin=0, value=0):
    biaozhi = 'he1pu_cfd'
    name_value_dict={'Cfd':'jxcfd'}
    r=f'http://www.helpu.cf/jdcodes/submit.php?code={decode}&type={value}&user={pin}'
    if value==0:
        return name_value_dict, biaozhi
    else:
        return r

## helloworld_cfd数据
def helloworld_cfd(decode, *, pin=0, farm_code=0, bean_code=0, value=0):
    biaozhi='helloworld_cfd'
    name_value_dict={'Cfd':'jxcfd'}
    r=f'https://api.jdsharecode.xyz/api/autoInsert/{value}?sharecode={decode}&bean={bean_code}&farm={farm_code}&pin={pin}'
    if value==0:
        return name_value_dict, biaozhi
    else:
        return r

## he1pu_cfd数据
def he1pu_mohe(decode, *, pin=0, value=0):
    biaozhi = 'he1pu_cfd'
    name_value_dict={'mohe':'mohe'}
    r=f'http://www.helpu.cf/jdcodes/submit.php?code={decode}&type={value}&user={pin}'
    if value==0:
        return name_value_dict, biaozhi
    else:
        return r

def main_run(data_pack,import_prefix='law_code'):
    url_list,biaozhi=Composite_urls(data_pack, import_prefix).main_run()
    Bulk_request(url_list, biaozhi).main_run()

if __name__=='__main__':
    path,pin_list,ckkk=Judge_env().main_run()
    match_list=['Health', 'MoneyTree', 'JdFactory', 'DreamFactory', 'Cfd', 'Carni', 'TokenJxnc', 'Jxnc', 'Joy', 'City', 'Bean', 'Cash', 'Pet', 'BookShop', 'Jdzz', 'Sgmh', 'Fruit']
    law_code=Import_files(path,match_list)
    law_code.main_run()
    log_code=Look_log_code('/ql/log/shufflewzc_faker2_jd_mohe',['5G超级盲盒'],['mohe'])
    log_code.main_run()
    pool = Pool(3)
    pool.apply_async(func=main_run,args=(passerbyBot,))   ## 创建passerbyBot激活任务
    pool.apply_async(func=main_run,args=(he1pu,))   ## 创建he1pu提交任务
    pool.apply_async(func=main_run,args=(helloworld,))  ## 创建helloworld激活任务
    pool.apply_async(func=he1pu_cfd_main_run,args=(he1pu_cfd,))  ## 创建he1pu_cfd活任务
    pool.apply_async(func=helloworld_cfd_main_run,args=(helloworld_cfd,))  ## 创建helloworld_cfd激活任务
    pool.apply_async(func=he1pu_cfd_main_run,args=(he1pu_mohe,'log_code'))  ## 创建he1pu_mohe激活任务
    pool.close()
    pool.join()
    print('wuye9999')


