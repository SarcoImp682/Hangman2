guest = []
while True:
    name = input()
    if name != '.':
        guest.append(name)
    else:
        break
print(f'{guest}\n{len(guest)}')
