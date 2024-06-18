
# Interface de gestos para apresentação de slides

Este projeto, desenvolvido em Python, permite o controle interativo de slides de apresentação através de gestos manuais capturados por uma webcam. Utilizando as bibliotecas OpenCV e CVZone, o principal objetivo da aplicação é reconhecer gestos específicos para navegar pelos slides.


## Descrição


O projeto oferece uma interface intuitiva que permite aos usuários controlar slides de apresentação através do reconhecimento de gestos manuais capturados em tempo real via webcam. Com este sistema, os apresentadores podem alternar entre slides.


## Tecnologias Usadas

* **Python :** Linguagem principal do projeto para desenvolver as funcionalidades e a lógica da aplicação.
* **OpenCV (cv2) :** Gerencia o acesso à webcam, manipulação de imagens e reconhecimento de gestos para controle de navegação e anotações nos slides.
* **CVZone :** Fornece ferramentas e funções especializadas para rastreamento preciso das mãos e interações baseadas em gestos nos slides de apresentação.
## Requisitos e Configurações Necessárias

**Requisitos -**

* Python 3.x
* Webcam


**ConfiguraçÕes -**

* Ajuste a resolução da webcam através das variáveis ``width`` e ``height``.
* Modifique o ``FolderPath`` para o diretório contendo os slides de apresentação no arquivo ``main.py``.
* Ajuste ``gestureThreshold``, ``button_delay`` e outros parâmetros conforme necessário.
## Processo de utilização

**Step 1 :** Clone o Repositório : 

```bash
  git clone https://github.com/AkshataKamerkar/GestureFlow.git
```

**Step 2 :** Set Up Environment and Dependencies
* **Instale o Python :**  Instale o python, de preferência um versão da 3.0 para cima.

* **Instale as bilbiotecas necessárias :** Vá até a pasta do projeto e rode o seguinte comando -

```bash
  pip install -r requirements.txt

```
O arquivo ``requirements.txt`` possui todas as dependências necessárias.

**Step 3 :** Configure e Rode o projeto

* **Colocar os Slides de Apresentação:** Siga as instruções do projeto para colocar os slides de apresentação na pasta designada (ppt ou conforme especificado).

* **Se Necessário Ajustar Configurações:** Modifique quaisquer parâmetros de configuração no código, como a resolução da webcam ou os caminhos das pastas.

* **Executar o Script:** Execute o script Python que controla os slides de apresentação -

```bash
  python main.py
```

**Step 4 :** Sair do projeto rodando
Aperte a tecla `Q` ou feche o terminal que está rodando a aplicação.

