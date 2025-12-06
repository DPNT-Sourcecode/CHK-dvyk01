from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus:str) -> int:
        price = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35,
            "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50
        }
        offers = {
            "A":[
                {"qty": 5, "price": 200},
                {"qty": 3, "price": 130}
            ],
            "B": [{"qty": 2, "price": 45}],
            "H": [
                {"qty": 10, "price": 80},
                {"qty": 5, "price": 45}
            ],
            "K": [{"qty": 2, "price": 120}],
            "P": [{"qty": 5, "price": 200}],
            "Q": [{"qty": 3, "price": 80}],
            "V": [
                {"qty": 3, "price": 130},
                {"qty": 2, "price": 90}
            ]
        }
        free_items = [
            {"trigger_item": "E", "free_item": "B", "trigger_qty": 2, "free_qty": 1},
            {"trigger_item": "F", "free_item": "F", "trigger_qty": 3, "free_qty": 1},
            {"trigger_item": "N", "free_item": "M", "trigger_qty": 3, "free_qty": 1},
            {"trigger_item": "R", "free_item": "Q", "trigger_qty": 3, "free_qty": 1},
            {"trigger_item": "U", "free_item": "U", "trigger_qty": 4, "free_qty": 1}
        ]
        counts = {k: 0 for k in price.keys()}
        if skus is None: return -1
        for sku in skus:
            if sku not in price:
                return -1
            counts[sku] += 1

        payable = counts.copy()
        for offer in free_items:
            trigger = offer["trigger_item"]
            free = offer["free_item"]
            trigger_qty = offer["trigger_qty"]
            free_qty = offer["free_qty"]
            num_trigger = payable.get(trigger, 0) // trigger_qty
            total_free = num_trigger * free_qty
            if total_free <=0: continue
            if free in payable:
                payable[free] = max(0, payable[free] - total_free)

        total = 0
        group_skus = ["S", "T", "X", "Y", "Z"]
        total_groups_items = sum(payable[sku] for sku in group_skus)

        for item, qty in payable.items():
            price_item = price[item]
            bundles = offers.get(item, [])
            if not bundles:
                total += qty * price_item
                continue
            bundles_sort = sorted(bundles, key=lambda x: x["qty"], reverse=True)
            remaining = qty
            for bundle in bundles_sort:
                bundle_qty = bundle["qty"]
                bundle_price = bundle["price"]
                num_bundle = remaining // bundle_qty
                if num_bundle > 0:
                    total += num_bundle * bundle_price
                    remaining -= num_bundle * bundle_qty
            if remaining > 0:
                total += remaining * price_item
        return total

