n = int(input())

functions = dict()

for f in range(1, n+1):
    func_lines = []
    
    func_str = input(f"Введите функцию f{f}: ")

    func_str = func_str.replace("[SEP]", "\n")

    functions[f"f{f}"] = exec(f"def f{f} {func_str}")

keys = list(functions.keys())

user_input = input("Введите выражение для функций: ")

for key in keys:
    user_input = user_input.replace(key, f"functions.get('{key}')()")

eval(user_input)