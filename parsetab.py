
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AND_LOGICAL AND_WORD ARRAY ARRAY_POP ARRAY_PUSH ARROW AS BOOLEAN BREAK CALLABLE CASE CATCH CLASS CLONE CLOSEINTER COMA COMENTARIO_LINEA COMENTARIO_MULTILINEA COMENTARIO_SHELL COUNT DECLARE DECREMENT DEFAULT DELIM_FIN DELIM_INICIO DIE DIVIDE DIVIDE_ASSIGN DOBLEDIVIDE DOBLEPUNTO ECHO ELSE ELSEIF EMPTY ENDFOR ENDFOREACH ENDIF ENDSWITCH ENDWHILE EQUAL EVAL EXIT EXTENDS FGETS FINAL FINALLY FLOAT FN FOR FOREACH FUNCTION GLOBAL GOTO GREATER_EQUAL ID IDENTICAL IF IGUAL IMPLEMENTS INCLUDE INCREMENT INSTANCEOF INSTEADOF INTERFACE IN_ARRAY ISSET LBRACE LBRACKET LESS_EQUAL LIST LLLAVE LPAREN MATCH MAYOR MAYORIGUAL MENOR MENORIGUAL MENOR_MAYOR MINUS MINUS_ASSIGN MOD MODULO_ASSIGN NEW NOT_EQUAL NOT_IDENTICAL NOT_LOGICAL NUMBER NUMERAL OR OR_LOGICAL OR_WORD PLUS PLUS_ASSIGN POT PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOYCOMA RBRACE RBRACKET READLINE REQUIRE RETURN RLLAVE RPAREN SORT STATIC STRING STRLEN STRPOS SWITCH THROW TIMES TIMES_ASSIGN TRAIT TRY UNSET USE VAR VARIABLE VIRGULILLA WHILE XOR XOR_WORD YIELD YIELD_FROMinput : ID IGUAL FGETS LPAREN ID RPAREN PUNTOYCOMA\n    imprimir : PRINT LPAREN valor RPAREN PUNTOYCOMA\n             | PRINT LPAREN argumentos RPAREN PUNTOYCOMA\n    \n    argumentos : valor\n               | argumentos COMA valor\n    \n    solicitud_datos : READLINE LPAREN STRING RPAREN PUNTOYCOMA\n    indexacion : VARIABLE LBRACKET valor RBRACKET\n                  | VARIABLE LBRACKET valor RBRACKET PUNTOYCOMAnumero : NUMBER\n            | MINUS NUMBER\n            | FLOAT\n  \n    valor : NUMBER\n          | FLOAT\n          | STRING\n          | BOOLEAN\n          | VARIABLE\n    operadores : AND_LOGICAL\n                 | OR_LOGICAL\n    operadorAritmetico : PLUS\n                          | MINUS\n                          | TIMES\n                          | DIVIDE\n                          | MOD\n                          | POT\n     comparadorNum : MAYOR\n                      | MAYORIGUAL\n                      | MENOR\n                      | MENORIGUAL\n     comparador : EQUAL\n                 | NOT_IDENTICAL\n                 | NOT_EQUAL\n                 | IGUAL\n                 | IDENTICAL\n     comparaciones : comparacion  \n\t\t\t\t\t | comparacion operadores comparaciones\n\t comparacion :  VARIABLE comparadorNum VARIABLE \n            | valor comparador valor \n\t \n    condicion : condicion_simple\n              | condicion compuesta_logica condicion\n    \n    condicion_simple : valor comparador valor\n    \n    compuesta_logica : AND_LOGICAL\n                     | OR_LOGICAL\n    OperacionASIG : VARIABLE PLUS_ASSIGN NUMBER\n                    | VARIABLE MINUS_ASSIGN NUMBER\n                    | VARIABLE TIMES_ASSIGN NUMBER\n                    | VARIABLE DIVIDE_ASSIGN NUMBER\n                    | VARIABLE MODULO_ASSIGN NUMBER\n                    | VARIABLE PLUS_ASSIGN NUMBER PUNTOYCOMA\n                    | VARIABLE MINUS_ASSIGN NUMBER PUNTOYCOMA\n                    | VARIABLE TIMES_ASSIGN NUMBER PUNTOYCOMA\n                    | VARIABLE DIVIDE_ASSIGN NUMBER PUNTOYCOMA\n                    | VARIABLE MODULO_ASSIGN NUMBER PUNTOYCOMA\n    incrementoDecremento : VARIABLE INCREMENT\n                            | VARIABLE DECREMENT\n                            | VARIABLE INCREMENT PUNTOYCOMA\n                            | VARIABLE DECREMENT PUNTOYCOMA\n     operacion : VARIABLE operadorAritmetico VARIABLE\n                 | operacion operadorAritmetico operacion\n     operaciones : operacion\n                    | operacion PUNTOYCOMA\n                    | operacion operadorAritmetico operaciones \n                    | VARIABLE IGUAL operaciones array : VARIABLE IGUAL ARRAY LPAREN RPAREN PUNTOYCOMA\n            | VARIABLE IGUAL ARRAY LPAREN elementos RPAREN PUNTOYCOMA\n            | VARIABLE IGUAL LBRACKET RBRACKET PUNTOYCOMA\n            | VARIABLE IGUAL LBRACKET elementos RBRACKET PUNTOYCOMA\n  \n    lista : LBRACKET RBRACKET\n          | LBRACKET elementos RBRACKET\n    \n    elemento : valor\n             | lista\n             | clave_valor\n    \n    elementos : elemento\n              | elementos COMA elemento\n    \n    clave_valor : valor ARROW valor\n    \n    diccionario : LBRACE pares RBRACE\n    \n    pares : par\n          | pares COMA par\n    \n    par : STRING ARROW valor\n    estructurasControl : WHILE\n                        | IF\n                        | ELSE\n                        | FOR\n  \n    if : IF LPAREN comparaciones RPAREN LLLAVE declaraciones RLLAVE\n       | IF LPAREN VARIABLE RPAREN LLLAVE declaraciones RLLAVE\n     else : RLLAVE ELSE LLLAVE declaraciones RLLAVE\n          | ELSE LLLAVE declaraciones RLLAVE\n\n          \n    declaraciones : declaracion\n                  | declaraciones declaracion\n    \n    declaracion : IF\n                | asignacion\n                | ELSE\n                | operacion\n                | WHILE\n                | FOR\n                | funcioninbuilt\n    \n    asignacion : VARIABLE IGUAL valor PUNTOYCOMA\n                | VARIABLE IGUAL valor \n    \n    while : WHILE LBRACE condicion RBRACE bloque\n    \n    bloque : LBRACE instrucciones RBRACE\n    \n    instrucciones : instruccion\n                  | instrucciones instruccion\n    \n    instruccion : asignacion\n                | imprimir\n    \n    funcioninbuilt : funciones LPAREN operaciones RPAREN\n                   | funciones LPAREN RPAREN\n    \n    funciones : STRLEN\n                | STRPOS\n                | ARRAY_PUSH\n                | ARRAY_POP\n                | IN_ARRAY\n                | COUNT\n                | SORT\n    \n    funcion_anonima : FUNCTION LPAREN parametros RPAREN LBRACE instrucciones RBRACE\n    \n    parametros : STRING\n               | parametros COMA STRING\n    '
    
_lr_action_items = {'ID':([0,5,],[2,6,]),'$end':([1,8,],[0,-1,]),'IGUAL':([2,],[3,]),'FGETS':([3,],[4,]),'LPAREN':([4,],[5,]),'RPAREN':([6,],[7,]),'PUNTOYCOMA':([7,],[8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> ID IGUAL FGETS LPAREN ID RPAREN PUNTOYCOMA','input',7,'p_input','Sintactico_analizador.py',16),
  ('imprimir -> PRINT LPAREN valor RPAREN PUNTOYCOMA','imprimir',5,'p_imprimir','Sintactico_analizador.py',22),
  ('imprimir -> PRINT LPAREN argumentos RPAREN PUNTOYCOMA','imprimir',5,'p_imprimir','Sintactico_analizador.py',23),
  ('argumentos -> valor','argumentos',1,'p_argumentos','Sintactico_analizador.py',32),
  ('argumentos -> argumentos COMA valor','argumentos',3,'p_argumentos','Sintactico_analizador.py',33),
  ('solicitud_datos -> READLINE LPAREN STRING RPAREN PUNTOYCOMA','solicitud_datos',5,'p_solicitud_datos','Sintactico_analizador.py',43),
  ('indexacion -> VARIABLE LBRACKET valor RBRACKET','indexacion',4,'p_indexacion','Sintactico_analizador.py',50),
  ('indexacion -> VARIABLE LBRACKET valor RBRACKET PUNTOYCOMA','indexacion',5,'p_indexacion','Sintactico_analizador.py',51),
  ('numero -> NUMBER','numero',1,'p_numero','Sintactico_analizador.py',54),
  ('numero -> MINUS NUMBER','numero',2,'p_numero','Sintactico_analizador.py',55),
  ('numero -> FLOAT','numero',1,'p_numero','Sintactico_analizador.py',56),
  ('valor -> NUMBER','valor',1,'p_valor','Sintactico_analizador.py',61),
  ('valor -> FLOAT','valor',1,'p_valor','Sintactico_analizador.py',62),
  ('valor -> STRING','valor',1,'p_valor','Sintactico_analizador.py',63),
  ('valor -> BOOLEAN','valor',1,'p_valor','Sintactico_analizador.py',64),
  ('valor -> VARIABLE','valor',1,'p_valor','Sintactico_analizador.py',65),
  ('operadores -> AND_LOGICAL','operadores',1,'p_operadores','Sintactico_analizador.py',69),
  ('operadores -> OR_LOGICAL','operadores',1,'p_operadores','Sintactico_analizador.py',70),
  ('operadorAritmetico -> PLUS','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',76),
  ('operadorAritmetico -> MINUS','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',77),
  ('operadorAritmetico -> TIMES','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',78),
  ('operadorAritmetico -> DIVIDE','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',79),
  ('operadorAritmetico -> MOD','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',80),
  ('operadorAritmetico -> POT','operadorAritmetico',1,'p_operadorAritmetico','Sintactico_analizador.py',81),
  ('comparadorNum -> MAYOR','comparadorNum',1,'p_comparadorNum','Sintactico_analizador.py',87),
  ('comparadorNum -> MAYORIGUAL','comparadorNum',1,'p_comparadorNum','Sintactico_analizador.py',88),
  ('comparadorNum -> MENOR','comparadorNum',1,'p_comparadorNum','Sintactico_analizador.py',89),
  ('comparadorNum -> MENORIGUAL','comparadorNum',1,'p_comparadorNum','Sintactico_analizador.py',90),
  ('comparador -> EQUAL','comparador',1,'p_comparador','Sintactico_analizador.py',95),
  ('comparador -> NOT_IDENTICAL','comparador',1,'p_comparador','Sintactico_analizador.py',96),
  ('comparador -> NOT_EQUAL','comparador',1,'p_comparador','Sintactico_analizador.py',97),
  ('comparador -> IGUAL','comparador',1,'p_comparador','Sintactico_analizador.py',98),
  ('comparador -> IDENTICAL','comparador',1,'p_comparador','Sintactico_analizador.py',99),
  ('comparaciones -> comparacion','comparaciones',1,'p_comparaciones','Sintactico_analizador.py',104),
  ('comparaciones -> comparacion operadores comparaciones','comparaciones',3,'p_comparaciones','Sintactico_analizador.py',105),
  ('comparacion -> VARIABLE comparadorNum VARIABLE','comparacion',3,'p_comparacion','Sintactico_analizador.py',108),
  ('comparacion -> valor comparador valor','comparacion',3,'p_comparacion','Sintactico_analizador.py',109),
  ('condicion -> condicion_simple','condicion',1,'p_condicion','Sintactico_analizador.py',115),
  ('condicion -> condicion compuesta_logica condicion','condicion',3,'p_condicion','Sintactico_analizador.py',116),
  ('condicion_simple -> valor comparador valor','condicion_simple',3,'p_condicion_simple','Sintactico_analizador.py',125),
  ('compuesta_logica -> AND_LOGICAL','compuesta_logica',1,'p_compuesta_logica','Sintactico_analizador.py',132),
  ('compuesta_logica -> OR_LOGICAL','compuesta_logica',1,'p_compuesta_logica','Sintactico_analizador.py',133),
  ('OperacionASIG -> VARIABLE PLUS_ASSIGN NUMBER','OperacionASIG',3,'p_operacionesASIG','Sintactico_analizador.py',139),
  ('OperacionASIG -> VARIABLE MINUS_ASSIGN NUMBER','OperacionASIG',3,'p_operacionesASIG','Sintactico_analizador.py',140),
  ('OperacionASIG -> VARIABLE TIMES_ASSIGN NUMBER','OperacionASIG',3,'p_operacionesASIG','Sintactico_analizador.py',141),
  ('OperacionASIG -> VARIABLE DIVIDE_ASSIGN NUMBER','OperacionASIG',3,'p_operacionesASIG','Sintactico_analizador.py',142),
  ('OperacionASIG -> VARIABLE MODULO_ASSIGN NUMBER','OperacionASIG',3,'p_operacionesASIG','Sintactico_analizador.py',143),
  ('OperacionASIG -> VARIABLE PLUS_ASSIGN NUMBER PUNTOYCOMA','OperacionASIG',4,'p_operacionesASIG','Sintactico_analizador.py',144),
  ('OperacionASIG -> VARIABLE MINUS_ASSIGN NUMBER PUNTOYCOMA','OperacionASIG',4,'p_operacionesASIG','Sintactico_analizador.py',145),
  ('OperacionASIG -> VARIABLE TIMES_ASSIGN NUMBER PUNTOYCOMA','OperacionASIG',4,'p_operacionesASIG','Sintactico_analizador.py',146),
  ('OperacionASIG -> VARIABLE DIVIDE_ASSIGN NUMBER PUNTOYCOMA','OperacionASIG',4,'p_operacionesASIG','Sintactico_analizador.py',147),
  ('OperacionASIG -> VARIABLE MODULO_ASSIGN NUMBER PUNTOYCOMA','OperacionASIG',4,'p_operacionesASIG','Sintactico_analizador.py',148),
  ('incrementoDecremento -> VARIABLE INCREMENT','incrementoDecremento',2,'p_incrementoDecremento','Sintactico_analizador.py',153),
  ('incrementoDecremento -> VARIABLE DECREMENT','incrementoDecremento',2,'p_incrementoDecremento','Sintactico_analizador.py',154),
  ('incrementoDecremento -> VARIABLE INCREMENT PUNTOYCOMA','incrementoDecremento',3,'p_incrementoDecremento','Sintactico_analizador.py',155),
  ('incrementoDecremento -> VARIABLE DECREMENT PUNTOYCOMA','incrementoDecremento',3,'p_incrementoDecremento','Sintactico_analizador.py',156),
  ('operacion -> VARIABLE operadorAritmetico VARIABLE','operacion',3,'p_operacion','Sintactico_analizador.py',162),
  ('operacion -> operacion operadorAritmetico operacion','operacion',3,'p_operacion','Sintactico_analizador.py',163),
  ('operaciones -> operacion','operaciones',1,'p_operaciones','Sintactico_analizador.py',168),
  ('operaciones -> operacion PUNTOYCOMA','operaciones',2,'p_operaciones','Sintactico_analizador.py',169),
  ('operaciones -> operacion operadorAritmetico operaciones','operaciones',3,'p_operaciones','Sintactico_analizador.py',170),
  ('operaciones -> VARIABLE IGUAL operaciones','operaciones',3,'p_operaciones','Sintactico_analizador.py',171),
  ('array -> VARIABLE IGUAL ARRAY LPAREN RPAREN PUNTOYCOMA','array',6,'p_array','Sintactico_analizador.py',177),
  ('array -> VARIABLE IGUAL ARRAY LPAREN elementos RPAREN PUNTOYCOMA','array',7,'p_array','Sintactico_analizador.py',178),
  ('array -> VARIABLE IGUAL LBRACKET RBRACKET PUNTOYCOMA','array',5,'p_array','Sintactico_analizador.py',179),
  ('array -> VARIABLE IGUAL LBRACKET elementos RBRACKET PUNTOYCOMA','array',6,'p_array','Sintactico_analizador.py',180),
  ('lista -> LBRACKET RBRACKET','lista',2,'p_lista','Sintactico_analizador.py',187),
  ('lista -> LBRACKET elementos RBRACKET','lista',3,'p_lista','Sintactico_analizador.py',188),
  ('elemento -> valor','elemento',1,'p_elemento','Sintactico_analizador.py',195),
  ('elemento -> lista','elemento',1,'p_elemento','Sintactico_analizador.py',196),
  ('elemento -> clave_valor','elemento',1,'p_elemento','Sintactico_analizador.py',197),
  ('elementos -> elemento','elementos',1,'p_elementos','Sintactico_analizador.py',202),
  ('elementos -> elementos COMA elemento','elementos',3,'p_elementos','Sintactico_analizador.py',203),
  ('clave_valor -> valor ARROW valor','clave_valor',3,'p_clave_valor','Sintactico_analizador.py',216),
  ('diccionario -> LBRACE pares RBRACE','diccionario',3,'p_diccionario','Sintactico_analizador.py',225),
  ('pares -> par','pares',1,'p_pares','Sintactico_analizador.py',231),
  ('pares -> pares COMA par','pares',3,'p_pares','Sintactico_analizador.py',232),
  ('par -> STRING ARROW valor','par',3,'p_par','Sintactico_analizador.py',241),
  ('estructurasControl -> WHILE','estructurasControl',1,'p_estructurasControl','Sintactico_analizador.py',253),
  ('estructurasControl -> IF','estructurasControl',1,'p_estructurasControl','Sintactico_analizador.py',254),
  ('estructurasControl -> ELSE','estructurasControl',1,'p_estructurasControl','Sintactico_analizador.py',255),
  ('estructurasControl -> FOR','estructurasControl',1,'p_estructurasControl','Sintactico_analizador.py',256),
  ('if -> IF LPAREN comparaciones RPAREN LLLAVE declaraciones RLLAVE','if',7,'p_if','Sintactico_analizador.py',260),
  ('if -> IF LPAREN VARIABLE RPAREN LLLAVE declaraciones RLLAVE','if',7,'p_if','Sintactico_analizador.py',261),
  ('else -> RLLAVE ELSE LLLAVE declaraciones RLLAVE','else',5,'p_else','Sintactico_analizador.py',271),
  ('else -> ELSE LLLAVE declaraciones RLLAVE','else',4,'p_else','Sintactico_analizador.py',272),
  ('declaraciones -> declaracion','declaraciones',1,'p_declaraciones','Sintactico_analizador.py',280),
  ('declaraciones -> declaraciones declaracion','declaraciones',2,'p_declaraciones','Sintactico_analizador.py',281),
  ('declaracion -> IF','declaracion',1,'p_declaracion','Sintactico_analizador.py',285),
  ('declaracion -> asignacion','declaracion',1,'p_declaracion','Sintactico_analizador.py',286),
  ('declaracion -> ELSE','declaracion',1,'p_declaracion','Sintactico_analizador.py',287),
  ('declaracion -> operacion','declaracion',1,'p_declaracion','Sintactico_analizador.py',288),
  ('declaracion -> WHILE','declaracion',1,'p_declaracion','Sintactico_analizador.py',289),
  ('declaracion -> FOR','declaracion',1,'p_declaracion','Sintactico_analizador.py',290),
  ('declaracion -> funcioninbuilt','declaracion',1,'p_declaracion','Sintactico_analizador.py',291),
  ('asignacion -> VARIABLE IGUAL valor PUNTOYCOMA','asignacion',4,'p_asignacion','Sintactico_analizador.py',295),
  ('asignacion -> VARIABLE IGUAL valor','asignacion',3,'p_asignacion','Sintactico_analizador.py',296),
  ('while -> WHILE LBRACE condicion RBRACE bloque','while',5,'p_while','Sintactico_analizador.py',305),
  ('bloque -> LBRACE instrucciones RBRACE','bloque',3,'p_bloque','Sintactico_analizador.py',312),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','Sintactico_analizador.py',318),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','Sintactico_analizador.py',319),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','Sintactico_analizador.py',328),
  ('instruccion -> imprimir','instruccion',1,'p_instruccion','Sintactico_analizador.py',329),
  ('funcioninbuilt -> funciones LPAREN operaciones RPAREN','funcioninbuilt',4,'p_funcioninbuilt','Sintactico_analizador.py',340),
  ('funcioninbuilt -> funciones LPAREN RPAREN','funcioninbuilt',3,'p_funcioninbuilt','Sintactico_analizador.py',341),
  ('funciones -> STRLEN','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',346),
  ('funciones -> STRPOS','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',347),
  ('funciones -> ARRAY_PUSH','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',348),
  ('funciones -> ARRAY_POP','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',349),
  ('funciones -> IN_ARRAY','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',350),
  ('funciones -> COUNT','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',351),
  ('funciones -> SORT','funciones',1,'p_funcionesdefin','Sintactico_analizador.py',352),
  ('funcion_anonima -> FUNCTION LPAREN parametros RPAREN LBRACE instrucciones RBRACE','funcion_anonima',7,'p_funcion_anonima','Sintactico_analizador.py',360),
  ('parametros -> STRING','parametros',1,'p_parametros','Sintactico_analizador.py',366),
  ('parametros -> parametros COMA STRING','parametros',3,'p_parametros','Sintactico_analizador.py',367),
]
