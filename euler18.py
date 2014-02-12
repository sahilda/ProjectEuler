def read_file(file):
    f = open(file,'r')
    f = f.read().split('\n')
    triangle = []
    for line in f:
        try: line.split()
        except: pass
        else:
            if len(line) > 0: triangle.append(line.split())
    return triangle

# To return the data in the form of x = rows, y = columns, and make the index start at 1, not zero
def value(x,y):
    if x <= 0 or y <= 0: raise Exception("Error!")
    return int(data[x-1][y-1])

def brute(data,x,y,sum,path):
    try: value(x+1,y)
    except: pass
    else: route(data,x+1,y,sum,path)

    try: value(x+1,y+1)
    except: pass
    else: route(data,x+1,y+1,sum,path)

def one_step(data,x,y,sum,path):
    a = 0
    b = 0
    try: value(x+1,y)
    except: pass
    else: a = value(x+1,y)

    try: value(x+1,y+1)
    except: pass
    else: b = value(x+1,y+1)

    if a > b: route(data,x+1,y,sum,path)
    elif b > a: route(data,x+1,y+1,sum,path)
    else: brute(data,x,y,sum,path)

def two_step(data,x,y,sum,path):
    a = 0
    b = 0
    c = 0
    d = 0

    try: value(x+1,y) and value(x+2,y)
    except: pass
    else: a = value(x+1,y) + value(x+2,y)

    try: value(x+1,y) and value(x+2,y+1)
    except: pass
    else: b = value(x+1,y) + value(x+2,y+1)

    try: value(x+1,y+1) and value(x+2,y+1)
    except: pass
    else: c = value(x+1,y+1) + value(x+2,y+1)

    try: value(x+1,y+1) and value(x+2,y+2)
    except: pass
    else: d = value(x+1,y+1) + value(x+2,y+2)

    if max(a,b,c,d) == 0: one_step(data,x,y,sum,path)
    elif max(a,b,c,d) == a:
        route(data,x+2,y,sum + value(x+1,y),path+str(y))
    elif max(a,b,c,d) == b:
        route(data,x+2,y+1,sum + value(x+1,y),path+str(y))
    elif max(a,b,c,d) == c:
        route(data,x+2,y+1,sum + value(x+1,y+1),path+str(y+1))
    elif max(a,b,c,d) == d:
        route(data,x+2,y+2,sum + value(x+1,y+1),path+str(y+1))

def route(data,x,y,sum,path):
    sum += value(x,y)
    path += str(y)
    if x == len(data): paths[path] = sum

    two_step(data,x,y,sum,path)

data = read_file('triangle.txt')

x,y = 1,1 #start value
paths = {}
route(data,x,y,0,'')

# Output
max = 0
max_key = 0

for key in paths:
    if paths[key] >= max:
        max_key = key
        max = paths[key]

print len(paths), max_key, paths[max_key]
