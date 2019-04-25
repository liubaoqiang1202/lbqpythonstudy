a=8
count =0
while True:
    b=input("输入一个数")
    try:
        int(b)
        if int(b) ==a:
            count +=1
            print("你输入的数是%d,你猜的次数是%d"%(int(b),count))
            break
        elif int(b) >a:
            count+=1
            print("猜大了")
        else:
            count+=1
            print("猜小了")
    except ValueError:
        print("输入有误")
        
