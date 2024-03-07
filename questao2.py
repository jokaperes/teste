def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

numero = int(input("Digite um número: "))

n_esimo_numero = fibonacci(numero)

if numero == n_esimo_numero:
  print(f"O número {numero} pertence a sequência Fibonacci.")
else:
  print(f"O número {numero} não pertence a sequência Fibonacci.")
