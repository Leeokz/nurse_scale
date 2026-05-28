escala = {
    "João": [],
    "Maria": [],
    "Carlos": [],
    "Ana": [],
    "Leonardo": [],
    "Julia": [],
    "Bruno": [],
    "Carla": [],
    "Enzo": [],
    "Jessica": [],
    "Gustavo": [],
    "Fernanda": [],
    "Lucas": [],
    "Mariana": [],
    "Ricardo": [],
    "Sofia": []
}

def add_turno(funcionario, turno):
    if funcionario in escala:
        escala[funcionario].append(turno)
        print (f"Turno {turno} adicionado para {funcionario}.")
    else:
        print(f"Funcionário {funcionario} não encontrado na escala.")

add_turno("João", "MT")
add_turno("Maria", "SN")
add_turno("Carlos", "F")
print(escala)

def exibir_escala():
    print("Escala de Trabalho:")
    for funcionario, turnos in escala.items():
        turnos_str = ", ".join(turnos) if turnos else "Sem turnos"
        print(f"{funcionario}: {turnos_str}")
exibir_escala()

def gerar_escala_vazia(dias):
    escala_vazia = ["F"] * dias
    return escala_vazia

print(gerar_escala_vazia(30)),

def aplicar_regra_sn(turnos):
    for indice, turno in enumerate(turnos):
        if turno == "SN":
            if indice + 1 < len(turnos):
                turnos[indice + 1] = "S"
    return turnos

turnos_exemplo = ["MT", "SN", "F", "MT", "SN", "F"]
turnos_aplicados = aplicar_regra_sn(turnos_exemplo)
print(turnos_aplicados)

def validar_mt_consecutivo(turnos):
   contador_mt = 0
   for turno in turnos:
       if turno == "MT":
           contador_mt += 1
           if contador_mt == 4:
               return False
       else:
           contador_mt = 0
   return True
print(validar_mt_consecutivo(["MT", "MT", "MT", "MT", "F"]))
print(validar_mt_consecutivo(["MT", "MT", "F", "MT", "MT"]))

def validar_folga_6dias(turnos):
    contador_folga = 0
    for turno in turnos:
        if turno in ["MT", "SN", "S"]:
            contador_folga += 1
            if contador_folga > 6:
                return False
        else:
            contador_folga = 0
    return True
print(validar_folga_6dias(["MT", "MT", "MT", "MT", "MT", "MT", "MT"]))
print(validar_folga_6dias(["MT", "MT", "F", "MT", "MT", "MT", "MT"]))

def validar_total_turnos(turnos):
    total_turnos = sum(1 for turno in turnos if turno in ["MT", "SN"])
    return total_turnos == 12
print(validar_total_turnos(["MT"] * 12))  
print(validar_total_turnos(["MT"] * 10 + ["SN"] * 3))


import calendar
def validar_fds_folga(turnos, ano, mes):
    # Verificar o dia da semana do primeiro dia do mês
    for indice, turno in enumerate(turnos):
        dia = indice + 1
        if turno in ["F"]:
            if calendar.weekday(ano, mes, dia) == 5:  # Verificar se é sábado ou domingo
                    
                if turnos[indice + 1] == "F":  # Verificar se o próximo dia também é folga
                    return True
    return False 

turnos_com_fds = ["F"] * 30
print(validar_fds_folga(turnos_com_fds, 2025, 5))
turnos_sem_fds = ["MT"] * 30
print(validar_fds_folga(turnos_sem_fds, 2025, 5))


def check_rules(turnos, ano, mes):
    mt_ok = validar_mt_consecutivo(turnos)
    print(f"Regra MT consecutivo: {'OK' if mt_ok else 'Violada'}")
    folga_ok = validar_folga_6dias(turnos)
    print(f"Folga a cada 6 dias: {'OK' if folga_ok else 'Violada'}")
    total_ok = validar_total_turnos(turnos)
    print(f"Total de turnos MT e SN: {'OK' if total_ok else 'Violada'}")
    fds_ok = validar_fds_folga(turnos, ano, mes)
    print(f"Folga no fim de semana: {'OK' if fds_ok else 'Violada'}")
  
    return mt_ok and folga_ok and total_ok and fds_ok 

turnos_teste = ["MT"] * 12 + ["F"] * 18
print(check_rules(turnos_teste, 2026, 5))