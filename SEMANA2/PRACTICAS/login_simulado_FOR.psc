Algoritmo login_simulado
    Definir  usuario, contrasenia Como Cadena

	Para vuelta = 1  Hasta 3 Con Paso 1 Hacer
		Escribir 'Ingrese su Usuario:'
		Leer usuario
		Escribir 'Igrese su Contraseņa:'
		Leer contrasenia
        
		// usuario -> admin  contraseņa -> dificil123 &
		Si usuario = "admin" y contrasenia = "dificil123" Entonces
			Escribir 'Login exitoso. Bienvenido!'
			vuelta = 3
		SiNo
			Escribir 'Usuario o contraseņa incorrectos!'
		Fin Si
	Fin Para
FinAlgoritmo