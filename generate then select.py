list_step=['R','L','U','D']
list_all=[]
def generate_un_list(s)
    count_un=s.count('?')
    global number_row
    global store_s
    store_s=[]

    for step in s:
        if step=='?'
            store_s.append(list_step)
    return store_s

def generate_all_path(s)
    count_un=s.count('?')
    global store_un
    global store_all
    global i
    global j
    global ss
    i=0
    j=0
    store_un=generate_un_list(s)
    while (i<=count_un):
        while (j<=count_un):
            ss=s
            s.replace('?',store_un[i][j],1)
            list_all.append(s)
            j+=1
        i+=1

def generate_position (s)
    
    for step in s:
        list_location.append((x,y))
        if step=='R':
            x=x+1
        elif step=='L':
            x=x-1
        elif step=='U':
            y=y+1
        elif step=='D':
            y=y-1
        
