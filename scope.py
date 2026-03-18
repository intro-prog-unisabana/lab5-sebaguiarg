ranint = None
ranstr = None

def set_globals(a,b):
    global ranint, ranstr
    ranint = int(a)
    ranstr = str(b)
def get_globals():
    return (ranint, ranstr)