
current_balance= 0
while True:
    print(" Bank System")
    input_value = int(input('Pleas Enter number \n1 to see your balance,\n2 to deposit\n3 to withdraw\n4 to exite proccec\n'))

    if input_value==1:
        print("Your current blace: {}" .format(current_balance))
    elif input_value==2:
        deposit=int(input("Enter deposit amount:"))
        if deposit==0:
            print("You cannot deposit 0")
            continue
        current_balance =current_balance + deposit
        print("Your current blace: {}" .format(current_balance))

    elif input_value==3:
        withdrow=int(input("Enter withdraw amount:"))
        if current_balance > withdrow:
            current_balance=current_balance-withdrow
            print("Your current blace: {}" .format(current_balance))
            continue
        elif withdrow==0:
            print("You cannot withdrow 0")
            continue
        else:
            print("Insufficient Balance !!")
            print("Your account have  {} Balance" .format(current_balance))
        
    elif input_value==4:
        break
    else:
        print("Plese give valid input")

  