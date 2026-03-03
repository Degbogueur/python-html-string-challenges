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

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

body_content = f"    <h1>{h1}</h1>\n    <h2>{h2}</h2>\n    <h3>{h3}</h3>"

parts = html.split("<body>")

html = parts[0] + "<body>\n" + body_content + parts[1]

print(html)