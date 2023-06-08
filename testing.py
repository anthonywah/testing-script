

PRICE_DICT = {
    'ProdA': 2.0, 
    'ProdB': 4.0
}


class Product:
    def __init__(self, name, qty):
        assert isinstance(name, str)
        assert name in PRICE_DICT.keys()
        assert isinstance(qty, int)
        self.name = name
        self.price = PRICE_DICT[self.name]
        self.qty = qty

# product_a = Product(name='A', price=0.5, qty=1)

class Cart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, product):
        if product.name not in self.cart:
            self.cart[product.name] = []
        self.cart[product.name].append(product)

    def print_summary(self):
        for k, v in self.cart.items():
            print(f'Product: {k}')
            for p in v:
                print(f'{p.qty} of {p.name} @ ${p.price}')

    def get_item_sum(self, product_name):
        """ Function to get sum of bill of one product type 
            and check items in cart and apply discount where applicable

            Returns total dollar amount to be billed for that product type
        """
        item_bill_sum = 0.
        v = self.cart.get(product_name)
        if product_name == 'ProdB':
            b_px = PRICE_DICT.get('ProdB')
            prod_qty_sum = sum([i.qty for i in v])
            discount_applicable = prod_qty_sum // 3
            remainder = prod_qty_sum % 3
            item_bill_sum += discount_applicable * 2 * b_px + (remainder * b_px)
            print(f'***** Discount applied! Original Amt: ${prod_qty_sum * b_px} ; New Amt ${item_bill_sum}:  *****')
        else:
            for p in v:
                item_bill_sum += (p.price * p.qty)
        return item_bill_sum
    
    def calc_bill(self):
        bill_sum = 0.
        for k, v in self.cart.items():
            bill_sum += self.get_item_sum(product_name=k)
        return bill_sum


def test(product_ls, expected):
    cart = Cart()
    for p in product_ls:
        p_obj = Product(name=p[0], qty=p[1])
        cart.add_to_cart(p_obj)
    cart.print_summary()
    bill_sum = cart.calc_bill()
    print(f'Test case {len(product_ls)} products {"Passed" if bill_sum == expected else "Failed"}')

        

if __name__ == '__main__':
    test_case_ls = [['ProdB', i] for i in range(8)]
    arg_ls = [
        [[test_case_ls[0]], 0], 
        [[test_case_ls[1]], 4], 
        [[test_case_ls[2]], 8], 
        [[test_case_ls[3]], 8], 
        [[test_case_ls[4]], 12], 
        [[test_case_ls[5]], 16], 
        [[test_case_ls[6]], 16], 
        [[test_case_ls[7]], 20], 
    ]
    
    for arg in arg_ls:
        test(product_ls=arg[0], expected=arg[1])


