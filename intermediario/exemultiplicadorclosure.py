#irei fazer um codigo que multiplica por 2,3 e 4 o valor que recebe, usando closure de funções

def multiplicador(multiplica):
    if multiplica == 2:
        def mult_valor2(valor):
                return int(2 * valor)
        return mult_valor2   
    if multiplica == 3:
        def mult_valor3(valor):
            return int(3* valor)
        return mult_valor3
    
    def mult_valor4(valor):
        return int(4*valor)
    return mult_valor4

#usando closure para os valores a seguir
valor1 = multiplicador(2)
valor2 = multiplicador(3)
valor3 = multiplicador(4)

#printando com as novas closures que chamam as novas funções 
print(f'valor duplicado de 3: {valor1(3)}')
print(f'valor triplicado de 3: {valor2(3)}')
print(f'valor quadriplicado de 3: {valor3(3)} ')