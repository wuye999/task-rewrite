#coding=utf-8
"""
青龙里填写 环境变量 JD_WSCK  格式pin=xxx;wskey=xxxx
"""
## 填写你的signbody文件地址及文件名，默认读取 /ql/config/code/signbody1.txt
## 填写你的signbody文件地址及文件名，默认读取 /ql/config/code/signbody1.txt
## 填写你的signbody文件地址及文件名，默认读取 /ql/config/code/signbody1.txt
## 注意signbody文件每行一条信息。 
fauc = "/ql/config/code/signbody1.txt"

import linecache
import random
import requests
import time
import json
import re
import uuid
requests.packages.urllib3.disable_warnings()

token = ""
username = ""
password = ""
if username == "" or password == "":
    f = open("/ql/config/auth.json")
    auth = f.read()
    auth = json.loads(auth)
    username = auth["username"]
    password = auth["password"]
    token = auth["token"]
    f.close()


def gettimestamp():
    return str(int(time.time() * 1000))


def login(username, password):
    url = "http://127.0.0.1:5700/api/login?t=%s" % gettimestamp()
    data = {"username": username, "password": password}
    r = s.post(url, data)
    s.headers.update({"authorization": "Bearer " + json.loads(r.text)["data"]["token"]})


def getitem(key):
    url = "http://127.0.0.1:5700/api/envs?searchValue=%s&t=%s" % (key, gettimestamp())
    r = s.get(url)
    item = json.loads(r.text)["data"]
    return item


def getckitem(key):
    url = "http://127.0.0.1:5700/api/envs?searchValue=JD_COOKIE&t=%s" % gettimestamp()
    r = s.get(url)
    for i in json.loads(r.text)["data"]:
        if key in i["value"]:
            return i
    return []

#随机读取本地signbody
def bendi_body():
    count = 0
    dbn = 30
    k = 1
    ## 判断signbody是否为空，循环获取直到signbody不为空
    while count <= dbn:
        txt = open(fauc, 'rb')  
        data = txt.read().decode('utf-8')   # python3一定要加上这句不然会编码报错！
        txt.close()
        n = data.count('\n')  # 获取txt的总行数！
        i = random.randint(1, n)
        print("\n本次使用第 【%s】 条signbody" % (i))
        res=linecache.getline(fauc, i)  ###得到对应的i行的数据
        count = 0
        all_res = res[count:]
        for x in all_res:
            count += 1
        if count <= dbn:
            print("本条signbody为空，正重新获取，第 【%s】 次尝试" % k)
            k += 1
    else:   
        return res

def genToken(wsCookie):
    res = bendi_body()
    res = res.replace("'","\"")
    r = json.loads(res)
    data=r["sign"].split("&")
    jduuid = data[1]
    clientVersion = data[3]
    client = data[2]
    sign = data[4] + "&" + data[5] + "&" + data[6]
    url = "https://api.m.jd.com/client.action?functionId=genToken&%s&%s&%s&%s" % (clientVersion, client, jduuid, sign)
    headers = {
        "Host": 'api.m.jd.com',
        "Cookie": wsCookie,
        "accept": '*/*',
        "referer": '',
        'user-agent': "okhttp/3.12.1;jdmall;apple;version/9.4.0;build/88830;screen/1440x3007;os/11;network/wifi;" + str(
            uuid.uuid4()),
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;',
    }
    r = requests.post(url, headers=headers, data="body=%7B%22to%22%3A%20%22https%3A//home.m.jd.com/myJd/newhome.action%22%2C%20%22action%22%3A%20%22to%22%7D")
    r = json.loads(r.text)["tokenKey"]
    return r


def getJDCookie(tokenKey):
    url = "https://un.m.jd.com/cgi-bin/app/appjmp?tokenKey=%s&to=https://home.m.jd.com/myJd/newhome.action" % tokenKey
    headers = {
        "Connection": 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Accept": 'application/json, text/plain, */*',
        'Accept-Language': 'zh-cn',
        "User-Agent": 'okhttp/3.12.1;jdmall;apple;version/9.4.0;build/88830;screen/1440x3007;os/11;network/wifi;' + str(
            uuid.uuid4())
    }
    r = requests.get(url, headers=headers, allow_redirects=False,)
    pt_pin = re.findall(r"pt_pin=(.*?);", str(r.headers))[0]
    pt_key = re.findall(r"pt_key=(.*?);", str(r.headers))[0]
    return "pt_key=" + pt_key + ";pt_pin=" + pt_pin + ";"


def wstopt(wskey):
    try:
        token = genToken(wskey)
        r = getJDCookie(token)
        return r
    except:
        return "error"


def update(text, qlid):
    url = "http://127.0.0.1:5700/api/envs?t=%s" % gettimestamp()
    s.headers.update({"Content-Type": "application/json;charset=UTF-8"})
    data = {
        "name": "JD_COOKIE",
        "value": text,
        "_id": qlid
    }
    r = s.put(url, data=json.dumps(data))
    if json.loads(r.text)["code"] == 200:
        return True
    else:
        return False


def insert(text):
    url = "http://127.0.0.1:5700/api/envs?t=%s" % gettimestamp()
    s.headers.update({"Content-Type": "application/json;charset=UTF-8"})
    data = []
    data_json = {
        "value": text,
        "name": "JD_COOKIE"
    }
    data.append(data_json)
    r = s.post(url, json.dumps(data))
    if json.loads(r.text)["code"] == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    s = requests.session()
    if token == "":
        login(username, password)
    else:
        s.headers.update({"authorization": "Bearer " + token})
    wskeys = getitem("JD_WSCK")
    count = 1
    for i in wskeys:
        if i["status"] == 0:
            r = wstopt(i["value"])
            if r == "error":
                print("失败，请检查本地文件是否正确")
            else:
                ptck = r
                try:
                    wspin = re.findall(r"pin=(.*?);", i["value"])[0]
                    if ptck == "wskey错误":
                        print("第%s个wskey可能过期了,pin为%s" % (count, wspin))
                    elif ptck == "未知错误" or ptck == "error":
                        print("第%s个wskey发生了未知错误,pin为%s" % (count, wspin))
                    elif "</html>" in ptck:
                        print("你的ip被cloudflare拦截")
                    else:
                        ptpin = re.findall(r"pt_pin=(.*?);", ptck)[0]
                        item = getckitem("pt_pin=" + ptpin)
                        if item != []:
                            qlid = item["_id"]
                            if update(ptck, qlid):
                                print("第%s个wskey更新成功,pin为%s" % (count, wspin))
                            else:
                                print("第%s个wskey更新失败,pin为%s" % (count, wspin))
                        else:
                            if insert(ptck):
                                print("第%s个wskey添加成功" % count)
                            else:
                                print("第%s个wskey添加失败" % count)
                except:
                    print("第%s个wskey出现异常错误" % count)
                count += 1
        else:
            print("有一个wskey被禁用了")
