import code.fibo
import code.factorial
import code.maxfactorial

print("Digite um número para imprimir a sequencia de Fibonacci e Calcular o Fatorial")

number = input()

#print(type(int(number)))
code.fibo.fib(int(number))
print('\n')
code.factorial.fact(int(number))

findMaxValue = code.maxfactorial.findMaxValue()

print("Maximum value of integer:",
                      findMaxValue);