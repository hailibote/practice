# 两边对齐

users = {'Hans': 'active', 'Éléonore': 'inactive', 'Jingtai': 'active'}

# for keys,values in users.copy().items():
#     if values == 'inactive':
#         del users[keys]
    
d = max(map(len, users.keys()))
for x in users:
    print(x.rjust(d),':',users[x])
