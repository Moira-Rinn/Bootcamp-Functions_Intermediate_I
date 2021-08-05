# 1. Update Values in Dictionaries and Lists:

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

# 1-1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].


def swapTen():
    for y in range(len(x)):
        for z in range(len(x[y])):
            if x[y][z] == 10:
                x[y][z] = 15
    return x


print(swapTen())

# 1-2. Change the last_name of the first student from 'Jordan' to 'Bryant'.


def swapName():
    for x in range(len(students)):
        if students[x]['last_name'] == 'Jordan':
            students[x]['last_name'] = 'Bryant'
    return students


print(swapName())

# 1-3. In the sports_directory, change 'Messi' to 'Andres'.


def swapName():
    for x in sports_directory.keys():
        for y in range(len(sports_directory[x])):
            if sports_directory[x][y] == 'Messi':
                sports_directory[x][y] = 'Andres'

    return sports_directory


print(swapName())

# 1-4. Change the value 20 in z to 30


def swapVal():
    for x in range(len(z)):
        for keys in z[x].keys():
            for key in keys:
                if z[x][key] == 20:
                    z[x][key] = 30

    return z


print(swapVal())

# 2. Iterate Through a List of Dictionaries:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary():
    for x in range(len(students)):
        for entry in students[x]:
            print(f"{entry} - {students[x][entry]}")


iterateDictionary()


def iterateDictionary():
    for x in range(len(students)):
        item = ""
        cnt = 0
        for key in students[x].keys():
            if cnt < len(students[x])-1:
                item += f"{key} - {students[x][key]}, "
            else:
                item += f"{key} - {students[x][key]}"
            cnt += 1
        print(item)


iterateDictionary()

# 3. Get Values From a List of Dictionaries:


def iterateDictionary2(key, students):
    for student in students:
        print(student[key])


iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dic):
    for entry in dic:
        print(f"{len(dic[entry])} {entry.upper()}")
        for x in range(len(dic[entry])):
            print(dic[entry][x])


printInfo(dojo)
