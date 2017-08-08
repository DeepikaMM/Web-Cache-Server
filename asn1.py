from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#import requests
import time,os,stat
import urllib2
import string
import re

class Local_Cache_Manager(BaseHTTPRequestHandler):
    #handling GET command
    def do_GET(self):
    
      try:
        print self.path
        strg = self.path
        a1, a2, a3 = strg.split('.')
        pathname = a2 + ".html"
        if os.path.exists(pathname):
            present=time.time()
            fileCreation = os.path.getctime(pathname)
            max_age=fileCreation+86400 #1 day
            if(present>max_age):
                print "File exceeded Max Age"
                os.remove(pathname)

        if os.path.exists(pathname):
            fileCreation = os.path.getctime(pathname)
            #print fileCreation
            now = time.time()
            #print 'Age:' 
            Age=now-fileCreation
            print "Age:" ,Age
            print "Cache found for the requested URL [CACHE HIT]"
            data = open(pathname).readlines()
        
        else:
            print "Requested URL not in cache [CACHE MISS]"
            data = urllib2.urlopen("http:/" + self.path).readlines()
            open(pathname, 'wb').writelines(data)
        self.send_response(200)
        print "Request successful"
        print "_________________________________________________________________________________________"

        self.send_header("Cache-Control", "public,max-age=86400")
        self.send_header("Expires", "-1")
        self.send_header("Content-type", "text/html")
        
        self.end_headers()

        self.wfile.writelines(data)
        return

      except IOError:
        self.send_error(404,'There was an error')

def main():
  try:
    #print('http server is starting...............')
    server_address = ('127.0.0.1', 8000)
    handler_class=Local_Cache_Manager
    httpd = HTTPServer(server_address, handler_class)
    print('http server is running.........')
    httpd.serve_forever()
      
  except KeyboardInterrupt:
    print '^C received, shutting down server'
    

if __name__ == '__main__':
    main()







