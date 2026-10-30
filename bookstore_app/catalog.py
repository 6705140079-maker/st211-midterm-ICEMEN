"""Product catalog: adding products and searching."""


class Catalog:
    def __init__(self):
        self.products = {}   # product_id -> {"title":..., "price":...}

    def add_product(self, product_id, title, price):
        self.products[product_id] = {"title": title, "price": price}

    def search(self, keyword):
        """Return product_ids whose title contains keyword, case-insensitively."""
        results = []

        for pid, info in self.products.items():
            if keyword.lower() in info["title"].lower():
                results.append(pid)

        return results
