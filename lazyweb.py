def create_simple_html(title, body):
    ret_string = "<html><head><title>" + title + "</title></head><body>" + body + "</body></html>"
    return bytes(ret_string, 'utf-8')


def index(arguments):
    title = "Mainpage"
    body = "<H1>Hello from index.html</h1>\n" + str(arguments)
    return create_simple_html(title, body)


def page1(arguments):
    title = "Page 1"
    body = "<H1>Hello from Page1</h1>\n" + str(arguments)
    return create_simple_html(title, body)


URLTABLE = {
    "/": index,
    "/p1": page1
}


def parse(urlstring):
    if not urlstring:
        return dict()
    arguments = dict()
    params = urlstring.split(',')
    for p in params:
        p = p.split('=')
        try:
            arguments[p[0]] = p[1]
        except IndexError:
            continue
    return arguments


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    arguments = parse(environ['QUERY_STRING'])
    if url in URLTABLE.keys():
        return URLTABLE[url](arguments)
    else:
        start_response('404 Not found', [('Content-Type', 'text/html')])
        return b"<h1>404 Page not found</h1>"