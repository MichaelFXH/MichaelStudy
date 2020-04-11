import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import  requests
import  urllib
import re
from lxml import etree
import  json
import  sys
import  io
import http.cookiejar

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def set_win_center(root, curWidth='', curHight=''):
    '''
    设置窗口大小，并居中显示
    :param root:主窗体实例
    :param curWidth:窗口宽度，非必填，默认200
    :param curHight:窗口高度，非必填，默认200
    :return:无
    '''
    if not curWidth:
        '''获取窗口宽度，默认200'''
        curWidth = root.winfo_width()
    if not curHight:
        '''获取窗口高度，默认200'''
        curHight = root.winfo_height()
    # print(curWidth, curHight)

    # 获取屏幕宽度和高度
    scn_w, scn_h = root.maxsize()
    # print(scn_w, scn_h)

    # 计算中心坐标
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    # print(cen_x, cen_y)

    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
    root.geometry(size_xy)

def message_showinfo(title, info):
    top = tkinter.Tk()
    top.wm_attributes('-topmost', 1)
    top.withdraw()
    top.update()
    tip=tkinter.messagebox.showinfo(title, info)
    top.destroy()
    return  tip

def productDelete():
     print(sitenameVar.get(),spuidsVar.get())
     try:
         # url='https://viewchic.myshopify.com/admin/products/set'

         # logindata={
         #          'utf8':'✓',
         #          'authenticity_token':'mjs7zOP76K7VpjryzPO9GEIPmiluVObvzAUKHOJLD1xcj8tcHJgfSycFe0HysBCHY3bMItzLoTg4x5NyxqPFNA==',
         #          'account[email]': 'liuna@tidebuy.net',
         #          'account[password]': 'zzzsyzxljtlx1,.',
         #          'captcha-enterprise-js-loaded': '',
         #          'captcha-enterprise-js-callback': 'true',
         #          'captcha-js-erro':'',
         #          'captcha-enterprise-nonce': '458b405d-77c7-4a4e-862c-3647938d4d10',
         #          'captcha-enterprise-fetched': 'true',
         #          'commit': '',
         # }

         # post_data = urllib.parse.urlencode(logindata).encode('utf-8')
         # headersLogin = {
         #                  'authority': 'accounts.shopify.com',
         #                    'method': 'POST',
         #                    'path': '/login?rid=ad8d1fee-48c2-4c99-83ea-33eea267d4e5',
         #                    'scheme': 'https',
         #                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
         #                    'accept-encoding': 'gzip, deflate, br',
         #                    'accept-language': 'zh-CN,zh;q=0.9',
         #                    'cache-control': 'no-cache',
         #                    'content-length': '391',
         #                    'content-type': 'application/x-www-form-urlencoded',
         #                    'cookie': '__cfduid=d0eaefb8117ed710dd5d012ce8c203df91571985409; _y=01a1a95d-7DF6-4A98-8AF6-220E5B7E802A; _y=01a1a95d-7DF6-4A98-8AF6-220E5B7E802A; _shopify_y=01a1a95d-7DF6-4A98-8AF6-220E5B7E802A; _shopify_y=01a1a95d-7DF6-4A98-8AF6-220E5B7E802A; _shopify_fs=2019-10-25T06%3A36%3A38.946Z; _shopify_fs=2019-10-25T06%3A36%3A38.946Z; _gcl_au=1.1.318516835.1571997776; _ga=GA1.2.01a1a95d-7DF6-4A98-8AF6-220E5B7E802A; _mkto_trk=id:932-KRM-548&token:_mch-shopify.com-1571997776427-46609; _scid=cfcbef69-43cf-47af-8ba7-a819bec28b9f; _biz_uid=343130e9b18d40ffee48abd3725412e1; _gid=GA1.2.1607374997.1572233068; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%7D; _biz_sid=5b2d84; _shopify_s=1132ea2d-0284-420A-4BCC-20D1CBF10D43; _shopify_s=1132ea2d-0284-420A-4BCC-20D1CBF10D43; _shopify_sa_p=; _shopify_sa_p=; _s=1132ea2d-0284-420A-4BCC-20D1CBF10D43; _biz_nA=10; _biz_pendingA=%5B%5D; utag_main=v_id:016e025e76350018fdc191ee473e03072003606a009dc$_sn:4$_se:5$_ss:0$_st:1572248494201$ses_id:1572246575460%3Bexp-session$_pn:2%3Bexp-session; device_id=VGxrYzJIbmJvT0RlT2FDTDQrZnJzMVpTUlhlTlo3dU9zRVNNY25GSFpSRGtHbTlOY2hLbG5JS3YyTFdoL1FpaS0tbU5ubkUrczBoNzJpelFlS01uQmxmUT09--761c1dc29ae52641e97a64157793d8b73bf09e87; master_device_id=c91f5ed4-9168-40b7-96b8-d5a9303eb1d9; _identity_session=7b8e64029060f6e802aefde179cc00fa; __Host-_identity_session_same_site=7b8e64029060f6e802aefde179cc00fa; _shopify_sa_t=2019-10-28T07%3A21%3A15.192Z; _shopify_sa_t=2019-10-28T07%3A21%3A15.192Z',
         #                    'origin': 'null',
         #                    'pragma': 'no-cache',
         #                    'sec-fetch-mode': 'navigate',
         #                    'sec-fetch-site': 'same-origin',
         #                    'sec-fetch-user': '?1',
         #                    'upgrade-insecure-requests': '1',
         #                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
         #               }
         # login_url = 'https://accounts.shopify.com/login?rid=aabb130a-442e-4413-9a79-76b111d67789'
         # req = urllib.request.Request(login_url, headers=headersLogin, data=post_data)
         # cookie = http.cookiejar.CookieJar()
         # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
         # resp = opener.open(req)

         tokens={'https://nailcaa.myshopify.com':'WlI4ANqFOo5ZSDLwciTicKY3XJtvB3rbZGR50crvsmJA1O2iUj4sQHfbbtTvnZ2k4IBKEZextOaES3U/L4Dkrg==',
                 'https://yunjideal.myshopify.com':'3f4DRPPAUicf5u1G3U3EkVk5QehwhllDf0nZCaP55K18FbgXI1kpEGyVjs+h8TDa/O3T3/lIhukFTEje58++Nw==',
                 'https://numcroll.myshopify.com':'N/meuDlwN37hnuTTjoLRUxLZrkycKuylLvKItqujxb+NO8AcxNLn6yVIGlyQwGWM2Drt3NlfHnF5znAhcaag8A=='
                 }
         cookies={
             'https://nailcaa.myshopify.com': '_secure_admin_session_id=feaec733814235da03edd1896be69912; new_admin=1; koa.sid.sig=vjsE_zhPOhQBc7ji6vT2Uq0hMzE; koa.sid=1j3P_X7PDDMd5JLG51rdZxFIn-v1rs20; new_theme_editor_disabled.sig=c0lGzzh0MFBQ5fCQTfz7yqvtriw; new_theme_editor_disabled=1; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1T0dFM056Rm1ZeTAyTW1RMUxUUTJPVFV0WWpsaVlpMHpOVFZrTVdJeVlXSmpNamdHT2daRlJnPT0iLCJleHAiOiIyMDIxLTEwLTI4VDEzOjQ1OjAzLjcxMFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--ff6f59d44c749d3536c882a68be0f1805f185460; _landing_page=%2Fadmin%2Fauth%2Flogin; _orig_referrer=; _ab=1; __ssid=350cf5cc-5cbe-40ed-8522-ed6e20b0497d; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; __cfduid=d33ebdd5bdf482b6ac5d6259a3877d8681572270429',
             'https://yunjideal.myshopify.com': '_secure_admin_session_id=8b4eec5b7f991f8288c41283684ab47b; new_admin=1; koa.sid.sig=ErAnxvnVhw3hlQHv8GrfMac4wSM; koa.sid=8vrfEuNkP8dPxwiLotZOdA6c43ONZWEO; new_theme_editor_disabled.sig=c0lGzzh0MFBQ5fCQTfz7yqvtriw; new_theme_editor_disabled=1; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1T0dFM056Rm1ZeTAyTW1RMUxUUTJPVFV0WWpsaVlpMHpOVFZrTVdJeVlXSmpNamdHT2daRlJnPT0iLCJleHAiOiIyMDIxLTEwLTI4VDEzOjQ1OjAzLjcxMFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--ff6f59d44c749d3536c882a68be0f1805f185460; __ssid=350cf5cc-5cbe-40ed-8522-ed6e20b0497d; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; _orig_referrer=; _landing_page=%2Fadmin%2Fauth%2Flogin; _ab=1; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; __cfduid=d271f6b3b90b6e0ec8c86377c741f3e031572270887',
             'https://numcroll.myshopify.com': 'master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1T0dFM056Rm1ZeTAyTW1RMUxUUTJPVFV0WWpsaVlpMHpOVFZrTVdJeVlXSmpNamdHT2daRlJnPT0iLCJleHAiOiIyMDIxLTEwLTI4VDEzOjQ1OjAzLjcxMFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--ff6f59d44c749d3536c882a68be0f1805f185460; _secure_admin_session_id=892cfd6b4749698c4451e7fa8dd72bf9; new_admin=1; koa.sid.sig=iFzMvtKdPlh44zFG8F7kUGGChYk; koa.sid=EJ-VkTM9sNf6UOAsmMIcI2lDhWZt-2Xw; new_theme_editor_disabled.sig=c0lGzzh0MFBQ5fCQTfz7yqvtriw; new_theme_editor_disabled=1; __ssid=350cf5cc-5cbe-40ed-8522-ed6e20b0497d; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; _landing_page=%2Fadmin%2Fauth%2Flogin; _orig_referrer=; _ab=1; _y=12986ae2-0003-4504-8F50-9B827FCD4B20; _shopify_y=12986ae2-0003-4504-8F50-9B827FCD4B20; _s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_s=12986afb-C0F5-41BF-829B-C257EADC2A65; _shopify_fs=2019-10-28T13%3A39%3A51.423Z; __cfduid=d5b21c306aba052ff6355f9b0a67c5a5e1572270317'
         }
         # tokens[sitenameVar.get().rstrip()]=
         token=tokens.get(sitenameVar.get())
         cookie=cookies.get(sitenameVar.get())
         headersget = {'Content-Type':'application/json',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                      'cookie':cookie,
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'path': '/admin/products/set',
                     'x-csrf-token':token
         }

         # headerspost = {'Content-Type': 'application/json',
         #               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
         #               'cookie': 'new_admin=1; new_theme_editor_disabled.sig=c0lGzzh0MFBQ5fCQTfz7yqvtriw; new_theme_editor_disabled=1; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpTUdZd05qa3haaTFtTkRFekxUUmhNREV0T1dVek9TMHlOV0prTXpkaU9HRTBNMkVHT2daRlJnPT0iLCJleHAiOiIyMDIxLTEwLTI4VDA3OjA5OjUwLjg1NFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--2de09b2e93fdf7661c56b0d023ef9a64e93fa765; koa.sid.sig=AZ54q9QNtaSZOSRu_vObvSYiwV0; koa.sid=F6-6z24Gfal2YW3T36ZG2WYa3gW2f7dD; _secure_admin_session_id=bf17113177cd633b217ce200ede400ea; __ssid=5cb04a07-ff70-4434-a459-eb7bac3b4c91; _y=01a35c65-4779-4922-C2A0-1F0E28B8EB02; _shopify_y=01a35c65-4779-4922-C2A0-1F0E28B8EB02; _shopify_fs=2019-10-25T06%3A37%3A56.855Z; _landing_page=%2Fadmin%2Fauth%2Flogin%3Ffrom_identity%3Dtrue%26login%3Dliuna%2540tidebuy.net; _orig_referrer=; _ab=1; _y=01a35c65-4779-4922-C2A0-1F0E28B8EB02; _shopify_y=01a35c65-4779-4922-C2A0-1F0E28B8EB02; _shopify_fs=2019-10-25T06%3A37%3A56.855Z; secure_customer_sig=; cart_sig=; _ga=GA1.2.1610906003.1572233082; _gid=GA1.2.1726781829.1572233082; currency=EUR; RT="z=1&dm=myshopify.com&si=6n1tipb17vo&ss=k29uzd6k&sl=2&tt=51q&obo=1&ld=hrii&r=90807da4080dab06d1393fe26fedfedf&ul=hrik&hd=htt1"; _s=11d4d42d-FAA5-4C49-3034-1553A256636A; _s=11d4d42d-FAA5-4C49-3034-1553A256636A; _shopify_s=11d4d42d-FAA5-4C49-3034-1553A256636A; _shopify_s=11d4d42d-FAA5-4C49-3034-1553A256636A; __cfduid=d61c15678c616daef8b617f2e644d49ea1572257201',
         #               # 'x-csrf-token':'uWElHOMz-hLP9R9zkVSBhmXv8vuhhNxtcnY8',
         #                # 'origin': 'https://viewchic.myshopify.com',
         #                # 'authority': 'viewchic.myshopify.com',
         #               'sec-fetch-site': 'same-origin',
         #               'sec-fetch-mode': 'cors',
         #               'path':'/admin/products/set',
         #               }

         Orginspuids=spuidsVar.get().split(',')
         productsids={}
         for orgids in Orginspuids:
             r = requests.get(sitenameVar.get()+'/admin/products?query={0}'.format(int(orgids)), headers=headersget, timeout=20)  # 设置超时
             r.raise_for_status()
             r.encoding = r.apparent_encoding
             # resp = opener.open(r)
             html = etree.HTML(r.text)
             productshtml = html.xpath('//*[@id="all-products"]/tbody/tr/@data-bind-class')
             productid = list(set(re.findall(r'\d*', str(productshtml[0]), re.S | re.M)))[1]
             #productsids.append(productid)
             productsids[orgids]=productid

         for key,value in productsids.items():
             try:
                 json_data={"operation":"destroy","product_ids":value,"search[query]":key} #,"search[query]":key
                 r = requests.put(sitenameVar.get()+'/admin/products/set', json=json_data,headers=headersget)
                 # message_showinfo("提示", "{0}执行完成,Deleting products in the background！".format(id));
                 print(r.content)
             except Exception as e:
                 print(e)
         message_showinfo("提示", "执行完成,Deleting products in the background！");
     except Exception as e:
         message_showinfo("提示", e);


if __name__ == "__main__":
        # 第1步，实例化object，建立窗口window
        window = tk.Tk()

        # 第2步，给窗口的可视化起名字
        window.title('shopiy批量下架')

        window.resizable(False, False)
        set_win_center(window,750,300)

        # 第3步，设定窗口的大小(长 * 宽)
        # window.geometry('650x300')  # 这里的乘是小x

        # 第4步，加载 wellcome image
        # canvas = tk.Canvas(window, width=650, height=150)
        # image_file = tk.PhotoImage(file='pic.gif')
        # image = canvas.create_image(200, 0, anchor='n', image=image_file)
        # canvas.pack(side='top')
        # tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()

        # 第5步，用户信息
        tk.Label(window, text='站点:', font=('Arial', 14)).place(x=10, y=10)
        tk.Label(window, text='SPUIDS:', font=('Arial', 14)).place(x=10, y=110)

        # 第6步，用户登录输入框entry
        # 站点
        sitenameVar = tk.StringVar()
        entry_siteName = tk.Entry(window,width=50,textvariable=sitenameVar ,selectbackground='green', font=('Arial', 14))
        entry_siteName.place(x=120, y=10)

        # SPUIDS
        spuidsVar = tk.StringVar()
        entry_spuids = tk.Entry(window,textvariable=spuidsVar , width=70,font=('Arial', 14))
        entry_spuids.place(x=120, y=110)

        window.title('批量下架')
        # 第7步，login and sign up 按钮
        btn_login = tk.Button(window, text='下架',width=20, command=productDelete)
        btn_login.place(x=200, y=150)
        # 第10步，主窗口循环显示
        window.mainloop()