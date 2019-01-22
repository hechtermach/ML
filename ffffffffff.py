list_s=[]
list_un_step=[]
flag=True
##count r,l,u,d,?
def counts(s):
    count_r = s.count('R')
    count_l= s.count('L')
    count_u = s.count('U')
    count_d = s.count('D')
    count_un=s.count('?')
    distance_x=count_r-count_l
    distance_y=count_u-count_d
    return (distance_x,distance_y,count_un)

##generate step list for unknown step
def generate_list(s)
    number_un=counts(s)[2]
    while (number_un>0):
        if (distance_x<w-1):
            list_un_step.append('R')         
        elif (distance_x>=w):
            list_un_step.append('L')
        elif (distance_y<h-1):
            list_un_step.append('U')
        elif (distance_y>=h):
            list_un_step.append('D')
        else:
            flag=False
        number_un-=1
    return list_un_step
##location determination and check
def CompletePath(s,w,h)
    pool_un=generate
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

print (list_location)
