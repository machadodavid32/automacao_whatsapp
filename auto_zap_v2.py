import webbrowser, pyautogui
from time import sleep


"""Automação para envio de mensagens WhatsApp
Vamos aos passos

CUIDADOS
1 - Lista de contatos
2 - Enviar individualmente uma mensagem para cada pessoa
3 - Pausas entre os envios

PASSOS
1 - Escolher um contato
2 - Enviar mensagem para este contato
3 - Repetir isso para outros contatos

api whatsApp - https://api.whatsapp.com/send?phone=aquinumerodotelefonecompleto

"""

telefones = [ ]  # números de telefones com codigo do país e cidade. Nesta v2, vamos importar do arquivo fones.txt

with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n') [0])
    print(telefones)    

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1073,246, duration=1)
    sleep(5)
    pyautogui.click(856,982, duration=1)
    sleep(3)
    pyautogui.typewrite("Isso é só um teste")
    sleep(5)
    pyautogui.press('enter')
