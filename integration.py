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





"""
P(Margin | Characteristics) = P(M | C) =
P(BreastDensity | M) * P(Location | M) * P(Age | M) * P(BC | M) * P(Mass | M) * P(AD | M) * P(Metastasis | M) * P(MC | M) * P(Size | M) *
P(Shape | M) * P(FibrTissueDev | M) * P(LymphNodes | M) * P(SkinRetract | M) * P(NippleDischarge | M) * P(Spiculation | M) * P(M)
/
P(BreastDensity | M) * P(Location | M) * P(Age | M) * P(BC | M) * P(Mass | M) * P(AD | M) * P(Metastasis | M) * P(MC | M) * P(Size | M) *
P(Shape | M) * P(FibrTissueDev | M) * P(LymphNodes | M) * P(SkinRetract | M) * P(NippleDischarge | M) * P(Spiculation | M)
"""