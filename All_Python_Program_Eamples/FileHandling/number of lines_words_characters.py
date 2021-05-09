#WAP to print the number of lines,words and characters present in the given file?
import os
fname = input("Enter file name: ")
if os.path.isfile(fname):
    lcount=wcount=ccount=0
    f = open(fname)
    for file in f:
        # print(file,end="")
        # print(len(file))
        lcount = lcount+1
        count = file.split()
        # print(len(count))
        wcount = wcount+len(count)
        ccount = ccount + len(file)
    print("*"*40)
    print("Line count are:",lcount)
    print("Word count are:", wcount)
    print("Charator count are:", wcount)
    f.close()

else:
    print("File not found, enter correct file name")

