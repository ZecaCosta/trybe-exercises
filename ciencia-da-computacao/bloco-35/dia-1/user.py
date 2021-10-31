class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


meu_user = User("Ari", "ari@dominio.com", "Senha")
print(meu_user)  # <__main__.User object at 0x7f477e6c2070>
print(meu_user.name)  # Ari
print(meu_user.email)  # ari@dominio.com
print(meu_user.password)  # Senha
print(type(meu_user)) ## <class '__main__.User'>
