from rpy2.robjects.packages import STAP

rfile = 'main.r'
with open(rfile, 'r') as f:
    string = f.read()
functions = STAP(string, "functions")

returnValue = functions.main()
print("The return value of main() is", returnValue[0])
#optional = True
#returnValue = functions.main(optional)
#print("The return value of main(TRUE) is", returnValue[0])
