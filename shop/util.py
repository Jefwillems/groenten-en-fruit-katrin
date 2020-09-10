class ItemCounter:

    def __init__(self, order):
        """

        :param order: the order of type: shop.models.ShoppingCart
        """
        self.item_amounts = {}
        for shoppingcartitem in order.shoppingcartitem_set.all():
            amount = shoppingcartitem.amount
            item_name = shoppingcartitem.product.name
            if item_name in self.item_amounts:
                amount += self.item_amounts[item_name]
            self.item_amounts[item_name] = amount

    def merge(self, other: 'ItemCounter'):
        for name, amount in other.item_amounts.items():
            if name in self.item_amounts:
                self.item_amounts[name] += amount
            else:
                self.item_amounts[name] = amount
        return self
