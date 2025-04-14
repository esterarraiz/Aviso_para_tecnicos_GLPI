import json
from datetime import datetime, timedelta

class ChamadosNotificados:
    def __init__(self, caminho_arquivo="notificados.json", dias_validade=2):
        self.caminho_arquivo = caminho_arquivo
        self.dias_validade = dias_validade
        self.notificados = self._carregar()
        self._remover_antigos()

    def _carregar(self):
        try:
            with open(self.caminho_arquivo, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _salvar(self):
        with open(self.caminho_arquivo, "w") as f:
            json.dump(self.notificados, f, indent=4)

    def _remover_antigos(self):
        agora = datetime.now()
        novos_notificados = {
            numero: data for numero, data in self.notificados.items()
            if datetime.strptime(data, "%Y-%m-%d %H:%M:%S") > (agora - timedelta(days=self.dias_validade))
        }
        self.notificados = novos_notificados
        self._salvar()

    def ja_notificado(self, numero_chamado):
        return str(numero_chamado) in self.notificados

    def adicionar(self, numero_chamado):
        self.notificados[str(numero_chamado)] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._salvar()
