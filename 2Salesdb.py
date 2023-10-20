import datetime

class SalesSystem:
    def __init__(self):
        self.sales = []
        self.customers = {}

    def record_sale(self, customer_name, items):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale = {'customer_name': customer_name, 'date': date, 'items': items}
        self.sales.append(sale)
        self.update_customer_data(customer_name, items)

    def update_customer_data(self, customer_name, items):
        if customer_name in self.customers:
            self.customers[customer_name]['total_sales'] += 1
            self.customers[customer_name]['total_items'] += len(items)
        else:
            self.customers[customer_name] = {'total_sales': 1, 'total_items': len(items)}

    def calculate_total_sales(self, start_date=None, end_date=None):
        total_sales = 0
        for sale in self.sales:
            sale_date = datetime.datetime.strptime(sale['date'], "%Y-%m-%d %H:%M:%S")
            if start_date and sale_date < start_date:
                continue
            if end_date and sale_date > end_date:
                continue
            total_sales += sum(item['price'] for item in sale['items'])
        return total_sales

    def provide_discount(self, customer_name):
        if customer_name in self.customers and self.customers[customer_name]['total_sales'] >= 10:
            return 0.1  # 10% discount for frequent customers
        else:
            return 0

    def generate_report(self):
        print("{:<20} {:<15} {:<10}".format('Customer', 'Total Sales', 'Total Items'))
        for customer, data in self.customers.items():
            print("{:<20} {:<15} {:<10}".format(customer, data['total_sales'], data['total_items']))


sales_system = SalesSystem()

# Record sales
sales_system.record_sale('John', [{'item': 'Apple', 'price': 1.5}, {'item': 'Banana', 'price': 0.5}])
sales_system.record_sale('Mary', [{'item': 'Orange', 'price': 2.0}, {'item': 'Grapes', 'price': 1.0}])

# Calculate total sales for a specific period
start_date = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d")
end_date = datetime.datetime.strptime("2022-12-31", "%Y-%m-%d")
total_sales = sales_system.calculate_total_sales(start_date, end_date)
print("Total sales for 2022:", total_sales)

# Provide personalized discount to frequent customers
discount = sales_system.provide_discount('John')
print("Discount for John:", discount)

# Generate report of top customers
sales_system.generate_report()

