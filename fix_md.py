with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the HTML entity encoding bug - the current code has literal < and > in the replace
# which doesn't escape anything. It should escape to HTML entities < and >
old = '${md.replace(/</g, "<").replace(/>/g, ">")}'
new = '${md.replace(/</g, "<").replace(/>/g, ">")}'
content = content.replace(old, new)

with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')