from datetime import datetime, timedelta

class relatorio:
    def __init__(self, lista_chamados):
        self.lista_chamados = lista_chamados
        self.hora_atual = datetime.now()

    def gerar_relatorio(self):
        limite_superior = self.hora_atual + timedelta(minutes=30)
        chamados_urgentes = []
        chamados_por_tecnico = {
            "Ester Matos": []
            #lista de tecnicos
            # "Tecnico 1": [],
            # "Tecnico 2": []
        }

        for chamado in self.lista_chamados:
            try:
                tempo_solucao = datetime.strptime(chamado['tempo_solucao'], "%d-%m-%Y %H:%M")
                if self.hora_atual <= tempo_solucao <= limite_superior:
                    chamados_urgentes.append(chamado)

                    tecnico = chamado['tecnico']
                    if tecnico in chamados_por_tecnico:
                        chamados_por_tecnico[tecnico].append(chamado)

            except ValueError:
                print(f"Erro ao converter tempo de solução do chamado {chamado['numero']}")

        return chamados_por_tecnico
