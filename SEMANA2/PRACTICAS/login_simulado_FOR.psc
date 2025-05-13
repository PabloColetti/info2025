Algoritmo login_simulado
    Definir  usuario, contrasenia Como Cadena

	Para vuelta = 1  Hasta 3 Con Paso 1 Hacer
		Escribir 'Ingrese su Usuario:'
		Leer usuario
		Escribir 'Igrese su Contraseña:'
		Leer contrasenia
        
		// usuario -> admin  contraseña -> dificil123 &
		Si usuario = "admin" y contrasenia = "dificil123" Entonces
			Escribir 'Login exitoso. Bienvenido!'
			vuelta = 3
		SiNo
			Escribir 'Usuario o contraseña incorrectos!'
		Fin Si
	Fin Para
FinAlgoritmo