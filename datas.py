from datetime import date
from datetime import datetime, timezone, timedelta

data_atual = date.today()
print(data_atual)

#
# A abordagem abaixo apresenta o problema de não incluir zeros à esquerda do dia e/ou do mês quando esse
# for menor que 10.
#
data_em_texto = ('{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year))
print(f'Data formatada: {data_em_texto}')

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(f'Data formatada com o método strftime: {data_em_texto}')

#
# Trabalhando com hora e data
#
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(f'Data e hora formatadas: {data_e_hora_em_texto}')

#
# Convertendo uma String em data e hora
#
data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(f'A data e hora obtidos a partir de uma String são {data_e_hora}')

#
# Trabalhando com fuso horário
#
data_e_hora_atuais = datetime.now()
#
# O parâmetro offset representa a diferença entre o fuso horário que queremos criar e o Tempo Universal
# Coordenado (UTC). No nosso caso, em São Paulo, temos uma diferença de -3 horas, mais conhecida como UTC-3.
# Não basta somente -3 como sendo essa diferença pois o timedelta entenderá como sendo -3 dias. É preciso
# especificar que são 3 horas a menos, passar esse valor ao construtor de timedelta e posteriormente utilizar
# esse resultado como argumento para um objeto do tipo timezone.
#
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

#
# Resolvendo o problema dos fusos horários com o pytz
#
from pytz import timezone
import pytz

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo') # Essa classe timezone é da biblioteca pytz
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(f'Data e hora gerados com pytz: {data_e_hora_sao_paulo_em_texto}')

#
# Imprimindo os fuso horários disponíveis através da classe timezone da biblioteca pytz
#
print('Lista de fuso horários disponíveis na biblioteca pytz\n')
for tz in pytz.all_timezones:
    print(tz)


