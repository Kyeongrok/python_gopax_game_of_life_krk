from cli import parse_file

file = open('../../plus.txt')
lines = file.readlines()
command = parse_file(lines)
print(command)
