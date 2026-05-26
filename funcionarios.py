funcionarios = [
    {
        "id": 1,
        "nome": "João",
        "cargo": "Enfermeiro"
    },
    {
        "id": 2,
        "nome": "Maria",
        "cargo": "Enfermeira"
    },
    {
        "id": 3,
        "nome": "Carlos",
        "cargo": "Enfermeiro"
    },
    {
        "id": 4,
        "nome": "Ana",
        "cargo": "Enfermeira"
    },
    {
        "id": 5,
        "nome": "Leonardo",
        "cargo": "Enfermeiro"
    },
    {
        "id": 6,
        "nome": "Julia",
        "cargo": "Enfermeira"
    },
    {
        "id": 7,
        "nome": "Bruno",
        "cargo": "Enfermeiro"
    },
    {
        "id": 8,
        "nome": "Carla",
        "cargo": "Enfermeira"
    },
    {
        "id": 9,
        "nome": "Enzo",
        "cargo": "Enfermeiro"
    },
    {
        "id": 10,
        "nome": "Jessica",
        "cargo": "Enfermeira"
    },
    {
        "id": 11,
        "nome": "Gustavo",
        "cargo": "Enfermeiro"
    },
    {
        "id": 12,
        "nome": "Fernanda",
        "cargo": "Enfermeira"
    },
    {
        "id": 13,
        "nome": "Lucas",
        "cargo": "Enfermeiro"
    },
    {
        "id": 14,
        "nome": "Mariana",
        "cargo": "Enfermeira"
    },
    {
        "id": 15,
        "nome": "Ricardo",
        "cargo": "Enfermeiro"
    },
    {
        "id": 16,
        "nome": "Sofia",
        "cargo": "Enfermeira"
    },]

def func_list():
    print("Lista de Funcionários:")
    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}")

func_list()

def add_funcionario(nome, cargo):
    new_id = len(funcionarios) + 1
    new_funcionario = {
        "id": new_id,
        "nome": nome,
        "cargo": cargo
    }
    funcionarios.append(new_funcionario)
    print(f"Funcionário {nome} adicionado com sucesso!")

add_funcionario("Pedro", "Técnico de Enfermagem")
func_list()

def remover_funcionario(id):
        for funcionario in funcionarios:
            if funcionario['id'] == id:  # ID do funcionário a ser removido
                funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso!")
                break
        else:
            print("Funcionário não encontrado!")

remover_funcionario(3)  # ID do funcionário a ser removido

func1 = "Enfermeiro"
func2 = "Técnico de Enfermagem"

def buscar_funcionario(nome):
    lista_funcionarios = [funcionario for funcionario in funcionarios if funcionario['nome'] == nome]
    if lista_funcionarios:
        for funcionario in lista_funcionarios:
            print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}")
    else:
        print("Funcionário não encontrado.")

        #Buscar um funcionário pelo nome#
buscar_funcionario("Maria")