import re

pattern = r'Life'
script = 'Life is so cool'
re.match(pattern, script)
print(re.match(pattern, script).group())


def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')


pattern = r'is'
refinder(pattern, script)

print(re.search(pattern, script).group())

print(re.search(r'Life', script).group())
print(re.search(r'cool', script).group())

number = 'My number is 511223-1******* and yours is 521012-2******'
print(re.findall('\d{6}', number))
