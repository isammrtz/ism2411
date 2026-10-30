# Isabella Martinez - ISM2411 Week 7
# Self-Assessment 1: The first bug identified during the AI-assisted review
# was the missing colon after 'for sale in sales', which causes SyntaxError.
# I received AI help before completing the solo debugging protocol, so this
# does not demonstrate independent debugging instincts. I need to practice
# reading the traceback and tracing values myself before asking for help.
# Self-Assessment 2: apply_discount takes a price and a customer tier. It returns
# the price after a 15% gold, 10% silver, or 5% bronze discount; other tiers
# receive no discount. Its name and docstring explain its use to a colleague.
# AI use: ChatGPT generated the exercise code and explanatory comments,
# identified and corrected the three bugs in broken_sales.py, drafted these
# self-assessment comments, and ran the completed script to check its outputs.
# Self-Assessment 3: This help supplied the solution rather than following
# the solo-debug-first exercise. To build understanding, I need to explain
# each function and each bug fix myself and practice without AI assistance.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    """Return the tax amount for a price and decimal tax rate."""
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    """Return price after gold (15%), silver (10%), or bronze (5%) discount."""
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':8} ${apply_discount(200, tier):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
total = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")


def final_price(price, tier, tax_rate):
    """Return discounted price plus tax calculated on that discounted price."""
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# Diagnosis: The count loop is missing a colon (SyntaxError). The total loop
# replaces the running total each time, leaving only the last sale ($90).
# The while loop allows i to equal len(sales), causing IndexError because
# a five-item list has valid indices 0 through 4, not 5.
sales = [120, 80, 250, 175, 90]

# Fix: Add each sale to the running total instead of replacing the total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Fix: End the for-loop header with a colon so Python can parse the loop.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Fix: Stop before the index reaches the list length to stay within bounds.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
# Prediction: 100, 1998, 100.
# The x inside double_it is local to that function. Setting it to 999 does
# not change the global x, which remains 100 before and after the call.
x = 100


def double_it():
    x = 999
    return x * 2


print(x)
print(double_it())
print(x)
