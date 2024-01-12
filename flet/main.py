
"""

frontend  -> usuario ve
backend -> logica por tras do site

framework - conj de ferramentas que servem para algo

django
flask
flet (uso hj) pip install flet no cmd
    - siste
    - programas de comp
    - app de celular

titulo hashzap
botao de iniciar o chat
    - pop up
     - bem vindo ao hashzap
     - escreva seu nome
     - button entrar no chat
chat
    - lira entrou no site
    - campo de enviar mensagem
campo para enviar mensagem
botao de enviar

"""
import flet as ft

def main(pagina):
    titulo = ft.Text("BrenoxZAP")
    
    nome_usuario = ft.TextField(label="Escreva seu nome")
    chat = ft.Column()
    
    campo_mensagem = ft.TextField(label = "escreva sua mensagem")

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):

        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        
        pagina.pubsub.send_all(texto_campo_mensagem)

        campo_mensagem.value = ""
        
        

        pagina.update()

    botao_enviar = ft.ElevatedButton("enviar", on_click = enviar_mensagem)

    def entrar_chat(evento):
        popup.open = False 
        pagina.remove(botao_iniciar)

        pagina.add(chat)
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)

        texto =  f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()

    popup = ft.AlertDialog( #criacao de popup
        open = False,
        modal = True,
        title = ft.Text("Bem vindo ao Brenoxzap"),
        content = nome_usuario,
        actions = [ft.ElevatedButton("Entrar", on_click = entrar_chat), ]
            )

    def iniciar_chat(evento): 
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click = iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)





ft.app(main, view=ft.WEB_BROWSER) #criar um aplicativo com esse codigo