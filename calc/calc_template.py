html = b"""
<html>
    <head>
        <title>WSGI SCRIPT CALCULATOR</title>
    </head>
    <body>
        <h1>CALCULATOR</h1>
        <form action="">
            a = <input type="number" name="a"><br><br>b = <input type="number" name="b">
            <br><br><input type="submit"><br><br>
        </form>
        <h2>RESULT</h2>
        %(result)s
    </body>
</html>
"""