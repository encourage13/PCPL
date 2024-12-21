package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func solveQuadratic(a, b, c float64) {
	discriminant := b*b - 4*a*c
	fmt.Printf("Дискриминант: %.2f\n", discriminant)

	switch {
	case discriminant < 0:
		fmt.Println("Уравнение не имеет действительных корней.")
	case discriminant == 0:
		x := -b / (2 * a)
		fmt.Printf("Уравнение имеет один корень: x = %.2f\n", x)
	default:
		x1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		x2 := (-b - math.Sqrt(discriminant)) / (2 * a)
		fmt.Printf("Уравнение имеет два корня: x1 = %.2f, x2 = %.2f\n", x1, x2)
	}
}

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Ошибка: укажите коэффициенты A, B и C в командной строке.")
		return
	}

	a, _ := strconv.ParseFloat(os.Args[1], 64)
	b, _ := strconv.ParseFloat(os.Args[2], 64)
	c, _ := strconv.ParseFloat(os.Args[3], 64)

	solveQuadratic(a, b, c)
}
