def calculate_total_fee(price, tax_rate):
    total = price * tax_rate
    return total

print(calculate_total_fee(1000, 1.1))