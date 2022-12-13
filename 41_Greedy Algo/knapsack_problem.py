
class Item:
    def __init__(self,weight,value) -> None:
        self.weight=weight
        self.value = value
        self.ratio = value/weight

def knapsack(capacity,items):
    usedCapacity = 0
    value = 0
    items.sort(key=lambda item:item.ratio,reverse=True)

    for item in items:
        if item.weight + usedCapacity <= capacity:
            value+=item.value
            usedCapacity+=item.weight
        else:
            remaining = capacity - usedCapacity
            value+=remaining*item.ratio
            usedCapacity+=remaining

        if usedCapacity==capacity:
            break

    print("Total Value is " + str(value))

i1 = Item(20,100)
i2 = Item(30,120)
i3 = Item(10,60)
items = [i1,i2,i3]
knapsack(50,items)