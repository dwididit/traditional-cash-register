# Welcome to simple data cleaning from traditional casier data. Created by Dwi Didit Prasetiyo
from data import daily_sales

daily_sales_replaced = daily_sales.replace(";,;","X")
daily_transactions = daily_sales_replaced.split(",")
#print(daily_transactions)

daily_transactions_split = []
for transaction in daily_transactions:
    transaction = transaction.split("X")
    daily_transactions_split.append(transaction)

transaction_clean = []
for transaction in daily_transactions_split:
    transaction_data_clean = []
    for data in transaction:
        data = data.strip().strip("\n")
        transaction_data_clean.append(data)
    transaction_clean.append(transaction_data_clean)

customers = []
sales = []
thread_sold = []

for transaction in transaction_clean:
    customers.append(transaction[0])
    sales.append(transaction[1])
    thread_sold.append(transaction[2])

total_sales = 0
for sale in sales:
    sale_no_usd = sale.replace("$", "")
    sale_as_int = float(sale_no_usd)
    total_sales += sale_as_int
    total_sales = round(total_sales, 2)
print(f"Total sales today: ${total_sales}")
print(f"List of today customers: {customers}")

thread_sold_split = []
for color in thread_sold:
    if "&" in color:
        thread_sold_split.extend(color.split("&"))
    else:
        thread_sold_split.append(color)

def color_count(color):
    return thread_sold_split.count(color)

color = "white"
number = color_count(color)
print("Thread Shed sold {} threads of {} thread today.".format(number, color))

colors = list(set(thread_sold_split))
print("Thread colors available: {}".format(colors))