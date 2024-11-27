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

// Caso 1: Bucle 'for' válido
// for ($i = 0; $i < 10; $i++) {
//     echo "Iteración: $i\n";
// }

// Caso 2: Bucle 'for' válido sin cuerpo explícito
for ($k = 0; $k < 5; $k++){
    echo "k = $k\n";
}

$doblar = fn($n) => $n * 2;
$triple = fn($x) => $x + 3;

?>