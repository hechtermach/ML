import itertools
list_step=['R','L','U','D']
list_all=[]
list_path=[]
list_location=[]
list_feasible_path=[]

def generate_un_list(s):
    count_un=s.count('?')
    return (list(itertools.product(list_step,repeat=count_un)))

def generate_all_list(s):
    global list_path
    count_un=s.count('?')
    un_list=generate_un_list(s)
    for combo in un_list:
        ss=s      
        for i in combo:
            ss=ss.replace('?',i,1)    
            list_all.append(ss)
    for i in range(4**(count_un)):
        list_path.append(list_all[count_un*i+count_un-1])
    return list_path 

def check_path_right(s,w,h):
    paths=generate_all_list(s)
    for path in paths:
        x=0
        y=0
        list_location=[(x,y)]
        for step_each in path:
            if step_each=='R':
                x=x+1
            elif step_each=='L':
                x=x-1
            elif step_each=='U':
                y=y+1
            else:
                y=y-1
            if (x,y) not in list_location:
                list_location.append((x,y))
            else:
                break
        if (x,y)==(w-1,h-1):
            list_feasible_path.append(path)
    if list_feasible_path==[]:
        return 'null'
    return list_feasible_path

def CompletePath(s,w,h):
    output=check_path_right(s,w,h) 
    print (output) 

CompletePath('UURDD?UUR?RR',6,4)         