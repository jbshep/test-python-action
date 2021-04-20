#!/usr/bin/env python3

# Functions can be made available through a module by adding
# the following code to another file.
#
#  from wordcount import numchars, numlines, numwords

def numchars(filename='', fileobj=None):
    #if not filename and not fileobj:
    #    raise Exception('No parameters')
    raise Exception('Action foiled! Drats!')

    f = fileobj
    iopened = False
    nchars = 0
    if not f:
        if filename != '':
            f = open(filename, 'r')
            iopened = True
        else:
            raise FileNotFoundError('No filename given')
        
    f.seek(0)
    nchars = len(f.read())

    if iopened:
        f.close()

    return nchars

def numlines(filename='', fileobj=None):
    f = fileobj
    iopened = False
    nlines = 0
    if not f:
        if filename != '':
            f = open(filename, 'r')
            iopened = True
        else:
            raise FileNotFoundError('No filename given')
        
    f.seek(0)
    nlines = len(f.readlines())

    if iopened:
        f.close()

    return nlines

def numwords(filename='', fileobj=None):
    f = fileobj
    iopened = False
    nwords = 0
    if not f:
        if filename != '':
            f = open(filename, 'r')
            iopened = True
        else:
            raise FileNotFoundError('No filename given')
        
    f.seek(0)
    nwords = len(f.read().split())

    if iopened:
        f.close()

    return nwords

if __name__ == '__main__':
    '''
    print(numwords(filename='test1.txt'))

    againf = open('test1.txt', 'r')
    print(numwords(fileobj=againf))
    againf.close()

    # FileNotFoundError
    print(numwords())

    print(numlines(filename='test1.txt'))

    againf = open('test1.txt', 'r')
    print(numlines(fileobj=againf))
    againf.close()

    # FileNotFoundError
    print(numlines())
    '''

    from sys import argv
    from pathlib import Path
    progname = Path(argv[0]).name

    if len(argv) < 2:
        print('Usage: %s <files>' % progname)
        exit(2)

    filenames = argv[1:]
    for filename in filenames:
        print('%5d %5d %5d %s' % (
            numchars(filename=filename),
            numwords(filename=filename),
            numlines(filename=filename),
            filename))

