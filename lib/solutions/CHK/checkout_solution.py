
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        price = {
            "A": 50, "B": 30, "C": 15
        }
        offers = {"A": (3,130), "B": (2,45)}

        counts = {"A": 0, "B": 0, "C": 0}
        for sku in skus:
            counts[sku] += 1
        for item, qty in counts.items():
            