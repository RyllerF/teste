def fibonacci(n):
    fibLs = [0, 1]
    while fibLs[-1] < n:
        fibLs.append(fibLs[-1] + fibLs[-2])
    return fibLs


def checa(numero, sequencia):
    if numero in sequencia:
        return f"O número {numero} pertence a sequencia de Fibonacci."
    else:
        return f"O número {numero} não pertence a sequencia de Fibonacci."

num = int(input('Digite o numero a ser checado: '))
sequencia_fibonacci = fibonacci(num)
print(checa(num, sequencia_fibonacci))
