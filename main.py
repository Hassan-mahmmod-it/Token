def search(path, string):
    count = 0
    with open(path, 'r') as file:
        for line in file:
            if string in line:
                print(string)


# -------------------------------------------------------
def deletelist(lister):
    y = ""
    for l in lister:
        y = y + l
    return y

# -----------------------------------------------------------
f = open("text", "r")
file = f.read()
logic = []
num = []
i = 0
j = 0
count = -1
for l in file:
    count = count + 1
print("the sum = ", count)

# -------------------------------------------------------------
print("-----(Logic Operation)-----")
for i in range(count):
    if file[i] in ['(', ')', '<', '>', '=', '+', '^', '%', '{', '}']:
        logic[j:j] = file[i]
        i = i + 1
        j = j + 1
print(logic)
print("-----(The Number)-----")
for i in range(count):
    if file[i] in ['0', '1', '2', '3', '5', '5', '6', '7', '8', '9']:
        num[j:j] = file[i]
        i = i + 1
        j = j + 1
print(deletelist(num))
print("-----(Key Word)-----")
ls = 0
search_string = ['for', 'int', 'if', "include", "using", "namespace", "std", "main", "cout", "return", "iostream"]
for k in search_string:
    ls = ls + 1
for i in range(ls):
    search("text", search_string[i])
    i = i + 1








