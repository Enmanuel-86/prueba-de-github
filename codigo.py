usuarios = ["juan", "pedro", "lopez"]

def revisar(usuario, contra):
    
    
    if usuario in usuarios and contra == "123":
        print(f"bienvenido {usuario}")
        
    else:
        
        print(f"el usuario {usuario} no esta registrado")
        
    

print("--------------------------------")
print("-------------Login-------------")
print("--------------------------------")


usuario = input("Usuario: ")
contra = input("Contraseña: ")


revisar(usuario, contra)

