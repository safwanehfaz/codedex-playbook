class Restaurant:
    def __init__(self, name="'Bob's Burgers'", category="American Diner", rating=4.7, delivery=False):
        self.name = name
        self.category = category
        self.rating = rating
        self.delivery = delivery

bobs_burgers = Restaurant()
print(vars(bobs_burgers))