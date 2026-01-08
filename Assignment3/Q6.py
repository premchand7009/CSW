def filter_high_sales(sales, threshold):
    for amount in sales:
        if amount >= threshold:
            yield amount


daily_sales = [250, 800, 450, 1200, 600]
threshold = 500

print("Daily Sales:", daily_sales)
print("Threshold:", threshold)
print("High Sales:")

for sale in filter_high_sales(daily_sales, threshold):
    print(sale)
