# Web-Cache-Server
An  HTTP server that works as web cache

Implemented a web cache server. An HTTP server that works as web cache. When it
receives a request, it check if the document is in its cache, then it serves the document providing the cache
validity time with 'max-age' options along with additional header 'Age' indicating how long the cache server
has cached it. If the document is not in the cache, then it fetches it from the actual web server URL and stores it
in the cache and also serve the request.
./server-asn1.py -n <num of cache objects> -p <server port number>

Note: Please configure browser with proxy setting to test your web server.
