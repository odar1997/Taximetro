
# 🚕 Proyecto Python: Taxímetro Digital

![Banner Proyectos](https://github.com/user-attachments/assets/bc6e34f7-4031-43dd-8cfc-805c935ba3c4)

## 📝 Descripción del Proyecto

Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.

## 📊 Niveles de Implementación

### 🟢 Nivel Esencial

Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.

- Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - Iniciar un trayecto.
  - Calcular tarifa mientras el taxi está parado (2 céntimos por segundo).
  - Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo).
  - Finalizar un trayecto y mostrar el total en euros.
  - Permitir iniciar un nuevo trayecto sin cerrar el programa.



## 🛠️ Tecnologías a Utilizar

- Python
- Git y GitHub para control de versiones
- Trello o Jira para la gestión del proyecto
- Bibliotecas adicionales según el nivel de implementación (por ejemplo, logging, unittest, tkinter para GUI, SQLite para base de datos)
- Docker para containerización (nivel experto)
- Framework web como Flask o Django para la versión web (nivel experto)

## 📦 Entregables

- Repositorio de GitHub con el código fuente del proyecto.
- Demostración del CLI desarrollado.
- Presentación para público no técnico.
- Presentación técnica del código, destacando fortalezas y debilidades.
- Enlace al tablero Kanban utilizado para la organización del proyecto.

## ⏳ Plazo de Entrega

Dos semanas a partir de la fecha de inicio del proyecto.

## 💡 Consejos para el Desarrollo

- Comienza con el nivel esencial y ve agregando funcionalidades gradualmente.
- Utiliza control de versiones desde el inicio del proyecto.
- Realiza pruebas frecuentes para asegurar el correcto funcionamiento en cada etapa.
- Documenta tu código y mantén un registro de los cambios y decisiones de diseño.
- Considera la usabilidad y la experiencia del usuario, incluso en la versión CLI.

- # Simulador de Tarifas de Taxi

Este proyecto es un simulador de tarifas de taxi desarrollado en Python, diseñado para ejecutarse en Visual Studio Code (VSCode) utilizando un entorno virtual creado con `venv`. El programa permite simular el comportamiento de un taxímetro, calculando tarifas basadas en el tiempo en movimiento y en parada.

## Características

- **Inicio y finalización de trayectos**: Controla el inicio y fin de un trayecto.
- **Cálculo de tarifas**:
  - Tarifa en movimiento: 0.05 €/segundo.
  - Tarifa en parada: 0.02 €/segundo.
- **Gestión de estados**:
  - En movimiento.
  - En parada.
- **Interfaz de consola interactiva**: Permite al usuario controlar el simulador mediante comandos sencillos.

## Requisitos previos

- **Python**: Asegúrate de tener instalado Python 3.8 o superior.
- **Entorno virtual**: Este proyecto utiliza `venv` para manejar las dependencias.

## Instalación

1. **Clona el repositorio o descarga el código fuente**:
   ```bash
   git clone https://github.com/odar1997/Taximetro.git
   cd Taximetro
   🚀 Desarrollado por Orlando Alcala

   Uso
Cuando ejecutes el programa, se mostrará un menú interactivo con las siguientes opciones:

Iniciar trayecto:

Escribe iniciar o i para comenzar un nuevo trayecto.
Esto reinicia los contadores de tiempo y la tarifa acumulada.
Registrar movimiento del taxi:

Escribe moverse o m para indicar que el taxi está en movimiento.
Registrar que el taxi está parado:

Escribe parar o p para indicar que el taxi se ha detenido.
Finalizar trayecto:

Escribe finalizar o f para terminar el trayecto y mostrar el total acumulado a pagar.
Salir del programa:

Escribe salir o s para cerrar la aplicación. Nota: Si un trayecto está en curso, primero debes finalizarlo.
Ejemplo de Uso
plaintext
Copiar
Editar
Bienvenido al simulador de tarifas de taxi.
Instrucciones:
1. Para iniciar un trayecto, escriba 'iniciar'.
2. Para registrar que el taxi está en movimiento, escriba 'moverse'.
3. Para registrar que el taxi está parado, escriba 'parar'.
4. Para finalizar el trayecto, escriba 'finalizar'.
5. Para comenzar un nuevo trayecto, simplemente repita 'iniciar'.

¿Qué desea hacer? (iniciar/moverse/parar/finalizar/salir): iniciar
Iniciando Trayecto
El trayecto inició: 2025/02/17 - 14:30:45

¿Qué desea hacer? (iniciar/moverse/parar/finalizar/salir): moverse
Tiempo transcurrido: 0.02 minutos.

¿Qué desea hacer? (iniciar/moverse/parar/finalizar/salir): parar
Tiempo transcurrido: 0.01 minutos.

¿Qué desea hacer? (iniciar/moverse/parar/finalizar/salir): finalizar
Trayecto finalizado. Total a pagar: €0.12
Estructura del Código
Clase taximetro:
Maneja los cálculos de tarifa, estado del taxi y tiempos de trayecto.
Métodos principales:
iniciar_trayecto: Inicia un nuevo trayecto.
finalizar_trayecto: Finaliza un trayecto en curso y muestra el total acumulado.
actualizar_tarifa: Actualiza la tarifa en función del estado (en movimiento/parado).
mostrar_instrucciones: Muestra las instrucciones de uso al usuario.
Función menu:
Proporciona un menú interactivo para que el usuario controle el programa.
   

