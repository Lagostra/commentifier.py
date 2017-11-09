import sys

if len(sys.argv) < 2:
    print()

lines = None
with open(sys.argv[1], 'r') as file:
    lines = [x.strip('\n') for x in file]

    i = 0
    while i < len(lines):
        index = lines[i].find('def')
        if index != -1:
            function_name = lines[i][index + 3:lines[i].index('(')].strip()
            function_name = ' '.join(function_name.split('_'))

            indent = lines[i+1][:len(lines[i+1]) - len(lines[i+1].lstrip())]

            lines.insert(i+1, indent + '"""')
            lines.insert(i+2, indent + function_name.capitalize())
            lines.insert(i+3, indent + '"""')
            i += 3
        i += 1

with open(sys.argv[1], 'w') as file:
    file.write('\n'.join(lines) + '\n')