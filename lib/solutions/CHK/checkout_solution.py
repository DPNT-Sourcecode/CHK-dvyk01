from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus:str) -> int:
        price = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40
        }
        offers = {
            "A":[
                {"qty": 5, "price": 200},
                {"qty": 3, "price": 130}
            ],
            "B": [{"qty": 2, "price": 45}]}
        free_items = [ {"trigger_item": "E", "free_item": "B", "trigger_qty": 2, "free_qty": 1}]
        counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
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
        for item, qty in payable.items():
            price_item = price[item]
            bundles = offers.get(item, [])
            if not offers:
                total += qty * price_item
                continue
            bundles_sort = sorted(bundles, key=lambda x: x["qty"], reverse=True)
            print(bundles_sort)
            remaining = qty
            for bundle in bundles_sort:
                print(bundle)
                bundle_qty = bundle["qty"]
                bundle_price = bundle["price"]
                num_bundle = remaining // bundle_qty
                if num_bundle > 0:
                    total += num_bundle * bundle_price
                    remaining -= num_bundle * bundle_qty
            if remaining > 0:
                total += remaining * price_item
        return total