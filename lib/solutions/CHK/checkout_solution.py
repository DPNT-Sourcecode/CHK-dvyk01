
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus:str) -> int:
        price = {
            "A": 50, "B": 30, "C": 20, "D": 15
        }
        offers = {"A": (3,130), "B": (2,45)}

        counts = {"A": 0, "B": 0, "C": 0, "D": 0}
        for sku in skus:
            counts[sku] += 1

        total = 0
        for item, qty in counts.items():
            price_item = price[item]
            if item in offers:
                offer_qty, offer_price = offers[item]
                packs = qty // offer_qty
                remainder = qty % offer_qty
                total += packs * offer_price + remainder * price_item
            else:
                total += qty * price_item
        return total

