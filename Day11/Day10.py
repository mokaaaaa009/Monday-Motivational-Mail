def Add (n1,n2):
    return n1+n2

def Substract (n1,n2):
    return n1-n2

def Multiply (n1,n2):
    return n1*n2

def Divide (n1,n2):
    return n1/n2


operator={"+":Add,
"-":Substract,
"*":Multiply,
"/":Divide}

n1=float(input("Enter you first Number: "))


for operation in operator:
  print(operation)

symbol=input("Pick operation: ")
n2=float(input("Enter you second Number: "))
res=operator[symbol](n1,n2)

