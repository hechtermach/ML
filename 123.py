
list_location=[]
def location(x=0,y=0):
    s = input("请输入一个字符串s:")
    global i
    global length_s
    i=0
    length_s=len(s)
    print (length_s)
    '''s.replace('R',1)
    s.replace('L',2)
    s.replace('U',3)
    s.replace('D',4)'''
    while (i<length_s):
        list_location.append((x,y))
        i=i+1
        if s[i]=='R':
            x=x+1
        elif s[i]=='L':
            x=x-1
        elif s[i]=='U':
            y=y+1
        elif s[i]=='D':
            y=y-1
    print (list_location)
        
location()
