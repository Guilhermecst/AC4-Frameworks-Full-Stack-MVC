import json


class Aluno:

    #construtor
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def get_aluno_data(self):
        data = [
            {
                'nome': self.nome,
                'cpf': self.cpf,
                'telefone': self.telefone,
                'email': self.email
            }
        ]
        data_json = json.dumps(data)
        return data_json