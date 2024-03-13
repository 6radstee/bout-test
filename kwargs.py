#kwargs = a parameter that allows packing all types of arguments in a dictionary
# 

def  hello(**kwargs):
   #print("hello"+" "+kwargs["first"]+" "+ kwargs ["middle"]+" "+kwargs["last"])

    print("hello",end=" ")
    for key,value in kwargs.items():
        print (value,end=" ") 

#    for i in kwargs:
#        sum +=0
#print(1,2,3,4)
hello(title="Mr ",first="stano",middle="bradley",last="ochieng")