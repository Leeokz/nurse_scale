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