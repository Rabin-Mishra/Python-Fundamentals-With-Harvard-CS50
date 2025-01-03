'''
This can be useful to close objects and clean up resources:

Example
Try to open and write to a file that is not writable:
'''
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Sth went wrong while writing a file")
    finally:
        f.close()
except:
    print("Sth went wrong on opening a file")
