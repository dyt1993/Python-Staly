#if else

name = "J"
#name = input("请输入你的名字：")
if len(name) < 3:
    print("name must be at least 3 characters.")
elif len(name) > 50:
    print("name must be a maximum 50 characters.")
else:
    print("name looks good!")