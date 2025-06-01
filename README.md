# Graphic Card Market Simulator
Este proyecto es un reto de código orientado a objetos en Python. 

## Comenzando

### Clonar este repositorio

```bash
# Clonar este repositorio
git clone https://github.com/TKadyear/graphic-card-market-simulator.git

# Entrar en el repositorio
cd graphic-card-market-simulator
```

### Ejecutar el proyecto

```bash
# Instalar las dependencias
pip install -r requirements.txt

# Ejecutar el script de simulación
python3 .
```

## Reto
El contexto del proyecto se basa en una economía basada en el intercambio de tarjetas gráficas donde hay una serie de agentes que operan con ciertas reglas.
En el mercado de tarjetas gráficas hay un stock limitado de 100.000 unidades y una serie de agentes económicos que compran y venden tarjetas gráficas en el mercado.

En cada iteración del mercado, se ordenan todos los agentes de forma aleatoria y uno a uno pueden elegir comprar una tarjeta, vender una tarjeta o no hacer nada. Cada vez que un agente compra, el precio de las tarjetas gráficas sube un 0.5%. Cada vez que un agente vende, el precio baja un 0.5%. En total en el mercado hay 100 agentes repartidos de la siguiente forma:

- **51 agentes aleatorios** que en cada iteración tienen 1/3 de probabilidades de comprar, 1/3 de probabilidades de vender y 1/3 de probabilidades de no hacer nada.

- **24 agentes tendenciales** que en cada iteración tienen un 75% de probabilidades de comprar y un25% de probabilidades de no hacer nada si el precio ha subido un 1% (o más) con respecto al final de la iteración anterior. En caso contrario tienen un 20% de probabilidades de vender y un 80% de probabilidades de no hacer nada.

- **24 agentes anti-tendenciales** que en cada iteración tienen un 75% de probabilidades de comprar y un 25% de probabilidades de no hacer nada si el precio ha bajado un 1% (o más) con respecto al final de la iteración anterior. En caso contrario tienen un 20% de probabilidades de vender y un 80% de probabilidades de no hacer nada.
- **1 agente especial** con el objetivo de maximizar su balance económico al final
de la simulación. El agente debe terminar la última iteración con cero tarjetas gráficas en su poder.

Cada agente cuenta con un **balance inicial de $1,000** y no puede tomar dinero prestado. Los agentes no pueden vender más tarjetas de las que tienen en su poder. Cada agente es consciente de que hay otros 100 agentes participando y de cómo se distribuyen las políticas de compra y venta en la población de agentes. Cada agente sabe cuál es su turno dentro de la iteración del mercado, pero desconoce la del
resto de agentes.

El mercado de tarjetas gráficas arranca con un precio unitario de $200.00 y a partir de ese momento los
agentes empiezan a operar. Se deben simular un total de 1.000 iteraciones.
## Explicación

WIP 

## Autora

* GitHub - [TKadyear](https://github.com/TKadyear)
* LinkedIn - [Tamara Kadyear Saber](https://www.linkedin.com/in/tamara-kadyear-saber/)