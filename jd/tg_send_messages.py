# 脚本为tg 定时发送消息，第一次请在命令行运行 cd /ql/scripts && python3 tg_send_messages.py 登陆tg获取密钥,验证码在tg内查看

# 脚本内填写 申请的TG API ID, 申请的TG API hash
# 向群't.me/iKuuuu_VPN' 发送 '长大了就不要笑得那么开心', 向机器人'@JD_ShareCode_Bot' 发送 '/help'。
tg_api_id = '12345'
tg_api_hash = '0123456789abcdef0123456789abcdef'
tg_send_messages_1='@iKuuuu_VPN>>>早'
tg_send_messages_2='@JD_ShareCode_Bot>>>/help' 

# 环境变量填写 ,会优先读取环境变量。
# export tg_api_id="12345"    
# export tg_api_hash="0123456789abcdef0123456789abcdef"  
# export tg_send_messages_1="@iKuuuu_VPN>>>长大了就不要笑得那么开心"
# export tg_send_messages_2="@JD_ShareCode_Bot>>>/help"

import os
import re
try:
    from telethon import TelegramClient, events, sync
except:
    print("\n缺少telethon 模块，请执行命令安装：pip3 install telethon")
    exit(3)

# 读取api
def get_tg_api():
    if 'tg_api_id' in os.environ:
        a=int(os.environ['tg_api_id'])
        b=os.environ['tg_api_hash']
    elif os.path.exists('/jd/log/jcode'):
        a=int(codes.set_var(['tg_api_id'],[r'export tg_api_id.*?="(.*?)"'],['/jd/config/config.sh'],1))
        b=codes.set_var(['tg_api_hash'],[r'export tg_api_hash.*?="(.*?)"'],['/jd/config/config.sh'],1)
    else:
        a=int(tg_api_id)
        b=tg_api_hash
    return a,b

# 读取不固定变量
def env_set(env):
    a=[]
    for n in range(1,999):
        try:
            if f'{env}_1' in os.environ:
                b=os.environ[f'{env}_{n}']
            elif os.path.exists('/jd/log/jcode'):
                b=codes.set_var([f'{env}_{n}'],[r'export '+f'{env}_{n}'+r'.*?="(.*?)"'],['/jd/config/config.sh'],1)
            else:
                b=eval(f'{env}_{n}')
            a.append(b)
        except:
            break
    return a


# 自定义正则匹配类
class Look_log_code(object):
    def __init__(self, name_list=0, match_list=0, path_list=0, stop_n=0):
        self.name_list=name_list 
        self.match_list=match_list      
        self.path_list = path_list
        self.stop_n=stop_n
        self.codes={}

    def set_var(self, name_list, match_list, path_list, stop_n):
        self.name_list=name_list 
        self.match_list=match_list      
        self.path_list = path_list
        self.stop_n=stop_n
        self.main_run()
        if len(name_list)==1:
            return self.codes[name_list[0]][0]

    ## 需要导入的文件组合成list
    def file_list(self):
        if os.path.isdir(self.path):
            files = [self.path+'/'+x for x in os.listdir(self.path) if os.path.isfile(self.path+'/'+x)]
            files = sorted(files, reverse=True)
            files = files[0]
        elif os.path.isfile(self.path):
            files=self.path
        else:
            print(f'文件夹或日志 {self.path} 不存在\n')
            files=False
        return files

    ## 将list里的文件全部读取
    def main_run(self):
        for e,self.path in enumerate(self.path_list):
            files = self.file_list()
            if files:
                self.read_code(files,self.match_list[e],self.name_list[e])
            else:
               self.codes[self.name_list[e]]=' '

    # 根据self.match_list中的关键字读取文件中的助力码
    def read_code(self,files,match,name):
        a=[]
        n=0
        re_match=re.compile(match)
        with open(files, 'r') as f:
            for line in f.readlines():
                try: 
                    b=re_match.match(line).group(1)
                    a.append(b)
                    n+=1
                except:
                    pass
                if n==self.stop_n:
                    break
        self.codes[name]=a


# 发送消息
def send_mess(tg_send_messages_list):
    with TelegramClient(anon, tg_api_id, tg_api_hash) as client:
        client.start()
        for username_information in tg_send_messages_list:
            a=username_information.split('>>>')
            print(f'{a[0]}: {a[1]}')
            try:
                client.send_message(a[0],a[1])
                print('ok\n')
            except ValueError as e:
                print(e)
                print(f'找不到用户名 {a[0]} 或群组 {a[0]} \n')

# 提示
def tip():
    if os.path.abspath('.')=='/ql/scripts':
        print("当前环境青龙\n")
        print('第一次请在命令行运行 cd /ql/scripts && python3 xxxxxx.py 登陆tg获取密钥\n')
        anon='anon'
    elif os.path.exists('/jd/log/jcode'):
        print("当前环境V4\n")
        print('第一次请在命令行运行 cd /jd/scripts && python3 xxxxxx.py 登陆tg获取密钥\n')
        anon='/jd/scripts/anon'
    else:
        print('运行目录下 python3 /运行目录/xxxxxx.py 登陆tg获取密钥\n')
        anon='anon'
    return anon


if __name__=='__main__':
    anon=tip()
    codes=Look_log_code()
    tg_api_id,tg_api_hash=get_tg_api()
    try:
        with TelegramClient(anon, tg_api_id, tg_api_hash) as client:
            client.start()    
    except:
        print('网络环境出错, 或tg_api出错，或验证出错')
    tg_send_messages_list=env_set('tg_send_messages')
    send_mess(tg_send_messages_list)
    print('\nwuye9999')
