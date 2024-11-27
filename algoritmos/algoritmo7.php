<?php
// Ejemplo de una función incorporada en PHP (strlen)
$texto = "Hola Mundo";
$longitud = strlen ($texto); // Función incorporada que devuelve la longitud de una cadena
// Ejemplo de declaración if/else
$edad = 25;
if($edad >= 18) {
    echo "Eres mayor de edad.\n";
} else {
    echo "Eres menor de edad.\n";
}
// Ejemplo de uso de un array
$frutas =array("Manzana","Banano","Cereza");
// Operaciones aritméticas básicas
$a = 10;
$b = 5;
$suma = $a + $b;
$resta = $a - $b;
$multiplicacion = $a * $b;
$division = $a / $b;
$modulo = $a % $b;

// Operadores de incremento y decremento
$contador = 5;
$contador++; // Incremento
$contador--; // Decremento

// Indexación de un array asociativo
echo $frutas[0]; // Imprimirá: manzana

?>