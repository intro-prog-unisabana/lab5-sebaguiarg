data = [2.0, 4.0, 6.0, 8.0]

def list_shift(a, b):
    for i in range(len(a)):
        a[i] += b

def calc_avg(a):
    prom = sum(a) / len(a)
    return prom

def print_normalized(a):
    print(a)
    
prom = calc_avg(data)        
list_shift(data, -prom)    
print_normalized(data)