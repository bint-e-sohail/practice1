class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, n, q, p):
        self.items[n] = (q, p)
    def total_value(self):
        return sum(q*p for q,p in self.items.values())
    def save_report(self, filename="report.txt"):
        with open(filename, "w") as f:
            for name, (qty, price) in self.items.items():
                f.write(f"{name}: {qty} x {price} = {qty*price}\n")
            f.write(f"Total: {self.total_value()}\n")

inv = Inventory()
inv.add_item("notebook", 5, 120)
inv.add_item("marker", 4, 80)
inv.save_report()
print("report.txt has been created successfully")