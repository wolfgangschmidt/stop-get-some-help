
import os



def file(name, mode):
    curpath = os.path.abspath(os.curdir)
    print(curpath)
    f =  open(f'%s/%s.py'% (curpath, name), f'%s' % mode)
    return f



def write():

    fl = file('some_name', 'w')
    idt = ident()
    cd = code()
    fl.write('def name():\n' + idt + cd)


def ident():
    return '    '

def code():
    return 'print("hello world")'


write()

        
