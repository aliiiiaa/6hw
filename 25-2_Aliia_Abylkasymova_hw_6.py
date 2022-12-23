import re
while True:
    with open('MOCK_DATA.txt', 'r') as file:
        info = file.read()
        name = re.findall(r"[A-Z][a-z-]+\s+[A-Za-d][A-Za-z- O']+", info)
        emails = re.findall(r'[a-z0-9]+@[a-z.0-9-]+', info)
        files = re.findall(r'[A-Za-z]+[A-Z]+[a-z]+\.[a-z]+\d|[A-Z]+[a-z]+\.[a-z]+\d|'
                           r'[A-Za-z]+[A-Z]+[a-z]+\.[a-z]+|[A-Z]+\.[a-z]+|[A-Za-z]+[A-Z]+\.[a-z]+|'
                           r'[A-Z]+[a-z]+\.[a-z]+', info)
        color = re.findall(r'#......', info)

    user_input = int(input(' 1 - Считать имена и фамилии\n 2 - Считать все емайлы\n 3 - Считать названия файлов\n '
                           '4 - Считать цвета\n 5 - Выход\n'))

    if user_input == 1:
        with open('name.txt', 'w') as name_file:
            name_file.write(f'{len(name)}\n{name}')
    if user_input == 2:
        with open('emails.txt', 'w') as emails_file:
            emails_file.write(f'{len(emails)}\n{emails}')
    if user_input == 3:
        with open('file', 'w') as file:
            file.write(f'{len(files)}\n{files}')
    if user_input == 4:
        with open('color.txt', 'w') as color_file:
            color_file.write(f'{len(color)}\n{color}')
    if user_input == 5:
        break
