import tkinter as tk

class StoreGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Store GUI")


        self.product_label = tk.Label(self.root, text="Search for Products")
        self.product_label.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.search_product)
        self.search_button.pack()

        self.cart_label = tk.Label(self.root, text="Shopping Cart")
        self.cart_label.pack()

        self.cart_text = tk.Text(self.root)
        self.cart_text.pack()

        self.total_cost_button = tk.Button(self.root, text="Calculate Total Cost", command=self.calculate_total_cost)
        self.total_cost_button.pack()

        self.orders_label = tk.Label(self.root, text="Place Orders")
        self.orders_label.pack()

        self.delivery_options = tk.StringVar(self.root)
        self.delivery_options.set("Home Delivery") # Default value

        self.delivery_dropdown = tk.OptionMenu(self.root, self.delivery_options, "Home Delivery", "Pickup")
        self.delivery_dropdown.pack()

        self.place_order_button = tk.Button(self.root, text="Place Order")
        self.place_order_button.pack()

        self.root.mainloop()

    def search_product(self):
        keyword = self.search_entry.get()
   

    def calculate_total_cost(self):


     def place_order(self):
        delivery_option = self.delivery_options.get()


store_gui = StoreGUI()

