from decimal import Decimal

def solve(N, M, S, offers):
    S = Decimal(S)
    offers.sort(key=lambda x: (x[2]))
    print(offers)
    dp = [0] * (int(S) + 1)
    items = []

    for day, name, price, quantity in offers:
        price = price * 1000
        for i in range(int(S), int(price * quantity) - 1, -1):
            income_per_bond = 1000 + (N + 30 - day)
            total_cost = int(price * quantity)
            if i >= total_cost and dp[i - total_cost] + int(income_per_bond * quantity) > dp[i]:
                dp[i] = dp[i - total_cost] + int(income_per_bond * quantity)
                items.append((day, name, price / 1000, quantity))

    return int(dp[-1]), items


# Пример использования (с исправленным вводом):
N = 2
M = 2
S = 8000
offers = [
    (1, "alfa-05", 100.2, 2),
    (1, "alfa-05", 101.5, 5),
    (2, "gazprom-07", 100.0, 2),
]

max_income, purchased_bonds = solve(N, M, S, offers)

print(max_income)
for day, name, price, quantity in purchased_bonds:
    print(day, name, price, quantity)
print()