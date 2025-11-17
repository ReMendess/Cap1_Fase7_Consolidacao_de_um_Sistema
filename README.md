
<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Despertar da rede neural - Fase 7 - Cap1
Link do vídeo: 

## Nome do Grupo

- Arthur Luiz Rosado Alves -> RM562061
- Renan de Oliveira Mendes -> RM563145

## Sumário
[1. Fase 1 – Base de Dados/API Metereologica](#c1)

[2. Fase 2 – Banco de Dados Estruturado](#c2)

[3. Fase 3 – IoT e Automação](#c3)

[4. Fase 4 – Dashboard Interativo com Data Science](#c4)

[5. Fase 5 – Cloud Computing/Scikit_Learn](#c5)

[6. Fase 6 – Visão Computacional](#c6)

[7. Fase 7 – Consolidação e AW](#c7)

[8. Ir Além 1](#c8)

[9. Ir Além 2](#c9)


# <a name="c1"></a>1. Base de Dados/API Metereologica
Na primeira entrega criamos duas aplicações. Uma  aplicação de entrada de dados em Python e outra aplicação de análise estatísca desses dados, em R - arquivos: "Fase1&2Banco_de_dados.py" e "Analise_R.R"
Utilizamos os registros no arquivo "dados_agricultura.csv".

Além disso, criamos uma aplicação extra, no qual entramos com o nome da cidade, e é realizada a chamada de uma API pública que resgata informações metereologicas do lugar. Essa aplicação simula o controle de uma bomba de água e caso ela detecte uma umidade muito baixa, ela aciona e ativa as bombas de irrigação.

<img src="assets/API.png" widht="150">
<img src="assets/API3.png" widht="150">

# <a name="c2"></a>2. Fase 2 – Banco de Dados Estruturado

Na segunda entrega, focado na parte estrutural, iniciamos criando um MER, em seguida criamos um banco de dados relacional, com a ferramenta SQL-Developer da Oracle e ampliamos nossa aplicação python, com novas funções CRUD e de seleção de dados.

Link MER: https://github.com/aarthurrosado/Fazenda

<img src="assets/MER.png" widht="150">

<img src="assets/banco_dados5.png" widht="150">


# <a name="c3"></a>3. Fase 3 – Fase 3 – IoT e Automação

Na terceira fase, entramos na parte de Iot com microprocessadores e sensores.
Usando wokwi e sensores reais e criamos uma aplicação de captação e monitoramento de dados. Desenvolveu-se um sistema IoT completo para irrigação automatizada conectado ao banco de dados. Usando a lógica de ativação automática da irrigação.

Link: https://github.com/ReMendess/Maquina_Agricola_Cap1

<img src="assets/wokwi.png" widht="150">

<img src="assets/wokwi_1.jpg" widht="150">


# <a name="c4"></a>4. Fase 4 – Fase 4 – Dashboard Interativo com Data Science

Na quarta fase, usando Streamlit, integramos Machine Learning em um dashboard online para análise exploratória dos dados. Também aprimoramos nosso ESP32 para monitoramento e criamos algoritmos preditivos de irrigação e manejo agrícola.

Link: https://github.com/ReMendess/Fase_4_Cap_1_Autom.Intelig.

<img src="assets/analise_exp3 (1).png" widht="150">

<img src="assets/modelo.png" widht="150">

# <a name="c5"></a>5. Fase 5 – Cloud Computing/Scikit_Learn

Quinta fase, usando Scikit_Learn treinamos e testamos diferentes modelos de Machine Learning. Criamos diferentes serviços na AWS, e orçamos em diferentes regiões.
Fomos além e usando ESP32 reais com dois sensores: DHT22 e Capacitive Soil Moisture Sensor v2.0, criamos uma aplicação de monitoramento e visualização via HTML e com protocolo MQTT

Link: https://github.com/ReMendess/Fase_5_Cap_1_FarmTech_Cloud_Comput

<img src="assets/Entrega1III (1).png" widht="150">

<img src="assets/Entrega2IIIV (1).png" widht="150">

<img src="assets/ESP32_Sensores2 (1).jpeg" widht="150">

<img src="assets/CodigoC (1).jpeg" widht="150">

<img src="assets/HTML_Leitura2 (1).jpeg" widht="150">

# <a name="c6"></a>6. Fase 6 – Visão Computacional

Sexta fase, usando visão computacional com redes neurais, testamos diferentes modelos YOLO, criamos nosso modelo do 0, e ainda realizamos Fine Tunning e Segmentação.
Usando uma base de imagens de cachorros e gatos

Link: https://github.com/ReMendess/Rede_Neural_FIAP_Cap1_Fase6

<img src="assets/MakeSensecachorro.png" widht="150">

<img src="assets/Entrega1_Yolo3 (1).png" widht="150">

<img src="assets/Entrega1_Yolo2 (1).png" widht="150">

<img src="assets/IrAlem2_Segment (1).png" widht="150">

# <a name="c7"></a>7. Fase 7 – Consolidação e AWS.

Nessa última fase, consolidamos todas as aplicações em uma só - "Fase7.py"
Nela podemos realizar a inserção de dados, operações CRUD, consultar API, captar dados com ESP32, treinar diversos modelos com Scikit Learn, ou treinar modelos de redes neuras com Yolo.

Além disso, aprofundamos com AWS hospedando alguns dos nossos serviços e infra garatindo a disponibilidade e escalabilidade.

### Aplicação final:
<img src="assets/Fase7.png" widht="150">

<img src="assets/Fase7II.png" widht="150">

<img src="assets/Fase7II.png" widht="150">

### Aqui criamos serviços de armazenamento de dados com DynamoDB

<img src="assets/fase5II.png" widht="150">

<img src="assets/fase5III.png" widht="150">

### Criamos um bucket com S3
<img src="assets/fase5IV.png" widht="150">

<img src="assets/fase5V.png" widht="150">

# <a name="c8"></a>8. Ir Além 1
Usando AWS Rekognition, configuramos e criamos um serviço de reconhecimento de imagem.

### Criamos um bucket e subimos imagens
<img src="assets/irAlem.png" widht="150">

### Atualizamos as politicas e criamos um usúario com permissão para usar o serviço do Rekognition
<img src="assets/irAlemII.png" widht="150">

### Acessando o Rekognition montamos toda a estrutura, pegando as imagens do bucket para treinar o modelo, rotular e dar deploy
<img src="assets/irAlemIII.png" widht="150">

<img src="assets/irAlemIV.png" widht="150">

<img src="assets/irAlemV.png" widht="150">

<img src="assets/irAlemVI.png" widht="150">

# <a name="c9"></a>9. Ir Além 2

