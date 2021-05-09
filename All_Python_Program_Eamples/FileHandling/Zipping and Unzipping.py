from zipfile import *

# Zipping File in Local Directory

# f= ZipFile("test_zip.zip","w",ZIP_DEFLATED)
# f.write("1.txt")
# f.write("2.txt")
# f.write("3.txt")
# f.close()
# print("File Zip operation completed successfully")

#Unzipping File

f = ZipFile("test_zip.zip","r",ZIP_STORED)
names=f.namelist()
for name in names:
    print("File name:", name)
    print("---------Content of file is-----------")
    f=open(name)
    data=f.read()
    print(data)
    f.close()