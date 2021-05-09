f1=open("payment.jpg","rb")
f2=open("googlepay.jpg","wb")

photo = f1.read()
f2.write(photo)
f1.close()
f2.close()
print("Binary file is saved successfully")