Algoritmo login_simulado
    Definir  usuario, contrasenia Como Cadena

	Para vuelta = 1  Hasta 3 Con Paso 1 Hacer
		Escribir 'Ingrese su Usuario:'
		Leer usuario
		Escribir 'Igrese su Contrase�a:'
		Leer contrasenia
        
		// usuario -> admin  contrase�a -> dificil123 &
		Si usuario = "admin" y contrasenia = "dificil123" Entonces
			Escribir 'Login exitoso. Bienvenido!'
			vuelta = 3
		SiNo
			Escribir 'Usuario o contrase�a incorrectos!'
		Fin Si
	Fin Para
FinAlgoritmo