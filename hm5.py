#Не до конца понял

goods = [
    (1, {"Name": "computer", "cost": 50000, "amount": 10, "unit": "thing"}),
    (2, {"Name": "scan", "cost": 10000, "amount": 4, "unit": "thing" }),
    (3, {"Name": "printer", "cost": 4000, "amount": 12, "unit": "thing"})
]

while input("Would you like add product? Yes/no: ") == 'yes':
    amount = int(input("Enter product amount: "))
    features = {"name": "computer"}
    while input("Would you like add product parameters? Yes/no: ") == 'yes':
        name = input("Enter name of product: ")
        cost = input("Enter cost of product: ")
        features[name] = cost
    goods.append(tuple([amount, features]))
print(goods)

analitics = {
    "Name": ["computer", "scan", "printer"],
    "cost": [50000, 10000, 4000],
    "amount": [10, 4, 12],
    "unit": ["thing"]
}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)