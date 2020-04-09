#if else

is_hot = False
is_cold = False


if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")

print("enjoy your day")


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down payment: ${down_payment}")