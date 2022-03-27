import sys
import os
import time

#? Desarrollo de aplicación sin entorno grafico para el soporte desde linux o windows
#? Consulta del sistema operativo en el que esta corriendo(Linux, Windows o Darwin)
my_sys = sys.platform

#? Menu de soporte
menu = [
    'Conexion VPN',
    'noMachine',
    'Interfaz Web',
    'AnyDesk',
    'Salir'
]

conn_menu = [
    'Conexión Externa',
    'Conexión Local',
    'Atrás'
]

def limpiar():
    os.system('clear')

def title():
    print ('***************************************************************************')
    print ('***************************************************************************')
    print (' ____                         _          ____      _     _  ___          _ ')
    print ('/ ___|  ___  _ __   ___  _ __| |_ ___   / ___|   _| |__ (_)/ _ \  __   _/ |')
    print ("\___ \ / _ \| '_ \ / _ \| '__| __/ _ \ | |  | | | | '_ \| | | | | \ \ / / |")
    print (" ___) | (_) | |_) | (_) | |  | ||  __/ | |__| |_| | |_) | | |_| |  \ V /| |")
    print ('|____/ \___/| .__/ \___/|_|   \__\___|  \____\__,_|_.__/|_|\__\_\   \_(_)_|')
    print ("            |_|                                                   ")
    print ('***************************************************************************')
    print ('***************************************************************************')
    print ('')

def impMenu():
    limpiar()
    title()
    # os.system('figlet Soporte CubiQ') # barra para titulos desde consola
    i = 1
    for x in menu:
        print (f'   {i}. {x}')
        i = i+1

# NOMACHINE ********* Funcion que permite abrir la aplicacion
def noMach():
    os.system ('sh /usr/NX/bin/nxplayer &')

# INTERFAZ_WEB ************* Abre interfaz de cubiq via web
def webLink():
    limpiar()
    title()
    vpn = input('   Ingrese vpn: ')
    os.system(f'google-chrome-stable --new-window 10.8.0.{vpn}')
    time.sleep(2)

# CONEXION_VPN ********* Funcion que permite la conexión a cubiq por vpn
def connExt(vpn):
    limpiar()
    print (f'Conectado a 10.8.0.{vpn}')
    os.system(f'konsole -e sshpass -p CubiQ2019 ssh -o "StrictHostKeyChecking=no" cubiq@10.8.0.{vpn} &')
    time.sleep(2)

def connLoc(vpn):
    limpiar()
    print(f'Conectado a {vpn}')
    os.system(f'konsole -e sshpass -p CubiQ2019 ssh -o "StrictHostKeyChecking=no" cubiq@{vpn} &')
    time.sleep(2)

#MENU_VPNS ********* Impresión de menu para Conexion VPN
def conn():
    limpiar()
    title()
    i = 1
    for x in conn_menu:
        print (f'   {i}. {x}')
        i = i+1
    try:
        connType = int(input('\n    Ingrese una opción: '))
        resConn = conn_menu[connType-1]
    except:
        pass

    if resConn == 'Conexión Externa':
        limpiar()
        title()
        vpn = int(input('   Ingrese vpn para conexión Externa: '))
        connExt(vpn)
    elif resConn == 'Conexión Local':
        limpiar()
        title()
        vpn = input('   Ingrese ip para la conexión local: ')
        connLoc(vpn)
    elif resConn == 'Atras':
        pass

# ANYDESK ********** Funcion que permite conectarse a equipos por anyDesk
def connAny():
    nom = input('   Nombre de la conexion: ')
    os.system(f'anydesk {nom} > /dev/null 2>&1 &')

#? MENU_PPAL ********** Esta función permite seleccionar una opcion del menú
def opcSelec(selec):
    if selec == 'Conexion VPN':
        conn()
    elif selec == 'noMachine':
        noMach()
    elif selec == 'Interfaz Web':
        webLink()
    elif selec == 'AnyDesk':
        connAny()
    elif selec == 'Salir':
        return 3

def error():
    e = sys.exc_info()
    print('    eRrOr: Opción no valida')
    time.sleep(1)

#! INICIO
i=0
while i!=3:
    impMenu()
    try:
        selec = int(input('\n   Ingrese una opción: '))
        res = opcSelec(menu[selec-1])
        i = res
    except:
        error()
limpiar()