'''def steps(s):
    countnt_r = s.count('R')
    count_l= s.count('L')
    count_u = s.count('U')
    count_d = s.count('D')
    count_un=s.count('?')
    distance_x=count_r-count_l
    distance_y=count_u-count_d
    return (distance_x,distance_y,count_un)

s = input("请输入一个字符串:")
print(steps(s))'''




def CompletePath(s):
    
    def steps(s):
        count_r = s.count('R')
        count_l= s.count('L')
        count_u = s.count('U')
        count_d = s.count('D')
        count_un=s.count('?')
        distance_x=count_r-count_l
        distance_y=count_u-count_d
        return (distance_x,distance_y,count_un)

    return steps(s)[2]
list_s=[]
s = input("请输入一个字符串s:")


print (CompletePath(s))
