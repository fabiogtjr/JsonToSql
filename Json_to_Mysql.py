# Importa biblioteca de Requests
import requests, pymysql.cursors, datetime

# Conecta com o Banco de Dados
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='banco',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# URL da API
URL = "https://urldaAPI.com.br"

# Cria o Header do token da API
HEADER = {'access-token': "chavedaAPI$"}

# envia o metodo get e salva as responses
r = requests.get(url=URL, headers=HEADER)

# extrai os dados no formato JSON
data = r.json()

#Grava no Banco os registros
for moto in data['employees']:
    try:
        with connection.cursor() as cursor:
            query = 'INSERT INTO `motoristas` (`id`, `nome`, `cpf`, `funcao`, `dia_ultimo_ponto`, `hora_ultimo_ponto`, `status_ultimo_ponto`, `tipo_jornada`, `polo`, `ultima_atualizacao`) VALUES (%s,"%s","%s",%s,"%s","%s",%s,%s,%s, CURRENT_TIMESTAMP)' % (
                moto['id'], moto['name'], moto['cpf'], moto['job_title']['id'],
                datetime.datetime.strptime(
                    moto['work_status_time_card']['date'],
                    "%d/%m/%Y").strftime("%Y-%m-%d"),
                moto['work_status_time_card']['time'],
                moto['work_status']['id'], moto['shift']['id'],
                moto['team']['id'])
            cursor.execute(query)
        connection.commit()
    except:
        pass
print('Script Carga Inicial Executado com Sucesso!')
