print ("Welcome to the tip calculator!")

print ("What is the total bill amount?")
bill=float(input("$:"))

print ("How much tip would you like to give?")
tip=float(input("Percent:"))

print ("How many people to split the bill?")
people=float(input("People:"))

#"{:.2f}" định dạng chuỗi
#: bắt đầu phần định dạng số
#.2 làm tròn đến 2 chữ số sau dấu phẩy
# biểu thị đây là 1 dấu phẩy động (float)
pay=("{:.2f}".format((((bill * (tip / 100)) + bill) / people))) #định dạng kết quả thành một chuỗi có 2 chữ số sau dấu phẩy

print(f"Each person should pay: ${pay}") # f"" cho phép nhúng giá trị trực tiếp vào chuỗi
