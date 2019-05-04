from datetime import datetime  #Pegar horário atual
import requests  # Pegar JSON do API do site
from unidecode import unidecode  # Tirar acentos de uma string
from datetime import datetime # Pegar o horário
from datetime import date # Pegar data
from pytz import timezone # Pegar o horário de um certo local

def resposta(ra):
    resp = 0
    try:
        url = "http://senaiweb.fieb.org.br/MinhaAula/api/aulas?ra=" + ra
        objeto = requests.get(url).json()
    except:
        return ("Error")
    try:

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
    except:
        return "Nenhuma aula hoje encontrada para o RA informado"

    nomeCurso = curso + '\n\n'

    if 'Tecnico em Manutencao Automotiva' in curso:
        retorno = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
    if 'Tecnico em Desenvolvimento de Sistemas' in curso:
        retorno = bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
    if 'Tecnico em Eletrotecnica' in curso:
        retorno = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal

    resp = (nomeCurso + retorno)



    if len(objeto) == 2:
        retorno = ""
        nomeProfessor = objeto[1]['professor']
        turno = objeto[1]['turno']
        codTurma = objeto[1]['codTurma']
        dtInicial = objeto[1]['dtInicial']
        dtFinal = objeto[1]['dtFinal']
        curso = unidecode(objeto[1]['curso'])
        disciplina = objeto[1]['disciplina']
        predio = objeto[1]['predio']
        bloco = objeto[1]['bloco']
        sala = objeto[1]['sala']
        data = objeto[1]['data']
        horaInicial = objeto[1]['horaInicial']
        horaFinal = objeto[1]['horaFinal']

        if 'Tecnico em Manutencao Automotiva' in curso:
            retorno2 = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
        if 'Tecnico em Desenvolvimento de Sistemas' in curso:
            retorno2 = bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal
        if 'Tecnico em Eletrotecnica' in curso:
            retorno2 = predio + " - " + bloco + " em " + sala + "\n" + horaInicial + " - " + horaFinal

        resp = (resp + "\n" + retorno2)


    return resp

def pegaHorario():
    dataUTC = datetime.now(timezone('UTC'))
    dataBahia = dataUTC.astimezone(timezone('America/Bahia'))
    horaBahia = dataBahia.strftime('%H:%M')
    return horaBahia
def pegaDia():
    DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]
    data_atual = date.today()
    indice_da_semana = data_atual.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    #numero_do_dia_da_semana = data_atual.isoweekday()
    return dia_da_semana

