with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the HTML entity encoding bug
# The file currently has literal < and > (single characters) in the replacement strings
# It should have HTML entities < and > (4-character strings)
old = '${md.replace(/</g, "<").replace(/>/g, ">")}'
# In the JavaScript, we need the string "<" and ">" (the HTML entities)
new = '${md.replace(/</g, "<").replace(/>/g, ">")}'
content = content.replace(old, new)

with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')