import urllib.request
import urllib.parse
import sys
try:
    arr=sys.argv[1:]
    if(len(sys.argv[1:])==0):
        temp=open('input.txt','r')
        a=temp.readlines()
        arr=[i.rstrip() for i in a]
        temp.close()
        
    for url in arr:
        first="http://tinyurl.com/api-create.php?"
        last=urllib.parse.urlencode({'url':url})
        last=last.encode('utf-8')
        req=urllib.request.Request(first,last)
        resp=urllib.request.urlopen(req)
        respData=resp.read()
        respData=respData.decode('utf-8')
        print(respData)
        savefile=open('output.txt','a+')
        savefile.write(respData+'\n')
        savefile.close()
except Exception as e:
    print(e)


