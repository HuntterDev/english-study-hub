with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all localStorage calls with safe versions
replacements = [
    # setItem
    ("localStorage.setItem('theme', newTheme);", "safeSetItem('theme', newTheme);"),
    ("localStorage.setItem('checklist-' + item.dataset.day, isDone);", "safeSetItem('checklist-' + item.dataset.day, isDone);"),
    ("localStorage.setItem('metrics-history', JSON.stringify(history));", "safeSetItem('metrics-history', JSON.stringify(history));"),
    ("localStorage.setItem('self-assessment-history', JSON.stringify(history));", "safeSetItem('self-assessment-history', JSON.stringify(history));"),
    ("localStorage.setItem(`phase-${phase}-${item.dataset.gate}`, item.classList.contains('done'));", "safeSetItem(`phase-${phase}-${item.dataset.gate}`, item.classList.contains('done'));"),
    ("localStorage.setItem('gate-log-history', JSON.stringify(history));", "safeSetItem('gate-log-history', JSON.stringify(history));"),
    ("localStorage.setItem('report-counter', reportCounter.toString());", "safeSetItem('report-counter', reportCounter.toString());"),
    
    # getItem
    ("localStorage.getItem('theme')", "safeGetItem('theme')"),
    ("localStorage.getItem('checklist-' + item.dataset.day)", "safeGetItem('checklist-' + item.dataset.day)"),
    ("localStorage.getItem('metrics-history')", "safeGetItem('metrics-history')"),
    ("localStorage.getItem('self-assessment-history')", "safeGetItem('self-assessment-history')"),
    ("localStorage.getItem(`phase-${phase}-${item.dataset.gate}`)", "safeGetItem(`phase-${phase}-${item.dataset.gate}`)"),
    ("localStorage.getItem('gate-log-history')", "safeGetItem('gate-log-history')"),
    ("localStorage.getItem('checklist-' + dayKey)", "safeGetItem('checklist-' + dayKey)"),
    ("localStorage.getItem('anki-total-cards')", "safeGetItem('anki-total-cards')"),
    ("localStorage.getItem('checklist-' + yesterdayKey)", "safeGetItem('checklist-' + yesterdayKey)"),
    ("localStorage.getItem('checklist-' + day)", "safeGetItem('checklist-' + day)"),
    ("localStorage.getItem('report-counter')", "safeGetItem('report-counter')"),
    
    # removeItem
    ("localStorage.removeItem('checklist-' + item.dataset.day);", "safeRemoveItem('checklist-' + item.dataset.day);"),
    ("localStorage.removeItem(`phase-${phase}-${item.dataset.gate}`);", "safeRemoveItem(`phase-${phase}-${item.dataset.gate}`);"),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(r'C:\Users\Douglas_Desktop\Pictures\DEEPSEEK PROJETOS\Learning English\english-study-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')