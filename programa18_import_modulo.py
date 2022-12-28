#!/usr/bin/python
#Importando módulo de outro diretório com o módulo sys

import sys
sys.path.append('/usr/senai/')

import fibo
fibo.fib(100)
