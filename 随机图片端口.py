from wsgiref.simple_server import make_server
from os import listdir,getcwd
from random import choice

def application(environ,start_response):
    imgList = listdir('.\\imgs')
    img = 'imgs\\' + choice(imgList)
    with open(img,'rb') as f:
        img = f.read()
    start_response('200 OK',[('Content-Type','image/jpeg')])
    body = img
    return [body]

httpd = make_server('0.0.0.0',11000,application)
print('Serving HTTP on port 11000...')
httpd.serve_forever()