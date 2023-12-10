import requests
import json
import os

# 推送开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写pushplus的sckey,不开启推送则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
COOKIES = os.environ["COOKIES"]
cookies = COOKIES.split('&&')


def start():
    url = "https://glados.one/api/user/checkin"
    url2 = "https://glados.one/api/user/status"
    referer = 'https://glados.one/console/checkin'
    origin = "https://glados.one"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.one'
    }
    for cookie in cookies:
        try:
            checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                                  'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
        except requests.exceptions.SSLError:
            checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                                  'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload), proxies={'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'})
        state = requests.get(url2, headers={
                             'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    # --------------------------------------------------------------------------------------------------------#
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        email = state.json()['data']['email']
        if 'message' in checkin.text:
            mess = checkin.json()['message']
            if sever == 'on':
                requests.get('http://www.pushplus.plus/send?token=' +
                             sckey + '&title='+mess+'&content='+email+' 剩余'+time+'天')
        else:
            requests.get('http://www.pushplus.plus/send?token=' +
                         sckey + '&content='+email+'更新cookie')
     # --------------------------------------------------------------------------------------------------------#


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
