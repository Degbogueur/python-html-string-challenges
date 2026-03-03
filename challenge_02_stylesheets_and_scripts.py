html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

stylesheet = "main.min.css"
script_file = "bundle.js"

start_css = html.find("styles.css")
end_css = start_css + len("styles.css")

html = html[:start_css] + stylesheet + html[end_css:]

start_js = html.find("app.js")
end_js = start_js + len("app.js")

html = html[:start_js] + script_file + html[end_js:]

print(html)