class EmailFormatar:
    def __init__(self, remetente, destinatario, nome_remetente):
        self.remetente = remetente
        self.destinatario = destinatario
        self.nome_remetente = nome_remetente.title()

    def formatar_email(self, nome_tecnico, chamados):
        lista_html = ""
        for chamado in chamados:
            numero = chamado['numero']
            prazo = chamado['tempo_solucao']
            lista_html += f"<li><strong>Chamado nº {numero}</strong> — Prazo de solução: {prazo}</li>\n"

        mensagem = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
                <div style="text-align: center; background-color: #000; padding: 20px;">
                    <img src="https://ugc.production.linktr.ee/ef83339a-c17f-44fd-a29e-9bad99c63a07_IDX---Logo-1-vertical-cor-invertida.png?io=true&size=avatar-v3_0" alt="Logo IDX Datacenters" width="100" />
                </div>
                <div style="text-align: center;">
                    <div style="color:black; padding: 15px; border-radius: 8px 8px 0 0;">
                        <h2 style="margin: 0;">⏰ Alerta: Chamado(s) prestes a vencer!</h2>
                    </div>

                    <p>Olá <strong>{nome_tecnico}</strong>,</p>

                    <p>Os seguintes chamados atribuídos a você estão com o prazo de resolução previsto para os próximos <strong style="color: #e53935;">30 minutos</strong>:</p>

                    <ul style="list-style-type: disc; text-align: left; display: inline-block; margin: 0 auto;">
                        {lista_html}
                    </ul>

                    <p style="color: #555;">Recomendamos atenção especial para evitar ultrapassar o SLA estabelecido.</p>

                    <p>Atenciosamente,<br><strong>Time de Atendimento IDX.</strong></p>

                    <p style="font-size: 12px; color: #999; margin-top: 30px;">
                        ⚠️ Em caso de erro ou inconsistência nos chamados listados, entre em contato com o <strong>Time de Atendimento IDX</strong>.
                    </p>
                </div>
            </body>
        </html>
        """

        return mensagem
