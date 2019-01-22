'''list_step=['R','L','U','D']
store=[]
i=5
while (i>=0):
    store.append(list_step)
    i-=1
print (store[2][2])'''


list_step=['R','L','U','D']


def generate_list(s):
    count_un=s.count('?')
    global number_row
    global store_s
    store_s=[]
    number_row=count_un

    for step in s:
        if step=='?':
            store_s.append(list_step)
    return store_s

print (generate_list('RULD????'))
