<?php
//Kevin Magallanes
// Ejemplo 1: Operaciones matemáticas básicas
$numero1 = 5;
$numero2 = 3;
$resultado = $numero1 + $numero2; // Suma
echo "Resultado de la suma: " . $resultado;

// Ejemplo 2: Condicional IF
$edad = 20;
if ($edad >= 18) {
    echo "Eres adulto";
} else {
    echo "Eres menor de edad";
}

// Ejemplo 3: Bucle FOR
for ($i = 0; $i < 5; $i++) {
    echo "El valor de i es: " . $i . "\n";
}

// Ejemplo 4: Función simple
function saludo($nombre) {
    return "Hola, " . $nombre;
}

echo saludo("Juan");

// Ejemplo 5: Array y acceso a sus elementos
$colores = array("Rojo", "Verde", "Azul");
echo $colores[1]; // Acceso a elemento 'Verde'

// Ejemplo 6: Uso de arrays asociativos
$persona = array("nombre" => "Carlos", "edad" => 30);
echo "Nombre: " . $persona["nombre"] . ", Edad: " . $persona["edad"];
//Kevin Magallanes
?>