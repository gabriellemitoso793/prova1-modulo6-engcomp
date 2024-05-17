# prova1-modulo6-engcomp

## Pré-requisitos

Certifique-se de ter o ROS 2 instalado em seu sistema. Consulte a [documentação oficial do ROS 2](https://docs.ros.org/en/galactic/Installation.html) para instruções de instalação.

## Instalação e Configuração

1. **Clone o Repositório:**
Primeiro é necesário clonar o repositório.


2. **Construa o Projeto:**
Acesse a pasta 'src' no seu terminal e execute os seguintes comandos para construir o projeto:

   ```bash
    cd src
    colcon build
    source install/local_setup.bash
   ```
## Executando o TurtleSim

1. **Inicie o TurtleSim:**
No terminal que você construiu o projeto, execute o TurtleSim, a execução abrirá a interface gráfica do TurtleSim com uma tartaruga.

    ```bash
   ros2 run turtlesim turtlesim_node
   ```

2. **Construção de Projeto no novo terminal:**
Em outro terminal, faça a construção do projeto:

    ```bash
    cd prova1-modulo6-engcomp/src
    source install/local_setup.bash
    ```

3. **Execute o Script do Projeto:**
No mesmo terminal, navegue até o diretório do projeto e execute o script responsável por enviar comandos para desenhar e manipular a tartaruga:

    ```bash
    cd prova1-modulo6-engcomp/src
    ros2 run ola_mundo cli-prova.py --vx 0.0 --vy 1.0 --vt 0.0 -t 1000
    ```
