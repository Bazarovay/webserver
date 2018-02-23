class HttpParser():
    """
    Reads header and parses it
    GET /a/c/getNameparam0:pradeep HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n
    """

    __slots__ = ['request_line_array', 'request_line', 'headers','body','method']

    def __init__(self, conn, req, conf):
        """
        Request from client
        Method SP Request-URI SP HTTP-Version CRLF
        """
        CRLF = "\r\n"
        req = req.decode()
        req_array = req.split(CRLF*2)
        req = req_array[0]
        if len(req_array) > 1:
            self.body = req_array[1]
        else:
            self.body = ""

        self.request_line_array = req.split('\n')
        self.request_line = self.request_line_array[0]
        self.set_headers()
        self.set_method()

    def get_version(self):
        return self.request_line.split(' ')[-1]

    def set_method(self):
        try:
            self.method = self.request_line.split()[0]
        except:
            self.method = None
        return self.method

    def get_method(self):
        return self.method

    def get_uri(self):
        try:
            uri = self.request_line.split()[1]
        except:
            uri = None
        return uri

    def get_params(self):
        if len(self.get_uri().split("?")) > 1:
            return self.get_uri().split("?")[1]
        else:
            return ""

    def get_params_dic(self):
        try:
            params = {}
            parameters = self.get_uri().split("?")[1]
            key_val = parameters.split("&")
            for key_val in key_val:
                key = key_val.split("=")[0]
                val = key_val.split("=")[1]
                params[key] = val
        except:
            params = None
        return params

    def get_resource(self):
        return self.get_uri().split("?")[0]

    def set_headers(self):
        self.headers = {}
        for header_line in self.request_line_array[1:]:
            key_val = header_line.split(":")
            self.headers[key_val[0]] = key_val[1]

    def get_header(self, header):
        if header in self.headers:
            return self.headers[header]
        return None

    def get_host(self):
        return self.get_header("Host")

    def get_body(self):
        return self.body

    def __str__(self):
        return ('headers : %s | request_line : %s   | body : %s  | method : %s'%(str(self.headers), str(self.request_line), str(self.body), str(self.method)))


def handle_client(connection , recvd_req , config):
    Request(connection , recvd_req , config)

if __name__ == "__main__":
    req = b'GET /a/c/getNameparam0:pradeep HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n'
    me_req = HttpParser(None, req, None)
    print(me_req)
    # print(me_req.get_host());
    # print(me_req.get_params());
    # print(me_req.get_uri());
    # print(me_req.get_method());
    # print(me_req.get_version());
