class HttpRequest():
    """
    Reads header and parses it
    GET /a/c/getNameparam0:pradeep HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n
    """

    __slots__ = ['method','headers','uri', 'host','version','params']
    GET = "GET"

    def __init__(self,method=GET,headers=None,params=None,uri=None):
        """
        Request from client
        Method SP Request-URI SP HTTP-Version CRLF
        """
        self.method = method
        self.host = "localhost:8080"
        self.headers = {}
        self.headers["Host"] = self.host
        self.params = ""
        self.set_version()

        self.set_uri(uri)

        if headers:
            self.set_header(headrs)

        if params:
            self.set_params(params)

    def send(self):
        """
        Method SP Request-URI SP HTTP-Version CRLF
        """
        if self.method is None or self.host is None or self.uri is None:
            raise ValueError("Can't Send Request: Method, Host and Resource need to be set")

        CRLF = '\r\n'

        http_string = "%s %s %s%s"%(self.method,self.uri+self.params,self.version,CRLF)
        http_string += "%s: %s%s"%("Host",self.host,CRLF)

        for key in self.headers:
            if key!= "Host":
                val = self.headers[key]
                http_string += "%s: %s%s"%(key,val,CRLF)
        http_string += CRLF

        return http_string

    def set_method(self, method):
        self.method = method
        return self.method

    def set_uri(self, uri):
        self.uri = uri
        return self.uri

    def set_version(self,version = "HTTP/1.1"):
        self.version = version
        return self.version

    def set_headers(self, headers):
        self.headers = {}
        for key in headers:
            val = headers[key]
            self.headers[key] = val

        return self.headers

    def set_host(self, host):
        self.host = host
        return self.host

    def set_body(self, body):
        self.body = body
        return self.body

    def set_params(self, params):
        params_str = "?"
        for key, val in params:
            params_str += "%s=%s&"%(key,val)

        self.params = params_str[:-1]
        # if self.get_uri:
            # self.get_uri += self.params

        return self.params


if __name__ == "__main__":
    req = "GET /a/c/getNameparam0?pradeep=1 HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n"
    res = HttpRequest(method="GET",uri="www.facebook.com");
    sending = res.send()
    print(sending)
    print(repr(sending))
