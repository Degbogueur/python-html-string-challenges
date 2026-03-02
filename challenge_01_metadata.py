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

page_title = "My Awesome Portfolio"
page_lang = "fr"

html = html.replace("My Page", page_title)
html = html.replace('lang="en"', f'lang="{page_lang}"')

print(html)

# Advanced Extension Explanation:
# The third argument in .replace() limits how many replacements occur.
# This is important because in large HTML documents, the same substring
# may appear multiple times (for example, multiple titles, scripts, or repeated text).
# Limiting replacements prevents accidentally modifying content you didn't intend to change.

# html = html.replace("My Page", page_title, 1)
# html = html.replace('lang="en"', f'lang="{page_lang}"', 1)