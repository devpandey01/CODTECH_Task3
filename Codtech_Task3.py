import tkinter as tk
from tkinter import messagebox

class InventoryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.inventory = {}

        self.product_label = tk.Label(root, text="Product Name")
        self.product_label.grid(row=0, column=0)
        self.product_entry = tk.Entry(root)
        self.product_entry.grid(row=0, column=1)

        self.quantity_label = tk.Label(root, text="Quantity")
        self.quantity_label.grid(row=1, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1)

        # Buttons
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=2, column=0)

        self.edit_button = tk.Button(root, text="Edit Product", command=self.edit_product)
        self.edit_button.grid(row=2, column=1)

        self.delete_button = tk.Button(root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=3, column=0)

        self.show_button = tk.Button(root, text="Show Inventory", command=self.show_inventory)
        self.show_button.grid(row=3, column=1)

        self.report_button = tk.Button(root, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=4, column=0, columnspan=2)

    def add_product(self):
        product = self.product_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            self.inventory[product] = quantity
            messagebox.showinfo("Success", f"Product '{product}' added with quantity {quantity}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")

    def edit_product(self):
        product = self.product_entry.get()
        if product in self.inventory:
            try:
                quantity = int(self.quantity_entry.get())
                self.inventory[product] = quantity
                messagebox.showinfo("Success", f"Product '{product}' updated with quantity {quantity}.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid quantity.")
        else:
            messagebox.showerror("Error", f"Product '{product}' not found.")

    def delete_product(self):
        product = self.product_entry.get()
        if product in self.inventory:
            del self.inventory[product]
            messagebox.showinfo("Success", f"Product '{product}' deleted.")
        else:
            messagebox.showerror("Error", f"Product '{product}' not found.")

    def show_inventory(self):
        if self.inventory:
            inventory_str = "\n".join([f"{product}: {quantity}" for product, quantity in self.inventory.items()])
            messagebox.showinfo("Inventory", inventory_str)
        else:
            messagebox.showerror("Error", "No products in the inventory.")

    def generate_report(self):
        if self.inventory:
            low_stock = [product for product, quantity in self.inventory.items() if quantity < 5]
            report = "Low Stock Alert:\n" + "\n".join(low_stock) if low_stock else "All products are sufficiently stocked."
            messagebox.showinfo("Inventory Report", report)
        else:
            messagebox.showerror("Error", "No products to generate a report.")

root = tk.Tk()
app = InventoryManagement(root)
root.mainloop()
