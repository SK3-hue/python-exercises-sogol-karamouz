#question04-S07
    
transactions = [("Ali", "deposit", 50000000, 10),("Ali", "withdraw", 2000000, 11),\
                    ("Ali", "withdraw", 3000000, 12),("Ali", "withdraw", 4000000, 13),\
                        ("Ali", "withdraw", 5000000, 14),("Ali", "withdraw", 6000000, 15),\
                            ("Sara", "deposit", 50000000, 20),\
                                ("Sara", "withdraw", 60000000, 21),\
                                    ("Reza", "deposit", 150000000, 30)]
def check_large_transaction():
    for i in transactions:
        if i[2] > 100000000:
            print(f"Large transaction: {i}")


def check_repeated_withdrawals():
    names = set([i[0] for i in transactions])

    for name in names:
        totalt = 0

        for i in transactions:
            if i[0] == name:
                totalt += 1

        if totalt > 3:
            print(f"Repeated transactions: {name}")


def check_balance():
    names = set([i[0] for i in transactions])

    for name in names:
        total = 0
        total1 = 0

        for i in transactions:
            if i[0] == name and i[1] == "deposit":
                total += i[2]

        for i in transactions:
            if i[0] == name and i[1] == "withdraw":
                total1 += i[2]

        if total1 > total:
            print(f"Negative balance: {name}")


def generate_fraud_report():
    print("__Fraud Report__")

    check_large_transaction()
    check_repeated_withdrawals()
    check_balance()


generate_fraud_report()
