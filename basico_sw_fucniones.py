menu = int(input("digite del 1 al 3 para saber que tiene el menu"))
# lo mas similar a casos en  otros lenguajes de progrmacion


def casos(menu):
    match menu:
        case 1:
            return "somos positivos"
        case 2:
            return "somos buenos"


print(" el resultado es ", casos(menu))
