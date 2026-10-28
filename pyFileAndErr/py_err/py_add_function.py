while True:
    try:
        num = input("Enter a number: ")
        if num == 'q':
            break
        num_1 = int(num)
        num_2 = int(input("请输入一个被加数："))
    except ValueError:
        print('输入的必须为整型数值')
    else:
        print(num_1 + num_2)
        if num_1 == 'q' or num_2 == 'q':
            break
