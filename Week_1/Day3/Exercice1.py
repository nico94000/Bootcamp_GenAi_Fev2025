class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
            
cat_1 = Cat("Sara", 2)
cat_2 = Cat("Micka", 4)
cat_2 = Cat("Olga", 8)

def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

oldest_cat = find_oldest_cat([cat1, cat2, cat3])

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
