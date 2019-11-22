#包含有的方法有：合成zip 排序sort 切片 计数count


toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms" ]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell {X} different kinds of pizza!".format(X = num_pizzas))
pizzas = list(zip(prices,toppings))#合成
print(pizzas)
pizzas.sort()#排序
cheapest_pizza= pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]#切片 
print(three_cheapest)
num_two_dollar_slices = prices.count(2)#计数
print(num_two_dollar_slices)
