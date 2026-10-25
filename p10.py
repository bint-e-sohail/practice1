# Problem 10 Inventory Mini Project

class Inventory:
    def __init__(self):
        self.items = {}  # name -> (qty, price)

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items) #return dict lenght

# Main program
inv = Inventory()

try:
    with open("stock.txt") as f: #close automatically using with
        for line in f:
            line = line.strip() #remove spaces and \n
            if not line:
                continue
            try: # split
                name, qty_str, price_str = [x.strip() for x in line.split(",")]
                qty = int(qty_str) #str into int
                price = int(price_str)
                inv.add_item(name, qty, price)
            except ValueError:
                print(f"Skipping {name}: bad number")

except FileNotFoundError:
    print("stock.txt not found, using empty inventory")

# 1. Print count and total
print(f"{len(inv)} items, total value {inv.total_value()}")

# 2. Remove pen and print again
inv.remove_item("pen")
print(f"{len(inv)} items, total value {inv.total_value()}")

# 3. Remove laptop and catch error
try:
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")

