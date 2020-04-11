import requests
import  re
import  json
import  threading

hd = {
    'Connection': 'keep-alive',
    'Host': 'upos-hz-mirrorkodo.acgvideo.com:443',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'cookie':'DICT_FORCE=true; OUTFOX_SEARCH_USER_ID_NCOO=836725316.3225262; OUTFOX_SEARCH_USER_ID="-1521503064@10.108.160.19"; NTES_YD_SESS=CR8VAWoAl.7ITYA_c0zUOIncXhXVkTkBe01jxL_Ux5S2JYRBJ0rMWQ0nyP_Krb9TNijf48HVoClgSvMcTMBjzZx5jLSxM1OZJcVvVUqFPzdrvrYwTuYfbMAumaXALLsXLskLsKoWb2tAE2UYRd_RKkObPSy5sUgJ026PaWLkmFLjoityVCf.sOs.laTh1nWSKg2T1xj.mVSLRcibQZy3OWu8mftY1_JOQljOPuoxclhHf; P_INFO=13311159232|1583762083|1|youdaodict|00&99|null&null&null#bej&null#10#0|&0|null|13311159232; DICT_SESS=v2|RzkOIzv8yVOfOMlGn4pz0pukLqFO4T40gLhHqZ0fTFRQKO4Pu6LkY0pynfeukfPy0wZ0MTBhfeL0ez64zfOfeBRYMOfqBOMTz0; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1583762084288||221.216.139.44||urs-phoneyd.6d1be61cd06b49369@163.com||UGhLJLnfgz0gFhLwz0MYM0z5OMYAOLwL0qyRHwZ6MpyRquhMzMn4lY0kMkMJynLkm0gLhMzY64eFRPu0HOEh46B0; DICT_LOGIN=3||1583762084300; xuetangvendor=zhihuiyun; keoutvendor=; ke_Pdt=CourseWeb; UM_distinctid=170bf99eb341a4-0c486a33575ee1-33365801-100200-170bf99eb355f0; davisit=1; __da_ntes_utmz=255406226.1583762500.1.1.; __da_ntes_utmfc=; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1583762500,1583842923; ke_inLoc=; ___rl__test__cookies=1584107104831; CNZZDATA1253417976=1135604278-1583757410-https%253A%252F%252Fke.youdao.com%252F%7C1584152631; __da_ntes_utma=255406226.1434767694.1583762500.1584107107.1584154930.9; __da_ntes_utmb=255406226.2.10.1584154930; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1584154942',
    'Referer':'https://ke.youdao.com/user/mycourse?loginBack=true&Pdt=CourseWeb',
    'Sec-Fetch-User': '?1',
     'Upgrade-Insecure-Requests':'1',
     'Sec-Fetch-Site': 'same-origin',
     'Host': 'ke.youdao.com'
}


hd1 = {
 'Accept': '*/*',
 'Accept-Encoding': 'identity;q=1, *;q=0',
 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'stream.ydstatic.com',
    'Range': 'bytes=0-',
    # 'Referer': 'https://live.youdao.com/live/index.html?courseId=27500&lesson=1715110&type=1',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

# url = 'https://ke.youdao.com/course/detail/27500?loginBack=true&Pdt=CourseWeb'
# r = requests.get(url, headers=hd)
#
# result=re.search('window.lesson(.*?)];',r.text,re.S)
# result=result.group(0).replace(';','').replace('window.lesson =','')
# jsonCourse=json.loads(result)

# for levels in jsonCourse: #课程表  痴学社
#     print("课程分类{0}".format(levels["title"]))
#     for item in levels["list"]:
#         print("阶段：{}标题{}".format(item["level"],item["title"]))
#         for course in item["list"]:
#             if(course.get("liveId")!=None):
#                print("id:{}课程id:{}课程名称:{}".format(course["id"],course["liveId"],course["title"]))
#                url="https://live.youdao.com/live/index.html?courseId={}&lesson={}&liveId={}&groupId=18828&token=86293".format("27500",course["id"],course["liveId"])
#             else:
#                print("id:{}课程名称:{}".format(course["id"], course["title"]))
#                url = ""

sess=requests.session()

url='https://ke.youdao.com/course/live/lessons.json?courseId=27500&r=1583768329386'
r = sess.get(url, headers=hd)
jsonCourse=json.loads(r.text)

i=0
downLoadDict={}
for levels in jsonCourse["data"]: #课程表  痴学社
    # print("课程分类{0}".format(levels["title"]))
    for item in levels["list"]:
        i=i+1
        # print("阶段：{}标题{}".format(item["level"],item["title"]))
        if(item.get("liveId")!=None):
            # print("id:{}课程id:{}课程名称:{}".format(item["id"],item["liveId"],item["title"]))
            url="https://live.youdao.com/live/index.html?courseId={}&lesson={}&liveId={}&groupId=18828&token=86293".format("27500",item["id"],item["liveId"])
        else:
             # print("id:{}课程名称:{}".format(item["id"], item["title"]))
             url = "https://live.youdao.com/live/index.html?courseId={}&lesson={}&type=1".format(
                 "27500", item["id"])
        # print("第{}个,id:{}课程名称:{}".format(i,item["id"], item["title"]))
        # print(url)
        # print(item["video"]["downloadUrl"])
        if(i<71):
            continue
        hd1["Referer"] = url
        print('下载第{}个'.format(i))
        video = sess.get(item["video"]["downloadUrl"], headers=hd1)
        with open("D:\\逻辑英语\\{}.mp4".format(str(i)+"."+ item["title"].replace('：','').replace('"','')), "wb") as mp4:
            for chunk in video.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

print('下载完成！')
# if __name__ == '__main__':
#     for key,value in downLoadDict.items():
#         hd1["Referer"]=key
#         video = requests.get(value,headers=hd1)
#         with open('test.mp4', "wb") as mp4:
#             for chunk in video.iter_content(chunk_size=1024 * 1024):
#                 if chunk:
#                     mp4.write(chunk)
