class HttpResponse():
    """
    Reads header and parses it
    GET /a/c/getNameparam0:pradeep HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n
    """

    __slots__ = ['version','status','reason_phrase','body','headers']

    # 200, 400, 401, 403, 404, 411, 500, 505
    code_and_reason = {200:"OK", 400:"Bad Request", 401:"Unauthorized", 402:"Payment Required",
     403:"Forbidden", 404:"Not Found", 405: "Method Not Allowed", 411:"Length Required",
      500:"Internal Server Error", 505:"HTTP Version not supported"}

    def __init__(self,status=200,headers=None,reason=None,body=""):
        """
        Request from client
        Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
        """
        self.version = "HTTP/1.1"
        self.set_status(status)

        if reason is None:
            reason = HttpResponse.code_and_reason[status]

        self.set_reason(reason)
        self.set_body(body)

        self.headers = {}
        if headers:
            self.set_headers(headers)

    def set_status(self,status,reason=None):
        self.status = status
        if reason:
            self.reason_phrase = reason
        return self.status

    def set_reason(self, reason):
        self.reason_phrase = reason
        return self.reason_phrase

    def set_version(self,version = "HTTP/1.1"):
        self.version = version
        return self.version

    def set_header(self, header_key, header_val):
        if header_key is not None and header_val is not None:
            self.headers[header_key] = header_val
        return self.headers

    def set_headers(self, headers):
        for key in headers:
            val = headers[key]
            self.headers[key] = val

        return self.headers


    def set_body(self, body):
        self.body = body
        return self.body

    def get_body(self):
        return self.body

    def send(self):
        """
        Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
        """
        if self.version is None or self.status is None or self.reason_phrase is None:
            raise ValueError("Can't Send Response: Version, Status and Reason phrase need to be set")

        CRLF = '\r\n'

        http_string = "%s %s %s%s"%(self.version,self.status,self.reason_phrase,CRLF)

        for key in self.headers:
                val = self.headers[key]
                http_string += "%s: %s%s"%(key,val,CRLF)
        http_string += CRLF

        if self.body:
            http_string += str(self.body)

        return str(http_string)



def ok(code=200,headers=None):
    return HttpResponse(status=code,headers=headers)

def unauthorized(code=400,headers=None):
    return HttpResponse(status=code,headers=headers)

def bad_request(code=401,headers=None):
    return HttpResponse(status=code,headers=headers)

def payment_required(code=402,headers=None):
    return HttpResponse(status=code,headers=headers)

def forbidden(code=403,headers=None):
    return HttpResponse(status=code,headers=headers)

def notfound(code=404,headers=None):
    return HttpResponse(status=code,headers=headers)

def methodnotallowed(code=405,headers=None):
    return HttpResponse(status=code,headers=headers)


def lenreqd(code=411,headers=None):
    return HttpResponse(status=code,headers=headers)

def internal_server_error(code=500,headers=None):
    return HttpResponse(status=code,headers=headers)

def version_not_supported(code=505,headers=None):
    return HttpResponse(status=code,headers=headers)





# def handle_client(connection , recvd_req , config):
    # HttpResponse(connection , recvd_req , config)

if __name__ == "__main__":
    req = "GET /a/c/getNameparam0?pradeep=1 HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n"
    sending = ok();
    print(sending)
    print(repr(sending))
