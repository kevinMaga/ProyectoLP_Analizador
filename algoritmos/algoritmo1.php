<?php
// Algoritmo de prueba para el analizador léxico


$numero1 = 10;
$numero2 = 20;
$numero3 = 5.5;
$Boolean = TRUE;
$Boolean2 = FALSE;
$nombre = "LeonardoParra";


if ($numero1 > $numero2) {
    echo "El número 1 es mayor que el número 2";
} else {
    echo "El número 2 es mayor o igual que el número 1";
}


$suma = $numero1 + $numero2;
$resta = $numero1 - $numero2;
$multiplicacion = $numero1 * $numero2;
$division = $numero1 / $numero2;
$modulo = $numero1 % $numero2;


while ($numero1 > 0) {
    $numero1--;
}


for ($i = 0; $i < 5; $i++) {
    echo "El valor de i es: $i";
}


class Persona {
    public $nombre;
    private $edad;

    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    public function obtenerNombre() {
        return $this->nombre;
    }
}


$persona = new Persona("Carlos", 25);


$cadenaHereda = <<<EOT
Esta es una cadena heredoc
que puede ocupar varias líneas
y se usa para cadenas largas.
EOT;

$cadenaNowdoc = <<<'EOT'
Este es un ejemplo de cadena nowdoc
que también puede ocupar varias líneas
pero no interpreta variables como en heredoc.
EOT;


function retornarTrue() {
    return TRUE;
}


$resultado = retornarValor();


switch ($numero3) {
    case 5.5:
        echo "El número es 5.5";
        break;
    case 10:
        echo "El número es 10";
        break;
    default:
        echo "El número no coincide con ningún caso";
}


try {

    if ($numero2 == 0) {
        throw new Exception("Division por cero");
    }
    $resultado = $numero1 / $numero2;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    echo "Este bloque siempre se ejecuta";
}


function sumar($a, $b) {
    return $a + $b;
}

$resultadoSuma = sumar(3, 7);


?>


