# Script to inspect current index3.html and test reading
import os

with open('index3.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Read index3.html successfully. Length: {len(content)} characters, {len(content.splitlines())} lines.")
