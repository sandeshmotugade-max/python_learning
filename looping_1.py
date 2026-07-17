orders = [2500, 1200, 5000, 800, 3200, 1500]

total_revenue = 0
high_value_orders = 0
max_order = 0
small_order = 0

for order in orders:
    total_revenue = total_revenue + order

    if order > 2000:
     high_value_orders = high_value_orders + 1

    if order > max_order:
       max_order = order 

    if order < 1000:
       small_order = small_order + 1

average_order = total_revenue/len(orders) 

print("total revenue:", total_revenue)
print("orders above 2000:", high_value_orders)
print("higest order:", max_order)
print("Number of small orders (<1000):", small_order)
print("Average order value:", average_order)