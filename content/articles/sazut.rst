My first bot !
##############

:tags: python, bot, telegram, telepot, docker, poetry, cookiecutter
:date: 2019-06-07
:modified: 2019-06-07
:author: Sarudego
:slug: my-first-bot



Sazut bot
=========

Como usuario del servicio de autobuses de Zaragoza,
he usado varias aplicaciones para obtener los tiempos de los autobuses,
pero harto de los fallos o mal funcionamiento, junto a mis ganas por hacer bots para telegram,
me decidí por hacer mi propio bot para obtener los datos de los autobues usando la API publica de Zaragoza.

Asi es como hice mi primer bot.

Primero el lenguaje y los objetivos basicos:
- Python
- Recibir los tiempos de los autobuses en base a un numero de poste dado.

Dada la multitud de frameworks que hay para crear bots con este lenguaje, finalmente me decidi por |telepot|, ya que soporta asyncio.

.. |telepot| raw:: html

   <a href="https://telepot.readthedocs.io/en/latest/" target="_blank">telepot</a>


Queria usar |poetry| como gestor de dependencias para la aplicacion,
|docker| para aislar la aplicacion del sistema y poder desplegarlo de manera
sencilla, y la posibilidad de añadir comandos.

.. |poetry| raw:: html

  <a href="https://github.com/sdispater/poetry" target="_blank">poetry</a>

.. |docker| raw:: html

  <a href="https://www.docker.com/" target="_blank">docker </a>

Así encontré este |cookiecutter| que genera una base con telepot, poetry y
generacion de comandos.

.. |cookiecutter| raw:: html

  <a href="https://github.com/necros-surion/cookiecutter_telegram_bot" target="_blank">cookiecutter</a>

Una vez generada la base y comprobado su funcionamiento, se crea el Dockerfile y
se despliega.

.. image:: |static|/pictures/sazut.jpg
    :width: 640 px
    :height: 1280 px
    :align: center
    :alt: Sazut works

Hasta aqui la primera version.

Espero que haya sido util para descubrir algunas herramientas como poetry o el
cookiecutter!

Un saludo!
