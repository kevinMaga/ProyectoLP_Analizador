<?php
// Inicio Ariana Gonzabay

// Diccionario
$diccionario = [
    "nombre" => "Ariana",
    "edad" => 22,
    "universidad" => "ESPOL"
];
print_r($diccionario);
echo "\n";

// Estructura While
$contador = 0;
while $contador < 3 {
    echo "Contador: $contador\n";
    $contador++;
}

// Condición simple
$numero1 = 5;
$numero2 = 10;
if ($numero1 < $numero2) {
    echo "$numero1 es menor que $numero2\n";
}

// Condición compleja
$numero3 = 15;
if ($numero1 < $numero2  $numero2 < $numero3) {
    echo "$numero1 es menor que $numero2 y $numero2 es menor que $numero3\n";
}

// Función anónima
$saludar = function$nombre {
    echo "Hola, $nombre!\n";
};
$saludar("Ariana");

// Impresión con múltiples argumentos
echo "Impresión con múltiples argumentos:\n";
echo "Este es un mensaje con varios argumentos\n";

// Solicitud de datos
echo "Ingrese su nombre: ";
$nombre = readline();
echo "Hola, $nombre!\n"

// Fin Ariana Gonzabay
?>
