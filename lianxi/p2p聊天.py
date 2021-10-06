"""
目前采用udp发送数据，各个用户p2p对等聊天，不经过服务器转发
实现与指定对象发起聊天，接收任意对象的消息
在本地保存与各个对象的聊天记录
该客户端修改本地绑定地址与文件保存地址后可复用
"""

import socket
import threading
from datetime import datetime


def addr_split(addr: str):
    """将输入的地址字符串解析为IP地址和端口号"""
    ip, port = addr.rsplit(',', maxsplit=1)
    # ip是字符串，端口号是整数，返回它俩的元组
    return ip, int(port)


def rec_msg(sk, save_path):
    """循环监听，接收消息"""
    while True:
        data, addr = sk.recvfrom(1024)
        utf8_data = data.decode('utf-8')
        print('来自{0}：\n{1}'.format(addr, utf8_data))
        filename = "({0}_{1}).txt".format(addr[0], addr[1])
        # 写入我收到的内容至与对应发送者的聊天记录
        with open(save_path + filename, 'a', encoding='utf-8') as f:
            # 获取当前时间的字符串，只精确到秒
            t_now = str(datetime.now()).rsplit('.', maxsplit=1)[0]
            # 写入发送时间+发送者地址+内容
            f.write(f'{t_now} from [{addr[0]}:{addr[1]}]\n' + utf8_data + '\n\n')


def send_msg(sk, ip_port, target_addr, save_path):
    """发送消息到目标对象"""
    filename = "({0}_{1}).txt".format(target_addr[0], target_addr[1])
    # 写入我发送的内容到与对应接收者的聊天记录
    with open(save_path + filename, 'a', encoding='utf-8') as f:
        while True:
            # 循环发送消息
            msg = input('发送消息：\n')
            if msg == 'q':
                print('结束聊天')
                break
            t_now = str(datetime.now()).rsplit('.', maxsplit=1)[0]
            f.write(f'{t_now} from [{ip_port[0]}:{ip_port[1]}]\n' + msg + '\n\n')
            # 用flush刷新缓存
            f.flush()
            # 也可以用print语句输出到指定文件，参数flush置为True刷新缓存
            # print(f'{t_now} from [{local_ip_port[0]}:{local_ip_port[1]}]\n' + msg + '\n\n', file=f, flush=True)
            # 发送内容到到目标地址
            sk.sendto(msg.encode('utf-8'), target_addr)


def chat(local_addr='192.168.3.7,9070', save_path=r'chat_record/'):
    # 解析ip与端口号
    ip_port = addr_split(local_addr)
    target_addr = addr_split(input("请输入好友地址，如 192.168.3.7,9080 ："))
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sk:
        sk.bind(ip_port)
        # 创建接收信息与发送信息两个子线程
        t_rec = threading.Thread(target=rec_msg, args=(sk, save_path))
        t_rec.start()
        t_send = threading.Thread(target=send_msg, args=(sk, ip_port, target_addr, save_path))
        t_send.start()
        # join方法在子线程结束后才能执行
        # 若不加join方法，执行完上述代码会跳出with语句执行函数剩余代码
        # 导致子线程的内容还没执行完就被with自动关闭了socket
        t_rec.join()
        t_send.join()


if __name__ == '__main__':
    chat()