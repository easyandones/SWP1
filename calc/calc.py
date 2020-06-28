from cgi import parse_qs
from calc_template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if '' not in [a, b]:
        a, b = int(a), int(b)
        add = a + b
        multiply = a * b
        result = "<p style=\"color:red;\">[Add] : %(a)d + %(b)d = %(add)d<br><br>[Multiply] : %(a)d * %(b)d = %(multiply)d</p>"%{'a':a, 'b':b, 'add':add, 'multiply':multiply}
    else:
        result = "<p style=\"font-style:italic; color:gray;\">No Result</p>"
    response_body = html%{'result':result}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]