family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name} doit payer {price} $")
    total_cost += price
    print(f"Coût total pour la famille : {total_cost} $")
    
