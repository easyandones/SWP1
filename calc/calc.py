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
        response_body = html+'<br><br><br>[Add] : '+str(a)+' + '+str(b)+' = '+str(add)+'<br><br>[Multiply] : '+str(a)+' * '+str(b)+' = '+str(multiply)
    else:
        response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]