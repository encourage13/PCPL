
import sys
#процедурное решение
def solve_biquadratic_equation():
    if a == 0:
        print("Это не биквадратное уравнение.")
        return
    d = b**2 - 4*a*c
    if d < 0:
        print("Уравнение не имеет действительных корней.")
    elif d == 0:
        x2 = -b / (2 * a)
        if x2 >= 0:
            x = x2**0.5
            print(f"Уравнение имеет один действительный корень: x = {x}")
            print(f"Уравнение имеет один действительный корень: x = -{x}")
        else:
            print("Уравнение не имеет действительных корней.")
    else:
        x2_1 = (-b + d**0.5) / (2 * a)
        x2_2 = (-b - d**0.5) / (2 * a)

        roots = []
        if x2_1 >= 0:
            roots.append(x2_1**0.5)
            roots.append(-x2_1**0.5)
        if x2_2 >= 0:
            roots.append(x2_2**0.5)
            roots.append(-x2_2**0.5)

        print("Действительные корни уравнения:")
        for root in sorted(list(set(roots))): # удаляем дубликаты и сортируем
          print(f"x = {root}")
# Объектно-ориентированное решение
class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            return "Это не биквадратное уравнение."

        d = self.b**2 - 4*self.a*self.c

        if d < 0:
            return "Уравнение не имеет действительных корней."
        elif d == 0:
            x2 = -self.b / (2 * self.a)
            if x2 >= 0:
                return f"Уравнение имеет один действительный корень: x = {x2**0.5}\nУравнение имеет один действительный корень: x = -{x2**0.5}"
            else:
                return "Уравнение не имеет действительных корней."
        else:
            x2_1 = (-self.b + d**0.5) / (2 * self.a)
            x2_2 = (-self.b - d**0.5) / (2 * self.a)

            roots = []
            if x2_1 >= 0:
                roots.extend([x2_1**0.5, -x2_1**0.5])
            if x2_2 >= 0:
                roots.extend([x2_2**0.5, -x2_2**0.5])

            result = "Действительные корни уравнения:\n"
            for root in sorted(list(set(roots))):
                result += f"x = {root}\n"
            return result

def get_coefficients():
    while True:
        try:
            if len(sys.argv) == 4:
                a = float(sys.argv[1])
                b = float(sys.argv[2])
                c = float(sys.argv[3])
            else:
                a = float(input("Введите коэффициент A: "))
                b = float(input("Введите коэффициент B: "))
                c = float(input("Введите коэффициент C: "))
            return a, b, c
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите действительные числа.")


if __name__ == "__main__":
    a, b, c = get_coefficients()

    print("Процедурное решение:")
    solve_biquadratic_equation()

    print("\nОбъектно-ориентированное решение:")
    equation = BiquadraticEquation(a, b, c)
    print(equation.solve())

