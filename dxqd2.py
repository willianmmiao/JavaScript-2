# -*- coding: utf-8 -*-
import base64
import requests,json
import time
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Crypto.Util.Padding import pad

# 青龙安装依赖  pycryptodome

# 安卓用HttpCanary去微信小程序抓包，只能抓用户中心home_info_body的包。
# ios可用Thor去电信营业厅app抓包，Thor可抓所有包，可以PDD买账号下载。Stream无法抓包，其它抓包软件自测。

# 抓包数据填脚本里

# 手机号
config_list = [
   {"mobile": "15606100019", "food": True}
]
# 用户中心
# 抓包url   https://wapside.189.cn:9001/jt-sign/api/home/homeInfo
# home_info_body   {"para":"xx"}
home_info_body = {"para":"1d9c241956e36dd7e8336455f34d36a6fa40021e633c5525436524c18e8d3443e7c1f3d524872d5a303b24cc0c32c7989b95ee8f959aa12820898ed16c05a1817c6664d4b378ef5ed15b245c6c779e4b6eded3536cdbae1569b2638c0d297b2b7200f8dca7f1de0775d04574935a07f9ede3f735351d0d494339c78bc25a1c4b4c905351d23eb9f15877821f39ec3fb8100da877fb5d24fb12263f7af37839b1064c8a1db8765f9c192c258959e2641b337c08d94cf66b55614d47b7aef72a76409e996a0e3157f20e2ba09da9cf8c74f09b656fe5755f246ceb3d8a111ec82dcbabbbf83f956db0ca66e5bc3b7ce6fd3ae084dbb9270ff7f191381c533cde12"}

# 喂宠物
# https://wapside.189.cn:9001/jt-sign/paradise/food
# food_body   {"para":"xx"}
food_body = {"para":"aa313b5e2c9ad08eed2a4631b108af2abd599074ea1a717d4d94a76ba7a85f9f4b74f36218da559e29970c4ea7c2cb3258aa1734cede7a3c88d303a3e669bbd739bb2890f994bc7fa5c3303e1243bf2c91ae3d1161112070766383c83a27e01919c0ce488534e0b9ce43ac8cafe598e123f8e4bf71fd04da31c3e4266213b49d"}


# 分享  
# https://dxhd.189.cn:7081/actcenter/v1/goldcoinuser/shareToGetCoin.do
# share_body = {
#     'activityId': 'telecomrecommend01',
#     'session': 'xxx'
# }
share_body = {
      'activityId': 'telecomrecommend01',
      'session': '20220430125319784430788f031a14fd6a165f6f3e173ff00'
}

# 云盘
# 'https://wapside.189.cn:9001/jt-sign/paradise/polymerize'
# cloud_body = {"para":"xx"}
cloud_body = {"para":"5af12c83cf7085a7ad3fb02c1b52add6b9053ec77e168edc743f74432dd6d9a9152853f392d50c74957b63b97de4d5efdc366b32240a96974ed36a2d3e66db8c224ef6e1789a4c3a17fc86c5037dc80890ac9aed4cdfec7147f6f4691f44525f877f2493293e1437b5b9c731df46e48e3df3cb09262c6c48ea043f0c929673447d8737f3ab5e9165155bf44eac975e40b73cc8470daa429a2a43472dbc24733f705e0bf277eb0b326c63d8bfded0b000f34e9f76c18558624164489e0647ff7e9214d791712d138e211f7b48683da081af408e62fb3e4f89174436c17653833ba5eaaaae260e8cfb84c3dafe5dd40b404fae8504f9fa51344860085e4a873311"}

# 种树
# 'https://wapside.189.cn:9001/jt-sign/paradise/polymerize'
# tree_body = {"para":"xx"}
tree_body = {"para":"5af12c83cf7085a7ad3fb02c1b52add6b9053ec77e168edc743f74432dd6d9a9152853f392d50c74957b63b97de4d5efdc366b32240a96974ed36a2d3e66db8c224ef6e1789a4c3a17fc86c5037dc80890ac9aed4cdfec7147f6f4691f44525f877f2493293e1437b5b9c731df46e48e3df3cb09262c6c48ea043f0c929673447d8737f3ab5e9165155bf44eac975e40b73cc8470daa429a2a43472dbc24733f705e0bf277eb0b326c63d8bfded0b000f34e9f76c18558624164489e0647ff7e9214d791712d138e211f7b48683da081af408e62fb3e4f89174436c17653833ba5eaaaae260e8cfb84c3dafe5dd40b404fae8504f9fa51344860085e4a873311"}


msg = []

def telegram_bot(title, content):
    print("\n")
    title = 小枫电信签到  # 改成你要的标题内容
    content = 签到通知来了  # 改成你要的正文内容
    bot_token = '1610757066:AAET5OjZgXVb_CKOcj3O3j945D9cIAIhN-Y'
    user_id = '1212068357'

    print("tg服务启动")
    url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'chat_id': str(user_id), 'text': f'{title}\n\n{content}', 'disable_web_page_preview': 'true'}
    proxies = None
    response = requests.post(url=url, headers=headers, params=payload, proxies=proxies).json()
    if response['ok']:
        print('推送成功！')
    else:
        print('推送失败！')


def encrypt(text):
    key = '34d7cb0bcdf07523'.encode('utf-8')

    cipher = AES.new(key, AES.MODE_ECB)
    pad_pkcs7 = pad(text.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
    cipher_text = cipher.encrypt(pad_pkcs7)

    return b2a_hex(cipher_text)

def telecom_task(config):
    mobile = config['mobile']
    msg.append(mobile + " 开始执行任务...")
    h5_headers = get_h5_headers(mobile)
    # 获取用户中心
    home_info_ret = requests.post(url="https://wapside.189.cn:9001/jt-sign/api/home/homeInfo", json=home_info_body, headers=h5_headers).json()
    if home_info_ret['resoultMsg'] != "成功":
        msg.append(home_info_ret['resoultMsg'])
        return
    user_id = home_info_ret['data']['userInfo']['userThirdId']
    old_coin = home_info_ret['data']['userInfo']['totalCoin']

    # 签到
    t = time.time()
    time1 = int(round(t * 1000))
    body_json = {
        "phone": f"{mobile}",
        "date": time1,
        "signSource": "smlprgrm"
    }
    body_str = json.dumps(body_json)
    s = str(encrypt(body_str),'utf-8')
    sign_body = {
        "encode": s
    }

    sign_ret = requests.post(url="https://wapside.189.cn:9001/jt-sign/api/home/sign", json=sign_body,
                             headers=h5_headers).json()
    if sign_ret['data']['code'] == 1:
        msg.append("签到成功, 本次签到获得 " + str(sign_ret['data']['coin']) + " 豆")
    else:
        msg.append(sign_ret['data']['msg'])

    #share
    share(config)
    time.sleep(1)
    # 获取用户中心
    home_info_ret = requests.post(url="https://wapside.189.cn:9001/jt-sign/api/home/homeInfo", json=home_info_body,
                                  headers=h5_headers).json()
    new_coin = home_info_ret['data']['userInfo']['totalCoin']
    msg.append("领取完毕, 现有金豆: " + str(new_coin))
    msg.append("本次领取金豆: " + str(new_coin - old_coin))
    time.sleep(1)
    # 喂食
    food(config)

    msg.append("----------------------------------------------")

def food(config):
    if config['food']:
        mobile = config['mobile']
        msg.append(mobile + " 开始执行喂食...")
        while True:
            food_ret = requests.post(url="https://wapside.189.cn:9001/jt-sign/paradise/food", json=food_body,
                                     headers=get_h5_headers(mobile)).json()
            msg.append(food_ret['resoultMsg'])
            if food_ret['resoultCode'] != '0':
                break

#分享
def share(config):
    mobile = config['mobile']
    msg.append(mobile + "开始执行分享...")
    url = 'https://dxhd.189.cn:7081/actcenter/v1/goldcoinuser/shareToGetCoin.do'
    resp = requests.post(url=url,data=share_body,headers=get_h5_headers(mobile))
    print('share==============')
    print(resp)
    result = resp.text
    print(result)
    msg.append("分享" + result)

    cloud(mobile)
    time.sleep(2)
    tree(mobile)

# cloud
def cloud(mobile):
    msg.append(mobile + "访问云盘...")
    url='https://wapside.189.cn:9001/jt-sign/paradise/polymerize'
    resp = requests.post(url=url, json=cloud_body, headers=get_h5_headers(mobile))
    print('cloud=========')
    print(resp)
    result = resp.json()
    print(result)
    if result['resoultCode'] ==0:
        msg.append("云盘"+result['resoultMsg'])
    else:
        msg.append("云盘访问失败"+result['resoultMsg'])

# tree
def tree(mobile):
    msg.append(mobile + "种树...")
    url='https://wapside.189.cn:9001/jt-sign/paradise/polymerize'
    resp = requests.post(url=url, json=tree_body, headers=get_h5_headers(mobile))
    print('tree=========')
    print(resp)
    result = resp.json()
    print(result)
    if result['resoultCode'] ==0:
        msg.append("种树"+result['resoultMsg'])
    else:
        msg.append("种树访问失败"+result['resoultMsg'])


def get_h5_headers(mobile):
    base64_mobile = str(base64.b64encode(mobile[5:11].encode('utf-8')), 'utf-8').strip(r'=+') + "!#!" + str(
        base64.b64encode(mobile[0:5].encode('utf-8')), 'utf-8').strip(r'=+')
    return {"User-Agent": "CtClient;9.2.0;Android;10;MI 9;" + base64_mobile}


def format_msg():
    str = ''
    for item in msg:
        str += item + "\r\n"
    return str

def main_handler():
    for config in config_list:
        telecom_task(config)
    content = format_msg()

    print(content)
    telegram_bot('电信签到任务', content)
    return content

main_handler()
