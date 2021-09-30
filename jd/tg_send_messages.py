# 脚本为tg 定时发送消息，第一次请在命令行运行 cd /ql/scripts && python3 tg_send_messages.py 登陆tg获取密钥,验证码在tg内查看

# 脚本内填写 申请的TG API ID, 申请的TG API hash
# 向群't.me/iKuuuu_VPN' 发送 '长大了就不要笑得那么开心', 向机器人'@JD_ShareCode_Bot' 发送 '/help'。
tg_api_id = '12345'
tg_api_hash = '0123456789abcdef0123456789abcdef'
tg_send_messages_1='@iKuuuu_VPN>>>长大了就不要笑得那么开心'
tg_send_messages_2='@JD_ShareCode_Bot>>>/help' 

# 环境变量填写 ,会优先读取环境变量。
# export tg_api_id="12345"    
# export tg_api_hash="0123456789abcdef0123456789abcdef"  
# export tg_send_messages_1="@iKuuuu_VPN>>>长大了就不要笑得那么开心"
# export tg_send_messages_2="@JD_ShareCode_Bot>>>/help"

import os
try:
    from telethon import TelegramClient, events, sync
except:
    print("\n缺少telethon 模块，请执行命令安装：pip3 install telethon")
    exit(3)

# 读取api
try:
    tg_api_id=int(os.environ['tg_api_id'])
    tg_api_hash=os.environ['tg_api_hash']
except:
    tg_api_id=int(tg_api_id)

# 读取环境变量中要发送的消息
def env_send_messages():
    tg_send_messages_list=[]
    n=0
    while True:
        n+=1
        try:
            a=os.environ[f'tg_send_messages_{n}']
            tg_send_messages_list.append(a)
        except:
            break
    return tg_send_messages_list

# 读取脚本中要发送的消息
def local_send_messages():
    tg_send_messages_list=[]
    n=0
    while True:
        n+=1
        try:
            a=eval(f'tg_send_messages_{n}')
            tg_send_messages_list.append(a)
        except:
            break
    return tg_send_messages_list

# 发送消息
def send_mess(tg_send_messages_list):
    with TelegramClient('anon', tg_api_id, tg_api_hash) as client:
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


if __name__=='__main__':
    print('第一次请在命令行运行 cd /ql/scripts && python3 tg_send_messages.py 登陆tg获取密钥\n')
    try:
        with TelegramClient('anon', tg_api_id, tg_api_hash) as client:
            client.start()
    except:
        print('网络环境出错, 或tg_api出错')
    if 'tg_send_messages_1' in os.environ:
        tg_send_messages_list=env_send_messages()
    else:
        tg_send_messages_list=local_send_messages()
    send_mess(tg_send_messages_list)
    print('\nwuye9999')