class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0  # Track last transaction for voiding

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the cash register.
        """
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction_amount = price * quantity  # Store last transaction amount

    def apply_discount(self):
        """
        Applies a discount to the total price.
        """
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Ensure proper formatting (no decimals if not needed)
            total_display = int(self.total) if self.total.is_integer() else round(self.total, 2)
            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction from the total.
        """
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0  # Reset last transaction amount
