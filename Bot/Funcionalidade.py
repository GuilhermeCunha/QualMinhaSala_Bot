import string

import requests
import urllib.request
import json
from DateTime import DateTime
from datetime import datetime, timezone
from pytz import timezone

data_e_hora_atual = datetime.now()
fuso_horario = timezone('America/Bahia')
data_e_hora_atual_bahia = data_e_hora_atual.astimezone(fuso_horario)
horaAtual = data_e_hora_atual_bahia.strftime('%H:%M')


data_e_hora_atual = datetime.now()
#zona = datetime.timetz(data_e_hora_atual)
#data_e_hora_atual_bahia = data_e_hora_atual.astimezone(zona)
horaAtual = data_e_hora_atual_bahia.strftime('%H:%M')

dataUTC = datetime.now(timezone('UTC'))
dataBahia = dataUTC.astimezone(timezone('America/Bahia'))
horaBahia = dataBahia.strftime('%H:%M')
print(horaBahia)

Usuarios = []
RAs = []



