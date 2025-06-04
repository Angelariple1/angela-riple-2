def tipo_triangulo(a,b,c):
	if a==b==c:
		return "Equilatero"
	elif a==b or b==c or a==c:
		return "Isosceles"
	else:return "Escaleno"
	try:
		a=float(input("Lado A:"))
		b=float(input("Lado b:"))
		c=float(input("Lado c:"))

		if a+b>c and a+c>b and b+c>a:
			print("Tipo de triangulo:", tipo_triangulo(a,b,c))
		else:
			print("No es un triangulo valido.")

	except ValueError:
		print("Por favor,ingrese solo numero.")




