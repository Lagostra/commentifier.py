import sys


def find_indent(lines, index):
    while len(lines[index]) == len(lines[index].lstrip()):
        index += 1

    if lines[index].lstrip().startswith('"""'):
        return False

    return lines[index][:len(lines[index]) - len(lines[index].lstrip())]

if len(sys.argv) < 2:
    print()

lines = None
with open(sys.argv[1], 'r') as file:
    lines = [x.strip('\n') for x in file]

    i = 0
    while i < len(lines):
        index = lines[i].find('def ')
        if index != -1:
            function_name = lines[i][index + 3:lines[i].index('(')].strip()
            function_name = ' '.join(function_name.split('_'))

            indent = find_indent(lines, i + 1)

            if not indent:
                i += 1
                continue

            lines.insert(i+1, indent + '"""')
            lines.insert(i+2, indent + function_name.capitalize())
            lines.insert(i+3, indent + '"""')
            i += 3

        index = lines[i].find('class ')

        if index != -1:
            i2 = lines[i].find('(')
            i2 = i2 if i2 != -1 else lines[i].find(':')
            class_name = lines[i][index + 5:i2].strip()

            indent = find_indent(lines, i + 1)

            if not indent:
                i += 1
                continue

            lines.insert(i + 1, indent + '"""')
            lines.insert(i + 2, indent + class_name + ' Class')
            lines.insert(i + 3, indent + '"""')
            i += 3

        i += 1

with open(sys.argv[1], 'w') as file:
    file.write('\n'.join(lines) + '\n')