import re
import sys

text = sys.stdin.read().strip()
words = re.findall(r'\b\w{3}\b', text)
print(len(words))