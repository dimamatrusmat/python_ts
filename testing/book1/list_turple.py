grid = [
    ['.','.','.','.','.','.'],
    ['.','O','O','.','.','.'],
    ['O','O','O','O','.','.'],
    ['O','O','O','O','O','.'],
    ['.','O','O','O','O','O'],
    ['O','O','O','O','O','.'],
    ['O','O','O','O','.','.'],
    ['.','O','O','.','.','.'],
    ['.','.','.','.','.','.']
]

height = len(grid)
width = len(grid[0])

s = 0
str1 = ""

for i in range(height):
    for q in range(width):
        str1.join(grid[i][s])
    str1 += "\n"
    s = s + 1
print(str1)
