try:
       import sys
       try:
              import requests
       except ImportError:
              print("requests package absent")
              sys.exit()
       
       try:
              sys.argv[1]
       except:
              print("No wordlist entered")
              sys.exit()

       if len(sys.argv)!=2:
              print("Syntax: python neocities.py words.txt")
              sys.exit()

       try:
              f=open(sys.argv[1])
       except FileNotFoundError:
              print("File not found")
              sys.exit()

       for i in (f.read()).split():
                     req=requests.get("https://"+i+".neocities.org")
                     if req.status_code==404:
                         print(i)
                         with open(sys.argv[1]+'_result','a+') as fr:
                                fr.write(i+'\n')
       f.close()

except KeyboardInterrupt:
       print("Exiting...")
       sys.exit()
