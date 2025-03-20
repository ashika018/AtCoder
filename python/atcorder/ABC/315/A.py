import re
S = input()
pattern = '[aioue]'
result = re.sub(pattern, '', S)
print(result)