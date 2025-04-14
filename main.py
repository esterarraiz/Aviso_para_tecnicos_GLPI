from glpi import GLPIBot
from alerta import relatorio
from formatacao_email import EmailFormatar
from envio_email import EnvioEmail
from salvar_chamados import ChamadosNotificados
from datetime import datetime

print("\n----- SEJA BEM-VINDO! -----\n")

usuario = "seu.usuario"
senha= "sua_senha"

glpi = GLPIBot(usuario, senha)
glpi.login()

chamados = glpi.extrair_chamados()
chamados_urgentes_por_tecnico = relatorio(chamados).gerar_relatorio()
notificador = ChamadosNotificados()

print("\n--- Lista de todos os chamados extraídos ---\n")
for chamado in chamados:
    print(f"Número: {chamado['numero']}, Técnico: {chamado['tecnico']}, Tempo para solução: {chamado['tempo_solucao']}")

print("\n--- Chamados urgentes por técnico (próximos 30 minutos) ---\n")
for tecnico, lista in chamados_urgentes_por_tecnico.items():
    if lista: 
        print(f"\nTécnico: {tecnico}")
        for chamado in lista:
            print(f"  - Número: {chamado['numero']}, Tempo para solução: {chamado['tempo_solucao']}")

remetente = usuario + "seu_dominio"
print(f"\nRemetente: {remetente}")
senha_email="senha_email"

for tecnico, lista in chamados_urgentes_por_tecnico.items():
    lista_filtrada = []
    lista_ja_enviados = []

    for chamado in lista:
        if not notificador.ja_notificado(chamado["numero"]):
            lista_filtrada.append(chamado)
        else:
            lista_ja_enviados.append(chamado)

    if lista_ja_enviados:
        print(f"\nChamados já notificados para {tecnico} (não serão reenviados):")
        for chamado in lista_ja_enviados:
            print(f"  - Número: {chamado['numero']}, Tempo para solução: {chamado['tempo_solucao']}")


    if lista_filtrada:  
        email_tecnico = tecnico.lower().replace(" ", ".") + "dominio"
        corpo_itens = ""

        for chamado in lista_filtrada:
            corpo_itens += f'<li><strong>Chamado nº {chamado["numero"]}</strong> — Prazo de solução: {chamado["tempo_solucao"]}</li>\n'

        email = EmailFormatar(remetente, email_tecnico, "Ester Arraiz Matos")
        corpo_email = email.formatar_email(nome_tecnico=tecnico, chamados=lista_filtrada)

        email_sender = EnvioEmail(remetente, senha_email)
        email_sender.enviar_email(destinatario=email_tecnico, assunto="[IDX] Chamado(s) críticos em sua fila — verificação recomendada", mensagem=corpo_email)

        print(f"E-mail enviado para: {email_tecnico}")

        for chamado in lista_filtrada:
            notificador.adicionar(chamado["numero"])
