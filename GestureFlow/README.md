
# GestureFlow 

Este projeto, desenvolvido em Python, permite o controle interativo de slides de apresentação através de gestos manuais capturados por uma webcam. Utilizando as bibliotecas OpenCV e CVZone, a aplicação reconhece gestos específicos para navegar pelos slides e realizar anotações em tempo real


## Descrição


O projeto oferece uma interface intuitiva que permite aos usuários controlar slides de apresentação através do reconhecimento de gestos manuais capturados em tempo real via webcam. Com este sistema, os apresentadores podem alternar entre slides, desenhar anotações e usar o dedo como ponteiro.
## Principais Funcionalidades
* **Controle por Gestos**: Navegue pelos slides com gestos de mão para a esquerda e para a direita, imitando o folhear de páginas para transições suaves.
  
* **Anotação**: Desenhe nos slides usando gestos manuais, permitindo ilustrações ou ênfases durante as apresentações.
  
* **Modo Ponteiro**: Utilize o dedo indicador como ponteiro virtual, aprimorando a interação e o engajamento com elementos específicos nos slides.
  
* **Limpar Anotações**: Limpe instantaneamente as anotações desenhadas com um gesto específico, garantindo uma tela limpa para novas interações.


## Tecnologias Usadas

* **Python :** Linguagem principal do projeto para desenvolver as funcionalidades e a lógica da aplicação.
* **OpenCV (cv2) :** Gerencia o acesso à webcam, manipulação de imagens e reconhecimento de gestos para controle de navegação e anotações nos slides.
* **NumPy :** Auxilia no manejo eficiente e na manipulação dos dados de imagem para reconhecimento e processamento de gestos.
* **CVZone :** Fornece ferramentas e funções especializadas para rastreamento preciso das mãos e interações baseadas em gestos nos slides de apresentação.
## Requisitos e Configurações Necessárias

**Requisitos -**

* Python 3.x
* Webcam


**Configurations -**

* Ajuste a resolução da webcam através das variáveis ``width`` e ``height``.
* Modifique o ``FolderPath`` para o diretório contendo os slides de apresentação no arquivo ``main.py``.
* Ajuste ``gestureThreshold``, ``button_delay`` e outros parâmetros conforme necessário.
## Deployment

Accessing the project involves a few steps:

**Step 1 :** Clone the Repository : 

```bash
  git clone https://github.com/AkshataKamerkar/GestureFlow.git
```

**Step 2 :** Set Up Environment and Dependencies
* **Install Python :**  Ensure Python (preferably Python 3.x) is installed on your system.

* **Install Required Libraries :** Navigate to the project directory and install the necessary Python libraries by running -

```bash
  pip install -r requirements.txt

```
If there's a requirements.txt file in the project, this command installs all the dependencies needed for the project to run.

**Step 3 :** Configure and Run the Project

* **Place Presentation Slides :** Follow the project's instructions to place the presentation slides in the designated folder (ppt or as specified).

* **Adjust Configuration (if required) :** Modify any configuration parameters in the code if needed, such as webcam resolution or folder paths.

* **Run the Script :** Execute the Python script that controls the presentation slides - 

```bash
  python main.py

```

* **Interact with the Presentation :** Use the hand gestures as specified in the project's README to control and interact with the presentation slides via the webcam.


**Step 4 :** Quitting the Application
Press the specified keyboard key 'q' to exit or close the application when done.

## Conclusion

The system offers a convenient gesture-based command to swiftly clear annotations. With a specific gesture, presenters can reset the slide, removing any drawn annotations instantly. This functionality ensures a clean slate for new annotations or a clear view of the original slide content.
## Contributors

* ak_639
* shubham-murtadak
* ItachiUchiha08
