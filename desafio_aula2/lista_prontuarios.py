# Tecnólogo em Ciência de Dados
# Estruturas de Dados (Aula 2 - Unidade 1)

# Você é um desenvolvedor de software em uma clínica médica que está migrando 
# os registros de saúde dos pacientes de um sistema baseado em papel para um 
# sistema eletrônico. Para atender a essa necessidade, você 
# decide utilizar listas encadeadas em Python para manter os registros médicos.
# Os prontuários devem ser rapidamente acessíveis e facilmente atualizáveis
# cada vez que um paciente visita a clínica.

# REQUISITOS: 
# 1. Usar listas encadeadas para armazenar prontuários eletrônicos dos pacientes.
# 2. Permitir a inserção de novos registros de maneira eficiente no histórico do paciente.
# 3. Facilitar a buscar e atualização de prontuários existentes.

import copy

class Record:
    """Representa o prontuário médico de um paciente."""
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"
        
    def update(self, key, new_value):
        self.data[key] = new_value

class PatientRecords:
    def __init__(self, head=None) -> None:
        self.head = head
        self.size = 0

    def __str__(self) -> str:
        # string = ""
        pointer = self.head
        string = f"{pointer}\n"
        while pointer.next:
            string = f"{string}{pointer}\n"
            pointer = pointer.next
        return string

    def append(self, new_data) -> None:
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Record(new_data)
        else:
            self.head = Record(new_data)

        self.size += 1

    def search(self, value):
        """Retorna uma lista com todos os prontuário que contêm a informação desejada."""
        results = PatientRecords()
        pointer = self.head
        while pointer.next:
            if value in pointer.data.values():
                obj_copy = copy.deepcopy(pointer)
                obj_copy.next = None
                results.append(obj_copy)
            pointer = pointer.next
        if results.size == 0:
            return "Not Found"
        else: 
            return results
        
    def get(self, value) -> Record:
        """Retorna o primeiro prontuário com a informação desejada."""
        pointer = self.head
        while pointer.next:
            if value in pointer.data.values():
                return pointer
            pointer = pointer.next