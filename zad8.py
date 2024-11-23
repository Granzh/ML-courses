import numpy as np
import matplotlib.pyplot as plt

def generate_array(*, N, A, B, D):
    # Генерируем массив с нормальным распределением
    mean = (A + B) / 2  # Среднее значение
    array = np.random.normal(mean, np.sqrt(D), N)
    
    # Ограничиваем значения интервалом [A, B]
    array = np.clip(array, A, B)
    
    # Сортируем массив
    array.sort()
    
    return array

def visualize_and_analyze(array, A, B):
    plt.figure(figsize=(10, 6))
    
    # Построение гистограммы
    plt.hist(array, bins=30, density=True, alpha=0.7, color='skyblue')
    plt.title('Распределение сгенерированных чисел')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    
    # Добавляем вертикальные линии для границ A и B
    plt.axvline(x=A, color='r', linestyle='--', label=f'A={A}')
    plt.axvline(x=B, color='g', linestyle='--', label=f'B={B}')
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Анализ данных
    print("\nАнализ сгенерированных данных:")
    print(f"Минимальное значение: {np.min(array):.2f}")
    print(f"Максимальное значение: {np.max(array):.2f}")
    print(f"Среднее значение: {np.mean(array):.2f}")
    print(f"Фактическая дисперсия: {np.var(array):.2f}")

# Пример использования
N, A, B, D = 1000, -5, 5, 2
array = generate_array(N=N, A=A, B=B, D=D)
visualize_and_analyze(array, A, B)

print("\nВыводы:")
print("1. Распределение имеет форму, близкую к нормальному, но ограничено интервалом [A, B]")
print("2. Фактическая дисперсия может отличаться от заданной из-за ограничения значений")
print("3. Среднее значение стремится к центру интервала [A, B]")
