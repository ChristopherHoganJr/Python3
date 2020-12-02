row1 = ['⬜️','⬜️','⬜️']
row2 = ['⬜️','⬜️','⬜️']
row3 = ['⬜️','⬜️','⬜️']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure?\n')
xy = position.split(', ')

x = int(xy[0])-1
y = int(xy[1])-1

# Selecting the row or Y axis
map[y][x] = 'X'

print(f'{row1}\n{row2}\n{row3}')

