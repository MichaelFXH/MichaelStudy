# coding:utf-8
import  requests
import  json
import  math
import  random
import  re
import  sys
from contextlib import  closing

def start_getSession():
    session_=requests.session()
    return  session_

def getFileList(session_,code,dirID):
    hd = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'protected_uid=372195564528; pass_d37296516={0}'.format(code),
        'Host': 'webapi.ctfile.com',
        'Origin': 'https://72k.us',
        'Pragma': 'no-cache',
        'Referer': 'https://72k.us/dir/'+str(dirID),
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    url='https://webapi.ctfile.com/getdir.php?d={0}&folder_id=&passcode={1}&r={2}&ref='.format(str(dirID),code,random.random())
    r = session_.get(url, headers=hd)
    dirContent=json.loads(r.text.encode('UTF-8'))
    userid=dirContent["userid"]
    folder_id=dirContent["folder_id"]
    file_chk=dirContent["file_chk"]
    folder_name=dirContent["folder_name"]
    url=dirContent["url"]
    return  userid,folder_id,file_chk,folder_name,url,hd

def getFile(session_,code,dirID):
    userid, folder_id, file_chk, folder_name, url,hd=getFileList(session, code,dirID)
    r = session_.get('https://webapi.ctfile.com/'+url)
    fileData=json.loads(r.text)
    for item in fileData["aaData"]:
        filere=r'value="(.*)(\d)+"(\s)?(\w).*?'
        #fileid=re.compile(filere, re.S).search(str(item)).group(1)
        fileName = re.compile(r'(.*)<a(.*?)>(.*?)</a>', re.S).search(str(item)).group(3)
        tempdir=re.compile(r'(.*?)href=(.*?)>', re.S).search(str(item)).group(2).replace('/file/','').replace('\"','')
        userid,fileid,filechk,filesize=getFileChk(session_,tempdir,dirID)
        fileName,downurl=GetdownUrl(session_,userid,fileid,folder_id,filechk,0,0,1,'',fileName)
        downLoadFile(session,downurl, fileName,filesize)

def GetdownUrl(session_,uid,fid,folderid,filechk,mb,app,acheck,verifycode,fileName):
    url='https://webapi.ctfile.com/get_file_url.php?uid={0}&fid={1}&folder_id={2}&file_chk={3}' \
        '&mb={4}&app={5}&acheck={6}&verifycode={7}&rd={8}'.\
        format(uid,fid,0,filechk,mb,app,acheck,verifycode,random.random())
    response=session_.get(url)
    downurl=json.loads(response.text)["downurl"]
    return  fileName,downurl

def downLoadFile(session_,url,fileName,filesize):
    print('正在下载文件：D:\\{}'.format(fileName))
    with closing(requests.get(url, stream=True)) as data:
        data_count = 0
        filesize = int(data.headers["Content-Length"])
        with open("D:\\{}.rar".format(fileName), "wb") as file:
            for chunk in data.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    data_count = data_count + len(chunk)
                    now_jd = (data_count / filesize) * 100
                    print("\r文件下载进度：%s===========(已下载：%d/总大小：%d)" % (str(int(now_jd))+'%', data_count, filesize), end=" ")

def getFileChk(session_,tempdir,dirID):
    hd={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'webapi.ctfile.com',
        'Origin': 'https://72k.us',
        'Pragma': 'no-cache',
        'Referer': 'https://72k.us/file/{}'.format(tempdir),
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    # 获取文件的chk
    chkurl = 'https://webapi.ctfile.com/getfile.php?f={0}&passcode={1}&r={2}&ref={3}'.format(
        tempdir, '', random.random(), 'https://72k.us/dir/{}'.format(dirID))
    # chkurl='https://webapi.ctfile.com/getfile.php?f=tempdir-BmVTZldkXTAFNgBjUGlTM1N8V2JTYAw-DWdVN1EyBzsFbFFvVHsNZFBnAW5TZ1w9UWpTYgY0Dz8Bbw&passcode=&r=0.9253514497517294&ref=https%3A//72k.us/dir/22151482-37296516-161d43'
    response = session_.get(chkurl,headers=hd)
    data=json.loads(response.text)
    return  data["userid"],data["file_id"] ,data["file_chk"],data["file_size"]

if __name__ == '__main__':
    try:
        print('PS：https://72k.us/dir/22151482-37296516-161d43!')
        sys.stdout.write('文件ID为：22151482-37296516-161d43\n\n')
        session=start_getSession()
        dirID=input('请输入文件ID(默认值：22151482-37296516-161d43)：')
        code=input('请输入提取码(默认值：bozhilu)：')
        if(dirID.strip()==''):
            dirID='22151482-37296516-161d43'
        if(code.strip()==''):
            code='bozhilu'
        getFile(session,code,dirID)
        #22151482-37296516-161d43
        #bozhilu
    except:
        print('请关闭重新运行！')
        input('')