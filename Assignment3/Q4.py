def sales_report(*args, **kwargs):
    total_sales = sum(args)
    extra_count = len(kwargs)

    print("Total Sales Amount:", total_sales)
    print("Number of Extra Information Items:", extra_count)

    if extra_count > 0:
        print("Extra Information Provided:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


sales_report(
    5000, 3000, 4500,
    Name="John Doe",
    Date="2025-11-01",
    Location="Bhubaneswar"
)
