import httpx 
import json
import base64
from random import choice

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"]
  
headers = {}

def get_url():
    email="" #email
    key="" #key
    targetsrting='app="宝塔Windows面板-Windows版" && port="888" && country="US"'
    target=base64.b64encode(targetsrting.encode('utf-8')).decode("utf-8")
    pages=1 #翻页数
    size="100" #每页返回记录数
    #print(url)
    for page in range(pages):
        page = page+1
        url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+target+"&size="+size+"&page="+str(page)
        print(url)
        resp = httpx.get(url)
        data_model = json.loads(resp.text)

        data_url=[]
        for i in data_model['results']: #取结果列表
            for j in i[0:1]: #取结果列表中的每个列表的url,需要IP则改为[1:2]
                data_url.append(j)
    save=open('fofaurl.txt','w+')
    for i in data_url:
        save.write(i+"\n")
    save.close()

def check_url():
    with open('fofaurl.txt','r') as f:
        all_url = f.readlines()
    for url in all_url:
        headers["User-Agent"] = choice(user_agents)
        url = 'http://'+url.strip('\n')+'/pma'
        print ('check:',url)
        try:
            res = httpx.get(url=url,timeout=0.1,headers=headers)
            if res.status_code != 404:
                print('[+]Get Available:'+url)
        except:
            pass
def main():
    get_url()
    check_url()
    
if __name__ == '__main__':
    main()