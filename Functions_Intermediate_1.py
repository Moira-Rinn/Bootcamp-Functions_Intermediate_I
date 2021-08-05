x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].


def swapTen():
    for y in range(len(x)):
        for z in range(len(x[y])):
            if x[y][z] == 10:
                x[y][z] = 15
    return x


print(swapTen())

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'.


def swapName():
    for x in range(len(students)):
        if students[x]['last_name'] == 'Jordan':
            students[x]['last_name'] = 'Bryant'
    return students


print(swapName())

# 3. In the sports_directory, change 'Messi' to 'Andres'.


def swapName():
    for x in sports_directory.keys():
        for y in range(len(sports_directory[x])):
            if sports_directory[x][y] == 'Messi':
                sports_directory[x][y] = 'Andres'

    return sports_directory


print(swapName())

# 4. Change the value 20 in z to 30


def swapVal():
    for x in range(len(z)):
        for keys in z[x].keys():
            for key in keys:
                if z[x][key] == 20:
                    z[x][key] = 30

    return z


print(swapVal())
