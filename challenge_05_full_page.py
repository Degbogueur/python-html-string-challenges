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

# Step 1
html = html.replace('lang="en"', 'lang="es"', 1)
html = html.replace("My Page", "Full Page Challenge", 1)

# Step 2
# Replace stylesheet
start_css = html.find("styles.css")
end_css = start_css + len("styles.css")
html = html[:start_css] + "app.min.css" + html[end_css:]

# Replace script
start_js = html.find("app.js")
end_js = start_js + len("app.js")
html = html[:start_js] + "main.bundle.js" + html[end_js:]

# Step 3
css_count = html.count("styles.css")
js_count = html.count("app.js")

if css_count == 0 and js_count == 0:
    print("Asset replacement successful.")
else:
    if css_count > 0:
        print("Error: styles.css was not fully replaced.")
    if js_count > 0:
        print("Error: app.js was not fully replaced.")

# Step 4
h1 = "Welcome to the Full Page"
h2 = "Building with String Methods"
h3 = "Final Assembly Step"

body_content = (
    f"    <h1>{h1}</h1>\n"
    f"    <h2>{h2}</h2>\n"
    f"    <h3>{h3}</h3>\n"
)

parts = html.split("<body>", 1)
html = parts[0] + "<body>\n" + body_content + parts[1]

# Step 5
paragraph_text = "This entire page was generated using only Python string methods."
img_src = "hero.jpg"
img_alt = "Hero image"

p_tag = "    <p>" + paragraph_text + "</p>\n"
img_tag = "    <img src=\"" + img_src + "\" alt=\"" + img_alt + "\">\n"

pos_h1 = html.rfind("</h1>")
pos_h2 = html.rfind("</h2>")
pos_h3 = html.rfind("</h3>")

last_pos = max(pos_h1, pos_h2, pos_h3)

if last_pos == pos_h1:
    closing_tag = "</h1>"
elif last_pos == pos_h2:
    closing_tag = "</h2>"
else:
    closing_tag = "</h3>"

insert_index = last_pos + len(closing_tag)

html = html[:insert_index] + "\n" + p_tag + img_tag + html[insert_index:]

# Step 6
title_start = html.find("<title>") + len("<title>")
title_end = html.find("</title>")
title_text = html[title_start:title_end]

second_paragraph = (
    "    <p>This page is titled: " + title_text + "</p>\n"
)

body_close_index = html.find("</body>")
html = html[:body_close_index] + second_paragraph + html[body_close_index:]

# Step 7
print("\n--- Validation Report ---")

print("✅ <title> is correct" if html.count("<title>Full Page Challenge</title>") == 1 else "❌ <title> incorrect")

print("✅ <h1> found" if html.count("<h1>") == 1 else "❌ <h1> missing")
print("✅ <h2> found" if html.count("<h2>") == 1 else "❌ <h2> missing")
print("✅ <h3> found" if html.count("<h3>") == 1 else "❌ <h3> missing")

print("✅ <img> appears exactly once" if html.count("<img") == 1 else "❌ <img> count incorrect")
print("✅ <p> appears exactly twice" if html.count("<p>") == 2 else "❌ <p> count incorrect")

print("✅ Starts with <!DOCTYPE html>" if html.startswith("<!DOCTYPE html>") else "❌ Incorrect start")

print("✅ Ends with </html>" if html.strip().endswith("</html>") else "❌ Incorrect ending")

print("-------------------------\n")

# Step 8
print(html)