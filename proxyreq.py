import urllib.request
import requests



def urllibproxy():
    a = urllib.request.ProxyHandler({"http": "109.62.181.230:8080"})
    opener = urllib.request.build_opener(a)
    urllib.request.install_opener(opener)
    
    req = urllib.request.urlopen("https://50321a5f.ngrok.io")
    print(req.status)
    print(req.read())




def proxyreq():
    req = requests.get("https://5d902545.ngrok.io", proxies={"http": "109.62.181.230:8080"})
    print(req.content.decode())

proxyreq()