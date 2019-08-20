fn = input('Enter the name of the file: \n')
try:
    fh = open(fn)
    for lx in fh:
        CAPSHANDLE = lx.upper()
        strip = CAPSHANDLE.rstrip()
        print(strip)

except:
    print('File cannot be opened:', fn)
    exit()
