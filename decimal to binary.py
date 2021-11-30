def dec(value):
    tin= ''
    if value > 1:
        dec(value // 2)
    tin=(value%2)    
    print(tin, end = ' ')
 
num = int(input("Enter any number: "))
print("binary value of decimal: ",num)
dec(num)
