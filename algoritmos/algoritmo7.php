<?php
// Ejemplo de una función incorporada en PHP (strlen)
$texto = "Hola Mundo";
$longitud = strlen($texto); // Función incorporada que devuelve la longitud de una cadena
$nombre = fgets(STDIN);  // Solicita al usuario que ingrese un valor desde la consola
echo "Hola, $nombre!";
echo "La longitud de '$texto' es: $longitud";

// Ejemplo de declaración if/else
$edad = 25;
if ($edad >= 18) {
    echo "Eres mayor de edad.";
} else {
    echo "Eres menor de edad.";
}

// Ejemplo de uso de un array
$frutas = array("Manzana", "Banano", "Cereza");
echo "La primera fruta es: " . $frutas[0];
echo "La segunda fruta es: " . $frutas[1];
echo "La tercera fruta es: " . $frutas[2];

// Operaciones aritméticas básicas
$a = 10;
$b = 5;
$suma = $a + $b;
$resta = $a - $b;
$multiplicacion = $a * $b;
$division = $a / $b;
$modulo = $a % $b;

echo "Suma: $suma";
echo "Resta: $resta<br>";
echo "Multiplicación: $multiplicacion";
echo "División: $division";
echo "Módulo: $modulo";

// Operadores de incremento y decremento
$contador = 5;
echo "Contador inicial: $contador";
$contador++; // Incremento
echo "Contador después de incremento: $contador";
$contador--; // Decremento
echo "Contador después de decremento: $contador";

// Operadores compuestos (+=, -=, *=, /=, %=)
$x = 10;
$x += 5; // $x = $x + 5
echo "Valor de x después de +=: $x";
$x -= 3; // $x = $x - 3
echo "Valor de x después de -=: $x";
$x *= 2; // $x = $x * 2
echo "Valor de x después de *=: $x";
$x /= 4; // $x = $x / 4
echo "Valor de x después de /=: $x";
$x %= 3; // $x = $x % 3
echo "Valor de x después de %=: $x";

// Indexación de un array asociativo
$persona = array("nombre" => "Juan", "edad" => 30, "ciudad" => "Madrid");
echo "Nombre: " . $persona["nombre"];
echo "Edad: " . $persona["edad"];
echo "Ciudad: " . $persona["ciudad"];

?>