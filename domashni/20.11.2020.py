#3
def sqroot():

    num = int(input('Enter a number: '))
    num_cop = num
    count = 0

    while num >= 2:
        num = math.sqrt(num)
        count += 1

    print(num_cop, '-->', count)