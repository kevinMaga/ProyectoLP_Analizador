import ply.yacc as yacc
import datetime
import os
from Lexico_analizador import tokens, lexer

d_variables = {}
errores_semanticos = []

usuario_git_global = None

