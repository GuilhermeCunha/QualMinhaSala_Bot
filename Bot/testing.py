#!-*- conding: utf8 -*-
#coding: utf-8
import telepot
import requests
from unidecode import unidecode
import sys
Guilherme = "162.650331"
Davi = "162.650145"
Mehiel = "162.649695"

"""
url = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + Davi
objetoDavi = requests.get(url).json()
print(objetoDavi)
url2 = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + Guilherme
objetoGuilherme = requests.get(url2).json()
print(objetoGuilherme)
url3 = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + Mehiel
objetoMehiel = requests.get(url3).json()
print(objetoMehiel)
print("\n\n")
print("\n\n\n")
print(sys.stdout.encoding)
"""

Usuarios = []
try:
    ra = input("Seu ra: ")
    url = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + ra
    objeto = requests.get(url).json()

    Desenvolvimento = 'Técnico em Desenvolvimento de Sistemas'
    Eletrotecnica = 'Técnico em Eletrotécnica'
    Manutencao = 'Técnico em Manutenção Automotiva'

    nomeProfessor = objeto[0]['professor']
    turno = objeto[0]['turno']
    codTurma = objeto[0]['codTurma']
    dtInicial = objeto[0]['dtInicial']
    dtFinal = objeto[0]['dtFinal']
    curso = unidecode(objeto[0]['curso'])
    disciplina = objeto[0]['disciplina']
    predio = objeto[0]['predio']
    bloco = objeto[0]['bloco']
    sala = objeto[0]['sala']
    data = objeto[0]['data']
    horaInicial = objeto[0]['horaInicial']
    horaFinal = objeto[0]['horaFinal']
    print("curso : " + curso)
    nomeCurso = curso + '\n'

    if 'Tecnico em Manutençao Automotiva' in curso:
        retorno = (predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal)
    if 'Tecnico em Desenvolvimento de Sistemas' in curso:
        retorno = (bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal)
    if 'Tecnico em Eletrotecnica' in curso:
        retorno = (predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal)
    resp = (nomeCurso + retorno)

    print(resp)
except:
    print("Algum erro ocorreu, confira seu RA")