<?php
// Caso 1: Lista válida
$numeros = [1, 2, 3, 4];

// Caso 2: Lista válida asociativa
$colores = [
    "rojo" => "#FF0000",
    "verde" => "#00FF00",
    "azul" => "#0000FF"
];

// Caso 3: Lista válida multidimensional
$matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Caso 4: Error en la lista (coma faltante)
$malArray = [1, 2 3, 4]; // Error: Falta una coma entre 2 y 3

// Caso 5: Error en la lista asociativa (falta "=>")
$malAsociativo = [
    "amarillo" #FFFF00 // Error: Falta "=>"
];

// Caso 6: Error en lista vacía (válida en PHP pero podría generar errores lógicos)
$listaVacia = []; // Esto es válido, pero verifica si está vacía.



// Caso 1: Bucle 'for' válido
for ($i = 0; $i < 10; $i++) {
    echo "Iteración: $i\n";
}

// Caso 2: Bucle 'for' válido sin cuerpo explícito
for ($k = 0; $k < 5; $k++)
    echo "k = $k\n";


// Caso 3: Bucle 'for' con error (falta un punto y coma en la condición)
for ($a = 0 $a < 5; $a++) { // Error: falta ';' después de la inicialización
    echo "a = $a\n";
}

$doblar = fn($n) => $n * 2;
$triple = fn($x) => $x + 3;
// Palabra reservada "fn" mal escrita
$invalida4 = fun($x) => $x * 2;
// Uso incorrecto de operadores en la expresión
$invalida3 = fn($a, $b) => $a + * $b;

// Caso 4: Bucle 'for' con error (llave de cierre mal colocada)
for ($d = 0; $d < 2; $d++) {
    echo "d = $d\n"; // Error: llave de cierre faltante o mal colocada

?>