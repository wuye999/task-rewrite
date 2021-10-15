# 沃邮箱网页版
# 入口>mail.wo.cn
# 随便抓一条mail.wo.cn链接，获取它的cookie,ua,sid  sid在链接里。
# 脚本功能为自动登录浏览，还在测试中
# 环境变量wy_womail为cookie，多账号用&分割
# export wy_womail="第1个cookie&第2个cookie"
# export wy_womail_ua="ua"
# export wy_womail_sid="sid"
import time
import os
import re
import requests
import sys
requests.packages.urllib3.disable_warnings()

# 13位时间戳
def gettimestamp():
    return str(int(time.time() * 1000))

def env_ua():
    try:
        ua=os.environ["wy_womail_ua"]
    except:
        ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
    return ua
    
def env_sid():
    try:
        sid=os.environ["wy_womail_sid"]
    except:
        print('获取sid失败，请检查是否填写了环境变量wy_womail_sid')
        exit()
    return sid

## 获取cooie
class Judge_env(object):
    ## 判断运行环境
    def getcodefile(self):
        global sys
        if '/ql' in os.path.abspath(os.path.dirname(__file__)):
            print("当前环境青龙\n")
            sys.path.append(os.path.abspath(os.path.dirname(__file__)))
        else:
            print('第三方环境\n') 
        if os.path.abspath('.') not in sys.path:
            sys.path.append(os.path.abspath('.'))

    ## 批量提取pin,输出ckkk,path,pin_list
    def main_run(self):
        self.getcodefile()
        cookie_list=os.environ["wy_womail"].split('&')       # 获取cookie_list的合集
        if len(cookie_list)<1:
            print('请填写环境变量wy_womail\n')    
        return cookie_list

# 
def headerss(cookie):
    headers = {
        'Host': 'mail.wo.cn',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'Accept': 'text/x-json',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': ua,
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://mail.wo.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://mail.wo.cn/coremail/XT5/index.jsp?sid={sid}',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
        'Cookie': cookie  
    }
    return headers

# 
def task_2(cookie):
    msg(f'开始任务 查看收信箱')
    url=f'https://mail.wo.cn/coremail/s/json?sid={sid}&func=mbox%3AlistMessages'
    headers=headerss(cookie)
    data='{"fid":1,"start":0,"limit":20,"mode":"count","order":"receivedDate","desc":true,"returnTotal":true,"summaryWindowSize":20,"skipLockedFolders":false,"mboxa":"","topFirst":true,"filterFlags":{}}'
    for n in range(3):
        a=0
        try:
            time.sleep(0.5)
            res = requests.post(url=url, headers=headers, data=data, timeout=2,verify=False).json()
            a=1
            break
        except:
            msg('请求失败，正在重试🌍...')
    if a!=1:
        msg('❗任务失败...')
        return False
    code=res['code']
    if code=='S_OK':
        msg('任务成功\n')
    else:
        msg('❗️未知错误\n')
        return False

def task_1(cookie):
    msg(f'开始任务 登录')
    url=f'https://mail.wo.cn/coremail/s/json?sid={sid}&func=user%3AgetPasswordKey'
    headers={
        'Host': 'mail.wo.cn',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'Accept': 'text/x-json',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': ua,
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://mail.wo.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mail.wo.cn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
        'Cookie': cookie
    }
    for n in range(3):
        a=0
        try:
            time.sleep(0.5)
            res = requests.post(url=url, headers=headers, timeout=2,verify=False).json()
            a=1
            break
        except:
            msg('请求失败，正在重试🌍...')
    msg(f"sid: {res['var']['sid']}")
    if a!=1:
        msg('❗任务失败...')
        return False
    code=res['code']
    if code=='S_OK':
        msg('任务成功\n')
    else:
        msg('❗️未知错误\n')
        return False


# 检查账号有效性
def getUserInfo(cookie):
    url = f'https://mail.wo.cn/coremail/XT5/jsp/mail.jsp?sid={sid}&func=getAllFolders'
    headers=headerss(cookie)
    data='stats=true&threads=false'
    try:
        time.sleep(0.2)
        if sys.platform == 'ios':
            resp = requests.post(url=url, verify=False, headers=headers, data=data, timeout=60).json()
        else:
            resp = requests.post(url=url, headers=headers, data=data, timeout=60).json()
        if resp['code'] == "S_OK":
            return True
        else:
            msg(f"该账号Cookie 已失效！请重新获取。")
    except:
        msg(f"该账号Cookie 已失效！请重新获取。")
    return False


def doTask(cookie):
    a=getUserInfo(cookie)
    if not a:
        return
    task_1(cookie)
    task_2(cookie)


## 获取通知服务
class msg(object):
    def __init__(self, m):
        self.str_msg = m
        self.message()
    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            msg_info = f'{msg_info}\n{self.str_msg}'
        except:
            msg_info = f'{self.str_msg}'
        sys.stdout.flush()
    def getsendNotify(self, a=0):
        if a == 0:
            a += 1
        try:
            url = 'https://ghproxy.com/https://raw.githubusercontent.com/wuye999/jd/main/sendNotify.py'
            response = requests.get(url)
            if 'curtinlv' in response.text:
                with open('sendNotify.py', "w+", encoding="utf-8") as f:
                    f.write(response.text)
            else:
                if a < 5:
                    a += 1
                    return self.getsendNotify(a)
                else:
                    pass
        except:
            if a < 5:
                a += 1
                return self.getsendNotify(a)
            else:
                pass
    def main(self):
        global send
        cur_path = os.path.abspath('.')
        sys.path.append(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            try:
                from sendNotify import send
            except:
                self.getsendNotify()
                try:
                    from sendNotify import send
                except:
                    print("加载通知服务失败~")
        else:
            self.getsendNotify()
            try:
                from sendNotify import send
            except:
                print("加载通知服务失败~")       
msg("").main()  # 初始化通知服务


if __name__ == '__main__':
    msg('🔔沃邮箱网页版，开始！\n')
    ua=env_ua()
    sid=env_sid()
    cookie_list=Judge_env().main_run()
    msg(f'====================共 {len(cookie_list)} 个沃邮箱网页版账号Cookie=========\n')
    for e,cookie in enumerate(cookie_list,start=1):
        msg(f'******开始【账号 {e}】 *********\n')
        doTask(cookie)
    send('🔔沃邮箱网页版', msg_info)   # 启用通知服务

