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