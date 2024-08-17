from linked_lists.lista_prontuarios import PatientRecords

records = [
    {
        "paciente": "João da Silva",
        "diagnostico": "Hipertensão arterial",
        "tratamento": "Atenolol 50 mg/dia"
    },
    {
        "paciente": "Maria Santos",
        "diagnostico": "Diabetes tipo 2",
        "tratamento": "Metformina 850 mg 2x/dia"
    },
    {
        "paciente": "Carlos Oliveira",
        "diagnostico": "Asma",
        "tratamento": "Salbutamol inalatório conforme necessidade"
    },
    {
        "paciente": "Ana Pereira",
        "diagnostico": "Depressão",
        "tratamento": "Sertralina 50 mg/dia"
    },
    {
        "paciente": "Luiz Costa",
        "diagnostico": "Gastrite",
        "tratamento": "Omeprazol 20 mg/dia"
    },
    {
        "paciente": "Fernanda Almeida",
        "diagnostico": "Infecção do trato urinário",
        "tratamento": "Ciprofloxacino 500 mg 2x/dia por 7 dias"
    },
    {
        "paciente": "Rafael Oliveira",
        "diagnostico": "Rinite alérgica",
        "tratamento": "Loratadina 10 mg/dia"
    },
    {
        "paciente": "Camila Rodrigues",
        "diagnostico": "Hipotireoidismo",
        "tratamento": "Levotiroxina 50 mcg/dia"
    },
    {
        "paciente": "Pedro Lima",
        "diagnostico": "Enxaqueca",
        "tratamento": "Sumatriptano 50 mg conforme necessidade"
    },
    {
        "paciente": "Isabela Ferreira",
        "diagnostico": "Artrite reumatoide",
        "tratamento": "Metotrexato 15 mg/semana"
    }
]

list = PatientRecords()

for i in range (len(records)):
    list.append(records[i])

print(f"> Quantidade de pacientes: {list.size}")
print(f"> Lista de pacientes:\n{list}")

print("Buscar prontuários que contenham a informação especificada:")
search_result = list.search("Luiz Costa")
print(search_result)

print("Mudar o nome do paciente para 'Pedro Amaral' no prontuário de 'Luiz Costa':")
list.get("Luiz Costa").update(key="paciente", new_value="Pedro Amaral")
search_result2 = list.search("Luiz Costa")
print(search_result2)