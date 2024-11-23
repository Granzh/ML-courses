n = int(input())

lambdas = dict()

for f in range(1, n+1):
    lambdas[f"f{f}"] = eval(input("Введите лямбда функции: "))

keys = list(lambdas.keys())

user_input = input("Введите выражение для функций: ")

for key in keys:
    user_input = user_input.replace(key, f"lambdas.get('{key}')")

print(eval(user_input))