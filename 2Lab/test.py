import os
import sys

sys.path.insert(0, '/app/geometric_lib')

try:
    import square
    import circle 
except ImportError:
    print("Ошибка: не удалось импортировать библиотеку geometric_lib")
    sys.exit(1)


try:
    side = float(os.environ.get('SIDE', 0))
except ValueError:
    print("Ошибка: Значение стороны должно быть числом!")
    sys.exit(1)

try:
    radius = float(os.environ.get('RADIUS', 0))
except ValueError:
    print("Ошибка: Значение радиуса должно быть числом!")
    sys.exit(1)


print(f"--- Геометрический калькулятор ---")
print(f"Данные квадрата: сторона = {side}")
print(f"Данные круга: радиус = {radius}")

if side <= 0:
    print("Внимание: для корректного расчета сторона должна быть больше нуля ($$x > 0$$).")
else:
    
    square_area = square.area(side)
    square_perimeter = square.perimeter(side)
    
    print(f"Площадь квадрата: {square_area}")
    print(f"Периметр квадрата: {square_perimeter}")

if radius <= 0:
    print("Внимание: для корректного расчета радиус должен быть больше нуля ($$x > 0$$).")
else:
    
    circle_area = circle.area(radius)
    circle_perimeter = circle.perimeter(radius)
    
    print(f"Площадь круга: {circle_area}")
    print(f"Периметр круга: {circle_perimeter}")

print("\nРасчет окончен.")
input("Нажмите Enter, чтобы выйти из контейнера...") 
