from webob import Request,Response,dec,exc
from wsgiref.simple_server import make_server
import  re

class Router:
    def __init__(self,prefix:str=''):
       self.__prefix=prefix.rstrip('/\\')
       self.__routetable=[]

    @property
    def prefix(self):
        return self.__prefix

    def route(self,pattern,*methods):
        def wraper(handler):
            self.__routetable.append((methods,re.compile(pattern),handler))
            return  handler
        return  wraper

    def get(self,pattern):
        return  self.route(pattern,'GET')
    def post(self,pattern):
        return  self.route(pattern,'POST')

    def match(self,request:Request)->Response:
        if not request.path.startswith(self.prefix):
            return
        for methods,pattern,handler in self.__routetable:
            if not methods or request.method.upper() in methods:
                matcher=pattern.match(request.path).replace(self.prefix)
                if matcher:
                    request.args=matcher.group()
                    request.kwargs=matcher.groupdict()
                    return  handler(request)

class Application:
    ROUTES=[]

    @classmethod
    def register(cls,router:Router):
        cls.ROUTES.append(router)

    @dec.wsgify
    def __call__(self,request:Request) ->Response:
        for router in self.ROUTES:
            response=router.match(request)
            if response:
                return  response
        raise exc.HTTPNotFound("您访问的页面不存在")

idx=Router()
py=Router('/python')
Application.register(idx)
Application.register(py)


@idx.get('^/index')
def index(request:Request):
    res=Response()
    res.body="hello how are you".encode()
    return  res

@py.post('^/python')
def showPython(request:Request):
    res=Response()
    res.body="hello Python".encode()
    return  res

if __name__ == '__main__':
    ip='127.0.0.1'
    port=9999
    server=make_server(ip,port,Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
