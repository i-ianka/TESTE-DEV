print("###### Sequencia de Fibonacci ########")

def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Digite um numero: "))
if pertence_fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci!")
else:
    print(f"O numero {numero} NAO pertence a sequencia de Fibonacci!")
