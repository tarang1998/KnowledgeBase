from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List


# === ENUMS ===

class ProductCategory(Enum):
    ELECTRONICS = 'Electronics'
    GROCERY = 'Grocery'
    CLOTHING = 'Clothing'
    FURNITURE = 'Furniture'
    OTHER = 'Other'


# === PRODUCT ===

class Product:
    def __init__(self, sku, name, price, quantity, threshold, category):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.threshold = threshold
        self.category = category

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        self.quantity -= amount


# === BUILDER PATTERN (Simplified) ===

class ProductBuilder:
    def __init__(self, sku, name, price, category):
        self.product = Product(sku, name, price, 0, 10, category)

    def quantity(self, quantity):
        self.product.quantity = quantity
        return self

    def threshold(self, threshold):
        self.product.threshold = threshold
        return self

    def build(self):
        return self.product


# === FACTORY PATTERN ===

class ProductFactory:
    def create_product(self, category, sku, name, price, quantity, threshold):
        builder = ProductBuilder(sku, name, price, category)
        return builder.quantity(quantity).threshold(threshold).build()


# === STRATEGY PATTERN ===

class ReplenishmentStrategy(ABC):
    @abstractmethod
    def replenish(self, product: Product):
        pass


class JustInTimeStrategy(ReplenishmentStrategy):
    def replenish(self, product: Product):
        print(f"[Just-In-Time] Replenishing {product.name}")


class BulkOrderStrategy(ReplenishmentStrategy):
    def replenish(self, product: Product):
        print(f"[Bulk Order] Replenishing {product.name}")


# === OBSERVER PATTERN ===

class InventoryObserver(ABC):
    @abstractmethod
    def update(self, product: Product):
        pass


class SupplierNotifier(InventoryObserver):
    def update(self, product: Product):
        print(f"[Supplier Alert] Low stock for {product.name}. Notify supplier!")


class DashboardAlertSystem(InventoryObserver):
    def update(self, product: Product):
        print(f"[Dashboard] Alert! {product.name} stock low: {product.quantity}")


# === WAREHOUSE ===

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product, quantity: int):
        if product.sku in self.products:
            self.products[product.sku].add_stock(quantity)
        else:
            product.quantity = quantity
            self.products[product.sku] = product
        print(f"[{self.name}] Added {quantity} of {product.name}")

    def remove_product(self, sku: str, quantity: int):
        if sku in self.products:
            product = self.products[sku]
            if product.quantity >= quantity:
                product.remove_stock(quantity)
                print(f"[{self.name}] Removed {quantity} of {product.name}")
            else:
                print("Error: Not enough stock")

    def get_product(self, sku: str):
        return self.products.get(sku)


# === SINGLETON INVENTORY MANAGER ===

class InventoryManager:
    _instance = None

    def __init__(self):
        if InventoryManager._instance:
            raise Exception("Use get_instance()")
        self.warehouses: List[Warehouse] = []
        self.factory = ProductFactory()
        self.observers: List[InventoryObserver] = []
        self.replenishment_strategy: ReplenishmentStrategy = None

    @staticmethod
    def get_instance():
        if not InventoryManager._instance:
            InventoryManager._instance = InventoryManager()
        return InventoryManager._instance

    def add_warehouse(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def add_observer(self, observer: InventoryObserver):
        self.observers.append(observer)

    def set_replenishment_strategy(self, strategy: ReplenishmentStrategy):
        self.replenishment_strategy = strategy

    def notify_observers(self, product: Product):
        for observer in self.observers:
            observer.update(product)

    def check_and_replenish(self, sku: str):
        for warehouse in self.warehouses:
            product = warehouse.get_product(sku)
            if product and product.quantity < product.threshold:
                self.notify_observers(product)
                if self.replenishment_strategy:
                    self.replenishment_strategy.replenish(product)


# === MAIN ===

if __name__ == "__main__":
    manager = InventoryManager.get_instance()

    # Observers
    manager.add_observer(SupplierNotifier())
    manager.add_observer(DashboardAlertSystem())

    # Strategy
    manager.set_replenishment_strategy(JustInTimeStrategy())

    # Warehouses
    w1 = Warehouse("Warehouse A")
    w2 = Warehouse("Warehouse B")
    manager.add_warehouse(w1)
    manager.add_warehouse(w2)

    # Products
    laptop = manager.factory.create_product(ProductCategory.ELECTRONICS, "SKU1", "Laptop", 1200.0, 5, 10)
    apple = manager.factory.create_product(ProductCategory.GROCERY, "SKU2", "Apple", 1.0, 300, 100)

    # Add to warehouse
    w1.add_product(laptop, 5)
    w2.add_product(apple, 300)

    # Trigger alerts
    manager.check_and_replenish("SKU1")
