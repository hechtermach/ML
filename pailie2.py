##import itertools
##l = [1, 2, 3]
##for item in itertools.product(l,repeat=2):
##    print (item)
import itertools
list_step=['R','L','U','D']
list_all=[]

def generate_un_list(s):
    count_un=s.count('?')
    return (list_step,repeat=count_un)


print (generate_un_list('URL??'))
