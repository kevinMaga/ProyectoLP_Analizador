<?php
// Algoritmo de prueba para el analizador léxico
//Inicio Ariana Gonzabay

// Probando diferentes tipos de comentarios
// Este es un comentario de una línea
# Este es un comentario tipo shell
/* Este es un comentario 
   de múltiples líneas  */

declare(strict_types=1);

abstract class ClaseBase {
    abstract public function metodoAbstracto();
}

final class ClaseFinal {
    final public function metodoFinal() {
        return "No se puede sobrescribir";
    }
}

interface InterfazBase {
    public function metodo();
}

trait CaracteristicaUno {
    public function metodoUno() {
        echo "Método uno";
    }
}

trait CaracteristicaDos {
    public function metodoUno() {
        echo "Método uno";
    }
}

class ClaseCompleta extends ClaseBase implements InterfazBase {
    use CaracteristicaUno, CaracteristicaDos {
        CaracteristicaDos::metodoUno insteadof CaracteristicaUno;
        CaracteristicaUno::metodoUno as metodoOriginal;
    }

    public function metodoAbstracto() {
        return "Implementación del método abstracto";
    }
    
    public function metodo() {
        return "Implementación del método de interfaz";
    }
}

class ClaseConVar {
    var $propiedadAntigua = "estilo antiguo";
    
    public function aceptarCallable(callable $funcion) {
        $funcion();
    }
}
$objeto = new ClaseConVar();

$a = true;
$b = false;

if ($a and $b) {
    echo "Verdadero con AND";
} elseif ($a or $b) {
    echo "Verdadero con OR";
} elseif ($a xor $b) {
    echo "Verdadero con XOR";
}

$array = [1, 2, 3];
foreach ($array as $valor):
    echo $valor;
endforeach;

$condicion = true;
while ($condicion):
    $condicion = false;
endwhile;

for ($i = 0; $i < 10; $i++):
    // código
endfor;

if ($condicion):
    // código
endif;

$variable = 1;
switch ($variable):
    case 1:
        // código
        break;
    default:
        // código
endswitch;

inicio:
echo "Inicio";
goto fin;
echo "Medio";
fin:
echo "Fin";

global $variable_global;

$var = "";
if (empty($var)) {
    echo "Variable vacía";
}
if (isset($var)) {
    echo "Variable definida";
}
unset($var);

$error = false;
if ($error) {
    die("Error fatal");
    exit("Saliendo del script");
}

eval('$x = 5;');


list($uno, $dos) = array(1, 2);

$valor = 1;
$resultado = match($valor) {
    1 => "uno",
    2 => "dos",
    default => "otro"
};

$original = new ClaseCompleta();
$clon = clone $original;
if ($clon instanceof ClaseCompleta) {
    echo "Instancia de ClaseCompleta";
}

$multiplicar = fn($x) => $x * 2;

function generador() {
    yield 1;
    yield 2;
    yield from [3, 4, 5];
}

try {
    //codigo
} finally {
    //codigo
}

$comparacion = ($a <> $b);

// Probando delimitadores
$texto = "Hola, soy Ariana";

// Delimitador /
if (preg_match('/Ariana/', $texto)) {
    echo "Encontrado el delimitador /.<br>";
}

// Delimitador #
if (preg_match('#Ariana#', $texto)) {
    echo "Encontrado el delimitador #.<br>";
}

// Delimitador ~
if (preg_match('~Ariana~', $texto)) {
    echo "Encontrado el delimitador ~.<br>";
}

// Delimitador []
if (preg_match('[Ariana]', $texto)) {
    echo "Encontrado el delimitador [].<br>";
}

// Delimitador {}
if (preg_match('{Ariana}', $texto)) {
    echo "Encontrado el delimitador {}.<br>";
}

// Delimitador ()
if (preg_match('(Ariana)', $texto)) {
    echo "Encontrado el delimitador ().<br>";
}

// Delimitador <>
if (preg_match('<Ariana>', $texto)) {
    echo "Encontrado el delimitador <>.<br>";
}

//Fin Ariana Gonzabay
?>