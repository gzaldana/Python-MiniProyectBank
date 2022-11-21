#Gerardo Antonio Zaldana Ruiz
from art import logo

granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("credencials.txt", "r") 
    #abre un archivo de texto donde se almacenan las credenciales
    for i in file:
         a,b=i.split(",")
         #separa por comas lo guardado en el archivo txt para verificarlo
         b = b.strip() 
         #remueve espacios al inicio y al final
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("\nLogueo Establecido\n")
        grant()
    else:
        print("Usuario o contraseña Incorrecta")
        begin()
        
def register(name,password):
    file = open("credencials.txt", "a")
    file.write("\n"+name+","+password)
    grant()

def access(option):
    global name
    if(option=="login"):
        name = input("Ingrese su usuario: ")
        password = input("Ingrese una contraseña: ")
        login(name,password)
    else:
        print("Ingrese su usuario y contraseña")
        name = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        register(name,password)

def begin():
    print(logo)
    global option
    print("######################################################")
    print("## Banco Costarricense de Desarrollo S.A “BACODESA” ##")
    print("######################################################\n")
    print('Favor Elija una de las siguientes user_electiones')
    print('login = Ingresar \nreg = Registrar')
    option = input("Ingresar o Registrar: ").lower()
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    
    print("######################################################")
    print('##    Estimado cliente, Bienvenido al sistema del   ## ')
    print("## Banco Costarricense de Desarrollo S.A “BACODESA” ##")
    print("######################################################\n")

    print('En el siguente menú se encuentra alguna de las siguientes user_electiones\nFavor secionar una: ')
    print('1) CONTACTO')
    print('2) INFORMACION')
    print('3) CALCULAR PRESTAMO')
    print('4) SALIR')
    user_election = input('Favor digite el número según lo deseado: ')
    
    if user_election=='1':
        print('Ejecutivo: Gerardo Antonio Zaldaña Ruiz \nCorreo: g.zaldana@bacodesa.com \nTelefono: 84886378')
        print('Dirección: Sabanilla de Montes de OCA, San José, Costa Rica')
    elif user_election=='2':
        print(''' 
        

            Nota
            *Importante: BACODESA agradece su preferencia y le informa que este servicio es únicamente
            como referencia para ayudarle en su decisión, sin embargo, debe considerar que las condiciones pueden
            variar ya que el precio final esta determinado por otras condiciones como garantía, tasa de interés,
            comisiones, seguros y características propias de cada cliente. BACODESA aclara que las 
            condiciones de tasa que regirán el contrato serán las que estén vigentes el día de firma de crédito, posterior a la
            verificación del cumplimiento de algunas condiciones.

        ''')
    elif user_election=='3':
        print('1- vivienda')
        print('2- vehiculo')
        print('3- personal')
        prestamo_opcion=int(input('Elija una de la opciones anteriores: '))
        if prestamo_opcion==1:
            prestamo=float(input('Ingrese el monto de su prestamo: '))
            interes=prestamo*0.08
            total=prestamo+interes
            print(f'El total del prestamo con los intereses sería de: ₡{total}')
            print('El plazo Maximo de años es de 30')
            aniospermit=False
            cuotasmen=0
            while aniospermit:
                 anios=int(input('A cuantos años desea adquirir su prestamo: '))
                 if 0>anios<31:
                    cuotasmen = anios/12
                 else:
                    aniospermit=True
            cuotamensual = total/cuotasmen
        else:
            print('error')
    elif user_election=='4':
        print('Gracias por su visita')
        #grant()
    else:
        print('La opción seleccionada no esta disponible: ')
        #access(option)
        grant()