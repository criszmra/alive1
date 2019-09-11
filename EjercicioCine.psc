Proceso sin_titulo
	//inputs
	escribir "Clasificacion de cine"
	escribir "Cuantos años tienes?"
	leer edad 
	Escribir ""
	Escribir "Puede ver peliculas clasificacion:"
	
	
	//proceso
	Si edad < 1
		Escribir "Edad incorrecta"
	SiNo
		Si edad >= 1 && edad < 13
			escribir "A"
		SiNo 
			Si edad >= 13 && edad < 18
				Escribir "B"
			Sino 
				Si edad >= 18
					Escribir "C"
				FinSi
			FinSi
		FinSi
	finsi
FinProceso
