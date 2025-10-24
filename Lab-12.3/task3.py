def maximize_profit(milk_available, choco_available, profit_A, profit_B):
    max_profit = 0
    best_A = 0
    best_B = 0
    
    for A in range(milk_available + 1):
        for B in range(milk_available + 1):
            # Each unit of A requires 1 milk, 3 choco
            # Each unit of B requires 1 milk, 2 choco
            total_milk = A + B
            total_choco = 3 * A + 2 * B
            if total_milk <= milk_available and total_choco <= choco_available:
                profit = profit_A * A + profit_B * B
                if profit > max_profit:
                    max_profit = profit
                    best_A = A
                    best_B = B
    
    print(f"Produce {best_A} units of A and {best_B} units of B for maximum profit.")
    print(f"Maximum profit: Rs {max_profit}")

if _name_ == "_main_":
    milk_available = int(input("Enter available units of Milk: "))  # e.g., 5
    choco_available = int(input("Enter available units of Choco: "))  # e.g., 12
    profit_A = int(input("Enter profit per unit of A: "))  # e.g., 6
    profit_B = int(input("Enter profit per unit of B: "))  # e.g., 5

    maximize_profit(milk_available, choco_available, profit_A, profit_B)