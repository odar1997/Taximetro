import time

class taximetro:
    def __init__(self, name):
        self.nombre_taxista = name
        self.total_tarifa = 0
        self.ultimo_tiempo = None
        self.en_movimiento = False
        self.tiempo_parado = 0
        self.tiempo_en_movimiento = 0
        self.en_servicio = False
        self.__tarifa_movimiento = 0.05
        self.__tarifa_parado = 0.02

    def iniciar_trayecto(self):
        if(self.en_servicio):
            print("Debe Finalizar el trayecto antes de iniciar uno nuevo")
            return
        self.en_servicio = True
        self.tiempo_parado = 0
        self.total_tarifa = 0
        self.tiempo_en_movimiento  = 0
        print("Iniciando Trayecto")
        self.ultimo_tiempo = time.time()
        print(f"El trayecto inicio: {time.strftime("%Y/%m/%d - %H:%M:%S")}")

    def finalizar_trayecto(self):
        if(self.en_servicio == False):
            print("Debe iniciar un trayecto primero.")
            return
        # Hay que actualizar la tarifa antes de finalizar 
        total_euros = self.total_tarifa  # Convertimos céntimos a euros
        print(f"El trayecto inicio: {time.strftime("%Y/%m/%d - %H:%M:%S")}")
        print(f"Trayecto finalizado. Total a pagar: €{total_euros:.2f}")
        print(f"La duración de su viaje fue: {(self.en_movimiento + self.tiempo_parado):.2f} segundos")
        self.ultimo_tiempo = None
        self.en_servicio = False

    def actualizar_tarifa(self, estado):
        if(self.en_servicio == False):
            print("Debe iniciar un trayecto primero.")
            return
        self.en_movimiento = estado
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.ultimo_tiempo
        print(f" prueba de tiempo:{tiempo_transcurrido / 60:.2f}")
        self.ultimo_tiempo = tiempo_actual

        if(self.en_movimiento):
            self.tiempo_en_movimiento += tiempo_transcurrido
            self.total_tarifa += tiempo_transcurrido * self.__tarifa_movimiento  # 5 céntimos por segundo
        else:
            self.tiempo_parado += tiempo_transcurrido
            self.total_tarifa += tiempo_transcurrido * self.__tarifa_parado
        
    def mostrar_instrucciones(self):
        print("Bienvenido al simulador de tarifas de taxi.")
        print("Instrucciones:")
        print("1. Para iniciar un trayecto, escriba 'iniciar'.")
        print("2. Para registrar que el taxi está en movimiento, escriba 'moverse'.")
        print("3. Para registrar que el taxi está parado, escriba 'parar'.")
        print("4. Para finalizar el trayecto, escriba 'finalizar'.")
        print("5. Para comenzar un nuevo trayecto, simplemente repita 'iniciar'.")
            
def menu():
    taxi = taximetro("Orlando")
    taxi.mostrar_instrucciones()

    while True:
        comando = input("\n¿Qué desea hacer? (iniciar/moverse/parar/finalizar/salir): ").strip().lower()

        if comando == 'iniciar' or comando[0] == "i":
            taxi.iniciar_trayecto()
        elif comando == 'moverse' or comando[0] == "m":
            taxi.actualizar_tarifa(True)
        elif comando == 'parar' or comando[0] == "p":
            taxi.actualizar_tarifa(False)
        elif comando == 'finalizar' or comando[0] == "f":
            taxi.finalizar_trayecto()
        elif comando == 'salir' or comando[0] == "s":
            if taxi.en_servicio == False:
                print("Gracias por usar el simulador de taxi. ¡Hasta luego!")
                break
            else:
                print("Debe finalizar el servicio primero antes de salir")
        else:
            print("Comando no reconocido. Intente de nuevo.")


if __name__ == "__main__":
    menu()