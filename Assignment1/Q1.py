def generate_bill(item, price, quantity=1, discount=0, taxrate=0.05):
    subtotal = price * quantity
    discount_amount = subtotal * (discount / 100)
    after_discount = subtotal - discount_amount
    tax_amount = after_discount * taxrate
    total = after_discount + tax_amount

    print("----- BILL SUMMARY -----")
    print(f"Item Name       : {item}")
    print(f"Quantity        : {quantity}")
    print(f"Price per item  : ₹{price:.2f}")
    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"Discount ({discount}%) : -₹{discount_amount:.2f}")
    print(f"Tax ({taxrate*100:.1f}%)     : +₹{tax_amount:.2f}")
    print(f"Total Payable   : ₹{total:.2f}")
    print("-------------------------\n")


generate_bill("Notebook", 50)
generate_bill("Pen", 10, 5)
generate_bill("Bag", 1200, discount=10, taxrate=0.08)
generate_bill("Shoes", 2000, 2, 15, 0.12)
