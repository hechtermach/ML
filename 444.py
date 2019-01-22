list_s=[]
##define func complete path
def CompletePath(s,w,h):
##count r,l,u,d,?    
    def steps(s):
        count_r = s.count('R')
        count_l= s.count('L')
        count_u = s.count('U')
        count_d = s.count('D')
        count_un=s.count('?')
        distance_x=count_r-count_l
        distance_y=count_u-count_d
        return (distance_x,distance_y,count_un)

    step_un=steps(s)[2]
    while (step_un>0):
        if (distance_x<w-1):
            s.replace('?',R',1)
            count_un-=1          
        elif (distance_x>=w):
            s.replace('?','L',1)
            count_un-=1
        elif (distance_y<h-1):
            s.replace('?','U',1)
            count_un-=1
        elif (distance_y>=h):
            s.replace('?','D',1)
            count_un-=1
        else:
            count_RRLLUUDD+=1
            count_un-=1
    list_s.append(s)
    
