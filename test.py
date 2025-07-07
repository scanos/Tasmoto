
#!/usr/bin/env python3
def application(environ, start_response):
    status = '200 OK'
    output = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Python</title>
</head>
<body>
    <h1>Hello from Python!</h1>
    <p>This is the default index.py page served by Apache using WSGI.</p>
</body>
</html>
""".encode('utf-8')
    response_headers = [('Content-type', 'text/html'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
