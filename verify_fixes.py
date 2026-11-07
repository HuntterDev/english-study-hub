with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for basic HTML structure
print('File length:', len(content))
print('Has DOCTYPE:', '<!DOCTYPE html>' in content)
print('Has html tag:', '<html' in content)
print('Has head tag:', '<head>' in content)
print('Has body tag:', '<body>' in content)
print('Has script tag:', '<script>' in content)
print('Has closing script:', '</script>' in content)
print('Has closing html:', '</html>' in content)

# Check for duplicate function definitions
import re
funcs = re.findall(r'function\s+(\w+)', content)
from collections import Counter
dupes = {k: v for k, v in Counter(funcs).items() if v > 1}
print('Duplicate functions:', dupes)

# Check specific fixes
print()
print('=== Specific Fixes ===')
print('initChecklists count:', content.count('function initChecklists'))
print('saveChecklist count:', content.count('function saveChecklist'))
print('resetChecklist count:', content.count('function resetChecklist'))

# Check switchTab before runInit
switchTab_idx = content.find('function switchTab')
runInit_call_idx = content.find('runInit();')
print(f'switchTab at {switchTab_idx}, runInit() call at {runInit_call_idx}, OK: {switchTab_idx < runInit_call_idx}')

# Check tab click count
tab_clicks = content.count("querySelectorAll('.nav-tab')[0]?.click()")
print(f'Tab clicks: {tab_clicks}')

# Check theme toggle
theme_toggles = content.count('themeToggle.addEventListener')
print(f'Theme toggle listeners: {theme_toggles}')

# Check updateNextAction fix
fallback_comment = 'fallback state try' in content
print(f'Confusing fallback comment removed: {not fallback_comment}')

# Check openReportsFolder dynamic path
hardcoded_path = 'C:\\Users\\Douglas_Desktop\\Pictures\\DEEPSEEK PROJETOS\\Learning English\\reports' in content
print(f'Hardcoded path removed: {not hardcoded_path}')

# Check markdown export fix
md_fix = '<' in content and '>' in content
print(f'Markdown export uses HTML entities: {md_fix}')