<?php
// Función para comparar el resultado esperado y el real
//Kevin Magallanes
function verificar($operacion, $resultadoEsperado, $resultadoReal) {
    echo "Prueba de $operacion: ";
    if ($resultadoEsperado === $resultadoReal) {
        echo "Correcto (Resultado: $resultadoReal)\n";
    } else {
        echo "Incorrecto (Esperado: $resultadoEsperado, Obtenido: $resultadoReal)\n";
    }
}

// Variables para prueba
$a = 10;
$b = 5;

// Pruebas para operadores aritméticos
verificar('Suma (+)', 15, $a + $b);
verificar('Resta (-)', 5, $a - $b);
verificar('Multiplicación (*)', 50, $a * $b);
verificar('División (/)', 2, $a / $b);
verificar('Módulo (%)', 0, $a % $b);

// Pruebas para operadores de incremento y decremento
$incrementoPost = $a;
$incrementoPre = ++$a;
verificar('Incremento postfijo (a++)', 10, $incrementoPost);
verificar('Incremento prefijo (++a)', 11, $incrementoPre);

$decrementoPost = $b;
$decrementoPre = --$b;
verificar('Decremento postfijo (b--)', 5, $decrementoPost);
verificar('Decremento prefijo (--b)', 4, $decrementoPre);

// Pruebas para operadores lógicos
$verdadero = true;
$falso = false;
verificar('AND lógico (&&)', false, $verdadero && $falso);
verificar('OR lógico (||)', true, $verdadero || $falso);
verificar('NOT lógico (!)', false, !$verdadero);
verificar('AND palabra (and)', false, $verdadero and $falso);
verificar('OR palabra (or)', true, $verdadero or $falso);
verificar('XOR palabra (xor)', true, $verdadero xor $falso);

// Pruebas para operadores de asignación
$x = 10;
$y = 5;
$x += $y;
verificar('Asignación con suma (+=)', 15, $x);

$x -= $y;
verificar('Asignación con resta (-=)', 10, $x);

$x *= $y;
verificar('Asignación con multiplicación (*=)', 50, $x);

$x /= $y;
verificar('Asignación con división (/=)', 10, $x);

$x %= $y;
verificar('Asignación con módulo (%=)', 0, $x);

// Pruebas para operadores de comparación
$a = 10;
$b = 5;
verificar('Igualdad (==)', false, $a == $b);
verificar('Identidad (===)', false, $a === $b);
verificar('Diferente (!=)', true, $a != $b);
verificar('No idéntico (!==)', true, $a !== $b);
verificar('Mayor que (>)', true, $a > $b);
verificar('Menor que (<)', false, $a < $b);
verificar('Mayor o igual que (>=)', true, $a >= $b);
verificar('Menor o igual que (<=)', false, $a <= $b);
// Fin Kevin Magallanes
?>