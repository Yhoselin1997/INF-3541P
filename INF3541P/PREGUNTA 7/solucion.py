from __future__ import print_function
from pyswip import Prolog, registerForeign

prolog = Prolog()

# Definir relaciones familiares en Prolog
prolog.assertz("padre(matiasa, olga)")
prolog.assertz("abuela(tiburscio, olga)")
prolog.assertz("madre(olga, yhoselin)")
prolog.assertz("tio(rene, yhoselin)")
prolog.assertz("tia(raquel, yhoselin)")
prolog.assertz("primo(monica, yhoselin)")
prolog.assertz("primo(cristian, yhoselin)")

# Definir consultas
print(list(prolog.query("padre(P, Hijo)")))
print(list(prolog.query("madre(M, Hija)")))
print(list(prolog.query("abuela(Abuela, Nieta)")))
print(list(prolog.query("tio(Tio, Sobrino)")))
print(list(prolog.query("primo(Primo, PrimoHermano)")))
