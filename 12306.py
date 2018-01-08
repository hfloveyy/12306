

# 哈尔滨西 VAB
#VUQ 海口
#Z114
import requests
import ssl
import random
import time

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


ssl._create_default_https_context = ssl._create_unverified_context


user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

import logging   
     
# 创建一个logger   
logger = logging.getLogger('mylogger')   
logger.setLevel(logging.DEBUG)   
     
# 创建一个handler，用于写入日志文件   
fh = logging.FileHandler('test.log')   
fh.setLevel(logging.DEBUG)   
     
# 再创建一个handler，用于输出到控制台   
ch = logging.StreamHandler()   
ch.setLevel(logging.DEBUG)


logger.addHandler(fh)   
logger.addHandler(ch)
'''
1、暂停发售
{
"validateMessagesShowId":"_validatorMessage",
"status":true,
"httpstatus":200,
"data":
    {
    "result":
    ["null|
    列车运行图调整,暂停发售
    |0h0000Z11400|Z114|VAB|VUQ|VAB|VUQ|24:00|24:00|99:59|IS_TIME_NOT_BUY||20180125||B2|01|29|0|1|||||||||||||||||0"
    ],
    "flag":"1",
    "map":{"VAB":"哈尔滨西","VUQ":"海口"}
    },
    "messages":[],
    "validateMessages":{}
}

2、预定
{
"validateMessagesShowId":"_validatorMessage",
"status":true,"httpstatus":200,
"data":
    {
    "result":
    [
    "Bxfl44FmwcnmIwahnkiAUWy%2F5b%2Bm6caVsaLW3eJZF7iRPGhQQoD%2FSdJzeBlmDbsHE0CNKaGQkHvr%0AMYArTvgZxRafc5h9vchMhZvtI5H2Njkbiq95ACc%2FvpFU2vQoVahnJFSFv%2FRjtALK46xSrazv92Y9%0A6I0q1NPl0hMzLMsNf9VRJ8cGeRs0OZnkxMqga5WcZvGa9SoBrsrjAgI%2F0K5V34JeeMN8s%2BEKj0OR%0AwNaf84BlI5vq8JcByzHufs9avssaYtAHU76t5mo%3D
    |预订
    |0h000G120208|G1202|VAB|AOH|VAB|AOH|08:19|21:04|12:45|Y|KfvqaekbC0xI6Or79GijZvaudVw87tEQ%2F3mq3iqREIGgfBvX
    |20180113|3|B2|01|25|1|0|||||||||||有|有|2||O090M0|O9M|1",
    "d3TOC9qogxoFegU6FjH82JlKLIBOJhdUVmubOlx5t6nUmHj6d4extmVbuv9%2FJyc1jHxk3IKxXTo8%0A61AtZCeMkrULg4QuQMNluM8bvlGhIQrjTdz7b4nwZgicurlshJkhcT8pgUG51lfzbR%2Br6nyzf5AK%0Az0O95hBtY2Dy%2FN1gwf3HCSrSx8V%2FxdspHxnMM3YB16ADPeVmADAEvr%2FaiNp%2FCMQiIEIhpLolTOr9%0AtBTHzI0hO1uwnydgHONDA3aONB0UZ7LhPn9I08WGbyZe
    |预订
    |0h0000Z17400|Z174|VAB|SHH|VAB|SHH|12:51|12:50|23:59|Y|HD47njW2lsYJ3Im0wuPtGon5FXQcMeyd5Sk7Hk1oMfEFbbQ3Hhrpe5V92XU%3D
    |20180113|3|B2|01|15|0|0||||无|||有||无|无|||||10401030|1413|0"
    ],
    "flag":"1",
    "map":{"AOH":"上海虹桥","VAB":"哈尔滨西","SHH":"上海"}},
    "messages":[],"validateMessages":{}}




you piao 


['VIhc', '预订', '0h000G120208', 'G1202', 'VAB', 'AOH', 'VAB', 'AOH', '08:19', '21:04', '12:45', 'Y', 'hIE5V2', '20180110', '3', 'B2', '01', '25', '1', '0', '', '', '', '', '', '', '', '', '', '', '有', '有', '4', '', 'O0M090', 'OM9', '1']
['null', '预订', '0h0000Z11400', 'Z114', 'VAB', 'VUQ', 'VAB', 'VUQ', '11:10', '10:52', '47:42', 'N', 'pLu030', '20180110', '3', 'B2', '01', '29', '0', '0', '', '', '', '无', '', '', '无', '', '无', '无', '', '', '', '', '10401030', '1413', '0']
['null', '列车运行图调整,暂停发售', '0h0000Z11400', 'Z114', 'VAB', 'VUQ', 'VAB', 'VUQ', '24:00', '24:00', '99:59', 'IS_TIME_NOT_BUY', '', '20180124', '', 'B2', '01', '29', '0', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0']


'''


my_sender='85127658@qq.com'    # 发件人邮箱账号
my_pass = 'ukycjxjaotpebgfb'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='hfloveyy@icloud.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('有票','plain','utf-8')
        msg['From']=formataddr(["12306_mybot",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["hfloveyy",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="有票"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception as e:
        print(e)# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret




data = '2018-01-24'
from_station = 'VAB'
to_station = 'VUQ'#BJP

url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(data,from_station,to_station)
ua = random.choice(user_agent_list)
header = {'User-Agent':ua}


response = requests.get(url,headers = header,verify = False)
#print(response.text)


train_dict = response.json()
train_result = train_dict['data']['result']
train_list = train_result[0].split('|')
print(len(train_list))

if '有' in train_list:
    print("有票！")
    ret=mail()
    if ret:
        print("邮件发送成功")
        logger.info('有票！'+ time.asctime( time.localtime(time.time()) )) 
    else:
        print("failed")
else: 
    print("没票！")


#crontab 5 * * * * python 12306.py