def bonAppetit(bill, k, b):
    total = 0

    for i in range(len(bill)):
        if i != k:
            total += bill[i]

    bill_division = total // 2

    if bill_division == b:
        print("Bon Appetit")
    else:
        print(b - bill_division)    
