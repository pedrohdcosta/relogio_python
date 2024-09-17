from datetime import datetime, timedelta
 
# Função para calcular as horas trabalhadas
def calcular_horas_trabalhadas(inicio, fim):
    formato = "%H:%M"
    try:
        hora_inicio = datetime.strptime(inicio, formato)
        hora_fim = datetime.strptime(fim, formato)
 
        # Se o término for antes do início, considera como dia seguinte
        if hora_fim < hora_inicio:
            hora_fim += timedelta(days=1)
 
        diferenca = hora_fim - hora_inicio
        return diferenca
    except ValueError:
        return "Erro: Formato de horário inválido. Utilize HH:mm."
 
# Função para descontar o intervalo de almoço
def descontar_intervalo(horas_trabalhadas, intervalo):
    formato = "%H:%M"
    try:
        # Desconta o intervalo das horas trabalhadas
        horas_trabalhadas_timedelta = timedelta(hours=horas_trabalhadas.seconds // 3600, minutes=(horas_trabalhadas.seconds // 60) % 60)
        intervalo_timedelta = datetime.strptime(intervalo, formato) - datetime.strptime("00:00", formato)
        resultado_final = horas_trabalhadas_timedelta - intervalo_timedelta
        return resultado_final
    except ValueError:
        return "Erro: Formato de intervalo inválido. Utilize HH:mm."
 
# Função para calcular as horas com inversão (UC 3)
def calcular_horas_com_inversao(inicio, fim):
    return calcular_horas_trabalhadas(inicio, fim)
 
# Função para interpretar horários sem o separador ":"
def interpretar_horario_sem_separador(horario):
    try:
        if len(horario) == 3:  # Formato Hmm (e.g., 830)
            horas = int(horario[0])
            minutos = int(horario[1:])
        elif len(horario) == 4:  # Formato HHmm (e.g., 0830)
            horas = int(horario[:2])
            minutos = int(horario[2:])
        else:
            return "Erro: Horário inválido."
 
        return f"{horas:02}:{minutos:02}"
    except ValueError:
        return "Erro: Formato de horário inválido."
 
# Função principal para processar todos os casos
def main():
    print("=== Calculadora de Horas Trabalhadas ===")
    # Exemplo UC 1 - Inserir horário de início e término
    inicio = input("Insira o horário de início (HH:mm): ")
    fim = input("Insira o horário de término (HH:mm): ")
    horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
    if isinstance(horas_trabalhadas, timedelta):
        print(f"Horas trabalhadas: {horas_trabalhadas}")
    else:
        print(horas_trabalhadas)  # Mostra mensagem de erro, se houver
    # Exemplo UC 2 - Inserir intervalo de almoço
    intervalo = input("Insira o intervalo de almoço (HH:mm): ")
    if isinstance(horas_trabalhadas, timedelta):
        resultado_desconto_intervalo = descontar_intervalo(horas_trabalhadas, intervalo)
        print(f"Total de horas após desconto do intervalo: {resultado_desconto_intervalo}")
    else:
        print(horas_trabalhadas)  # Mostra mensagem de erro, se houver
    # Exemplo UC 3 - Inversão de horários
    inicio = input("Insira o horário de início para inversão (HH:mm): ")
    fim = input("Insira o horário de término para inversão (HH:mm): ")
    horas_com_inversao = calcular_horas_com_inversao(inicio, fim)
    if isinstance(horas_com_inversao, timedelta):
        print(f"Horas trabalhadas com inversão: {horas_com_inversao}")
    else:
        print(horas_com_inversao)  # Mostra mensagem de erro, se houver
    # Exemplo UC 4 - Inserir horários sem separador ":"
    horario = input("Insira o horário sem separador (HHmm ou Hmm): ")
    horario_formatado = interpretar_horario_sem_separador(horario)
    print(f"Horário formatado: {horario_formatado}")
 
# Execução do programa principal
if __name__ == "__main__":
    main()