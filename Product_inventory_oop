class store_data():
    def __init__(self, no_of_products):
        self.no_products = no_of_products
        self.sides = [0 for i in range(no_of_products)]
    def get_products(self):
        self.products = [str(input(f"\nenter product {i+1}: ")) for i in range(self.no_products)]
    def get_price(self):
        self.price = [int(input(f"\nEnter price of {self.products[i]}: ")) for i in range(self.no_products)]
    def get_qty(self):
        self.qty = [int(input(f"\nEnter the qty of {self.products[i]}: ")) for i in range(self.no_products)]
    def display(self):
        print(f"Product : {self.products[0]}, Price : {self.price[0]}$, Quantity : {self.qty[0]}\n"
              f"Product : {self.products[1]}, Price : {self.price[1]}$, Quantity : {self.qty[1]}")
    def check_qty(self,q1):
        while True:
            qty = float(input(" : "))
            if qty <= q1:
                return qty
            else:
                print("we don't have enough product")

class purchase(store_data):
    def __init__(self):
        store_data.__init__(self,2)


    def buy_items(self):
        p1, p2 = self.products
        pr1,pr2 = self.price
        q1, q2 = self.qty
        amount = float(input("Enter the amount you have: "))
        i1 = print(f"How many {p1} you want")
        i1 = self.check_qty(q1)
        i2 = print(f"How many {p2} you want")
        i2 = self.check_qty(q2)
        tot_amount = (i1 * pr1) + (i2 * pr2)
        if tot_amount<= amount:
            temp = []
            print(f"Total Amount : {tot_amount}")
            temp.append(q1 - i1)
            temp.append(q2-i2)
            self.qty = temp
            return tot_amount
        else:
            print("WARNING : less amount you have...")
            profit = 0
            return profit
    def stock_product(self,profit):
        print("re_stock")
        if self.qty[0] < self.qty[1]:
            p = profit /self.price[0]
            avl = profit % self.price[0]
            p_2 = avl / self.price[1]
            p = self.qty[0] + p
            p_2 = self.qty[1] + p_2
            temp = []
            temp.append(p)
            temp.append(p_2)
            self.qty = temp
        else:
            p = profit / self.price[1]
            avl = profit % self.price[1]
            p_2 = avl / self.price[0]
            p = self.qty[1] + p
            p_2 = self.qty[0] + p_2
            temp = []
            temp.append(p_2)
            temp.append(p)
            self.qty = temp





data = purchase()
data.get_products()
data.get_price()
data.get_qty()
data.display()
profit = data.buy_items()
data.display()
print("After re_stocking")
if profit > 0:
    data.stock_product(profit)
data.display()
