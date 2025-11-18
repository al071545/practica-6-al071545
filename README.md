# Práctica 6 Marco Teórico — Cálculo de Caudal usando la Fórmula de Manning
## Juan Pablo Javier Morales - 71545


## Introducción

- El flujo de agua en canales abiertos es un tema fundamental en la Ingeniería Civil, especialmente en el diseño de sistemas hidráulicos como canales de riego, drenaje, alcantarillado pluvial y ríos artificiales. Para estimar la velocidad y el caudal del agua en estos conductos, una de las fórmulas más utilizadas es la Ecuación de Manning.

- Este programa en Python implementa una interfaz gráfica (Tkinter) que permite calcular el caudal de un canal trapezoidal ingresando solo unos cuantos datos, facilitando el proceso para estudiantes y principiantes.


---

## ¿Qué es el caudal?

El caudal (Q) es la cantidad de agua que pasa por una sección de un canal por unidad de tiempo.

 Su unidad es: m³/s (metros cúbicos por segundo)

##  Sección hidráulica del canal

Este programa trabaja con un canal trapezoidal, muy común en ingeniería.
La geometría depende de:
a → Base superior (m)
b → Base inferior (m)
h → Profundidad del agua (m)

## 2.1 Área hidráulica (A)

Es el área mojada por el agua.

A=(h){(a+b)/2}
	​

## Perímetro mojado (P)

Es la longitud del contorno en contacto con el agua.

𝑃=𝑎+𝑏+2𝐿
Donde:
𝐿=√[ℎ² +{(𝑏−𝑎²)/2}]


##  Radio hidráulico (R)

El radio hidráulico relaciona el área con el perímetro mojado.
𝑅=𝐴/𝑃
	
Un radio hidráulico mayor significa menos fricción y mejor flujo.

##  La Ecuación de Manning

La fórmula de Manning permite calcular el caudal Q en canales abiertos:

𝑄=(1/𝑛)(𝐴)(𝑅^2/3)(𝑆^1/2)
Donde:

Q → Caudal (m³/s)

n → Coeficiente de rugosidad

A → Área hidráulica (m²)

R → Radio hidráulico (m)

S → Pendiente del canal (adimensional)
## Coeficiente de rugosidad (n)

El valor n representa qué tan “rugoso” es el material del canal.
A mayor rugosidad, menor será la velocidad del agua.

El programa incluye una tabla:

Tipo de canal	              n
Tubería PVC/PEAD          	0.013
Concreto nuevo	            0.015
Concreto desgastado        	0.017
Tierra (buen estado)	      0.020
Tierra (mal estado)       	0.025
## ¿Cómo funciona el programa?

El programa usa una interfaz gráfica creada con Tkinter, donde el usuario:
Ingresa:
Base superior (a)
Base inferior (b)
Profundidad (h)
Pendiente (S)
Selecciona el tipo de canal (para obtener el valor de n)
Da clic en Calcular
El programa:
Calcula A, P, R y Q usando las fórmulas anteriores
Muestra los resultados en pantalla
## Objetivo del programa

Este programa sirve para:
-Aprender el uso de la fórmula de Manning
-Visualizar cómo cambian los resultados al modificar el canal
-Automatizar cálculos que normalmente requieren tiempo
-Trabajar con una interfaz sencilla e intuitiva