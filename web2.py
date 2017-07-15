
import BaseHTTPServer
import hashlib
import os
import urllib2

class CacheHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
      m = hashlib.md5()
      m.update(self.path)
      cache_filename = m.hexdigest() + ".cached"
   
      data = urllib2.urlopen("http:/" + self.path).readlines()
        
      self.send_response(200)
      self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
      self.send_header("Pragma", "no-cache")
      self.send_header("Expires", "0")
      self.wfile.writelines(data)

def run():
    server_address = ('', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, CacheHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()







