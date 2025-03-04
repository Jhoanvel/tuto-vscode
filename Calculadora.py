def sumar(x, y):
  """Suma dos números."""
  return x + y

def restar(x, y):
  """Resta dos números."""
  return x - y

def multiplicar(x, y):
  """Multiplica dos números."""
  return x * y

def dividir(x, y):
  """Divide dos números."""
  return x / y

print("Selecciona operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

while True:
  eleccion = input("Ingresa opción(1/2/3/4): ")

  if eleccion in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
      print("Entrada inválida. Por favor, ingresa números.")
      continue

    if eleccion == '1':
      print(num1, "+", num2, "=", sumar(num1, num2))

    elif eleccion == '2':
      print(num1, "-", num2, "=", restar(num1, num2))

    elif eleccion == '3':
      print(num1, "*", num2, "=", multiplicar(num1, num2))

    elif eleccion == '4':
      if num2 == 0:
        print("No se puede dividir entre cero.")
      else:
        print(num1, "/", num2, "=", dividir(num1, num2))

    break
  else:
    print("Opción inválida. Por favor, ingresa 1, 2, 3 o 4.")