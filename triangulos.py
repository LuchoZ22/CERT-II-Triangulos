def triangulos(a, b, c): 
    if(a == b and b == c):
        print("EL TRIANGULO ES EQUILATERO")
    if (a == b or b == c or a == c):
        print("EL TRIANGULO ES ISÓCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")


def read_number(msg):
    while True:
        try:
            aux = float(input(msg))
            if(aux > 0):
                return aux
            else:
                print("ERROR: EL VALOR DEBE SER MAYOR A 0")
        except:
            print("ERROR: INGRESE UN VALOR NUMERICO")
        
        

def main():
    a = read_number("Lado 1: ")
    b = read_number("Lado 2: ")
    c = read_number("Lado 3: ")

    triangulos(a, b, c)

if __name__=="__main__":
    main()
    