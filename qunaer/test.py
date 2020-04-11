# coding:utf-8
#模拟登陆  session

import requests

def start_getSession():
    session_=requests.session()
    return  session_

def getBaseCookie(session_):
    session_.get('http://user.qunar.com/passport/login.jsp')
    getImg(session_)

def getImg(session_):
   response= session_.get('https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a')
   with open('code.png','wb') as f:
       f.write(response.content)

def login(session_,username,passwd,_code):
    data={
        "oginType": 0,
        "username": username,
        "password": passwd,
        "remember": 1,
        "vcode": _code
    }
    response=session_.post('https://user.qunar.com/passport/loginx.jsp',data=data)
    print(response.text)

if __name__ == '__main__':
    session=start_getSession()
    getBaseCookie(session)
    #getImg(session)
    username=input('请输入用户名')
    passwd=input('请输入密码')
    _code=input('请输入验证码')
    login(session,username,passwd,_code)