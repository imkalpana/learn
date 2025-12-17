class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        return True


    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        return False


    def get_balance(self):
        return sum(fund['amount'] for fund in self.ledger)
            
    
    def transfer(self, amount, destination):
        self.destination = destination
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        return False
        

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self):
        lines = [center_title(self.name)]
        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = '{:.2f}'.format(transaction['amount'])
            lines.append(f"{description.ljust(23)}{amount.rjust(7)}")
        lines.append(f"Total: {self.get_balance()}")
        return '\n'.join(lines)


def center_title(title):
    title_length = len(title)
    left_padding = (30 - title_length) // 2
    right_padding = 30 - title_length - left_padding
    return '*' * left_padding + title + '*' * right_padding    


def create_spend_chart(categories):
    category_withdrawals = {}

    for category in categories:
        withdrawals = 0
        for transaction in category.ledger:
            amount = transaction['amount']
            if amount < 0:
                withdrawals += -amount  
        category_withdrawals[category.name] = withdrawals

    total_withdrawals = sum(category_withdrawals.values())

    category_percentages = {}
    for name, withdrawals in category_withdrawals.items():
        category_percentages[name] = (withdrawals / total_withdrawals) * 100 if total_withdrawals > 0 else 0


    chart_str = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for name in category_percentages:
            percent = category_percentages[name]
            if percent >= i:
                line += "o  "
            else:
                line += "   "
        chart_str += line + "\n"

    # Print the horizontal line at the bottom of the chart
    chart_str += "    " + "-" * (len(category_percentages) * 3 + 1) + "\n"

    # Print category names vertically
    max_name_length = max(len(name) for name in category_percentages)
    for i in range(max_name_length):
        line = "     "  
        for name in category_percentages:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        chart_str += line  + '\n'
        

    return chart_str.rstrip('\n')



food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(500.00, "groceries")

clothing = Category("Clothing")
clothing.deposit(1000, "deposit")
clothing.withdraw(100.00, "buying new clothes")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(200.00, "fuel")

food.transfer(200, clothing)


categories = [food, clothing, auto]
chart_str = create_spend_chart(categories)

print(clothing)
print(chart_str)
