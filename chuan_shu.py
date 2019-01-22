import itertools
list_step=['R','L','U','D']
list_all=[]
list_path=[]
def generate_un_list(s):
    count_r = s.count('R')
    count_l= s.count('L')
    count_u = s.count('U')
    count_d = s.count('D')
    count_un=s.count('?')
    distance_x=count_r-count_l
    distance_y=count_u-count_d
    if count_un==1:
        return list_step
    elif count_un==2:
        return (list(itertools.product(list_step,list_step)))
    elif count_un==3:
        return (list(itertools.product(list_step,list_step,list_step)))
    elif count_un==4:
        return (list(itertools.product(list_step,list_step,list_step,list_step))) 

def generate_all_list(s):
    global list_path
    count_un=s.count('?')
    generate_index=0
    un_list=generate_un_list(s)
    for combo in un_list:
        ss=s      
        for i in combo:
            ss=ss.replace('?',i,1)    
            list_all.append(ss)
    for i in range(4^(count_un)+1):
        list_path.append(list_all[count_un*i])
    return list_path
#    return list_all
ttttt=generate_all_list('URL???DDDDU')
print (ttttt)  
