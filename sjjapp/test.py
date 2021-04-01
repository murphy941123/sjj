# import json
# import requests
#
# params={"userId":"0391e032b77d48a490859b9ceebdcbb9","url":"coupon/couponlist",'pageNum':20,'offset':1,'type':0,}
# r=requests.get(url="http://muser.ssports.iqiyi.com/api/jsonp/pf?",params=params)
# re=json.loads(json.dumps(r.text))
# print(re)
# res=str(re).replace('callback(','').replace(')','')
# a=json.loads(res)
# print(a["resCode"])
# import random
#
#
# province=['北京市','天津市','河北省','山西省',]
# print(random.choice(province))
import requests

url='https://app-daily.xdfsjj.com/userservice/login.do'
params={'mobile':18500963075,'pwd':'chd1588459','loginType':4,'_appid':8,'appType':5}
re=requests.post(url=url,params=params)
print(re.json())
