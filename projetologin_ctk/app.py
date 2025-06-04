
import customtkinter as ctk


# aparencia da janela
ctk.set_appearance_mode('dark')

# criação das função


def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # verificar se o usuario e senha esta certo
    if usuario == 'paulo' and senha == '123':
        resultado_login.configure(
            text='Login feito com sucesso!', text_colo='green')

    else:
        resultado_login.configure(text='Login incorreto', text_colo='red')


# janela pricipal
app = ctk.CTk()
app.title('Sistema de Long')
app.geometry('300x300')


# label
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=10)

# entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuario')
campo_usuario.pack(pady=10)
# label
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)

# entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite seu Senha')
campo_senha.pack(pady=10)

# button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# campos feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


# aplicação
app.mainloop()
