html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: black;
}

h1 {
    color: white;
}

h4 {
    color: grey;
}
</style>
</head>
<body>
    <h1>Hello from containerized web app</h1>
    <h4>Created by Kartik Sharma.</h4>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_template)
    while True:
        pass
