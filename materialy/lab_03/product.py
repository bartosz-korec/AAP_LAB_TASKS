# -*- coding: utf-8 -*-
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be >= 0")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0 or amount > self.quantity:
            raise ValueError("Invalid amount")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity
