turnos = {
    "MT": "Manhã e Tarde",
    "SN": "Serviço Noturno",
    "F": "Folga",
    "S": "Saída"
}

def listar_turnos():
    print("Turnos disponíveis:")
    for sigla, descricao in turnos.items():
        print(f"{sigla}: {descricao}")
        
listar_turnos() 