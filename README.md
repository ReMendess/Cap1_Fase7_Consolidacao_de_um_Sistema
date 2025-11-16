# FIAP - Faculdade de Informática e Administração Paulista

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
[1. Organização do drive e Tratamento](#c1)

[2. Entrega1](#c2)

[3. Entrega2](#c3)

[4. IrAlém2](#c5)

---

# <a name="c1"></a>1. Organização do drive Coleta e Rotulagem

Para o treinamento de todos os modelos que estão separados entre: Entrega1, Entrega2, IrAlem e IrAlem2

Criamos um diretório no drive.
O diretório está dentro da pasta Entrega1.
*FIAP_FASE6*

A organização do diretório ficou da seguinte forma
```
FIAP/
├── data.yaml                          # Arquivo de configuração do dataset
│
├── FIAP_FASE6/                        # Pasta principal do dataset
│   ├── images/
│   │   ├── train/                     # Imagens de treino
│   │   │   ├── cachorro1.jpg
│   │   │   └── gato1.jpg
│   │   └── val/                       # Imagens de validação
│   │       ├── cachorro_val1.jpg
│   │       └── gato_val1.jpg
│   │
│   ├── labels/                        # Anotações YOLO
│   │   ├── train/                     # Labels de treino (.txt)
│   │   │   ├── cachorro1.txt
│   │   │   └── gato1.txt
│   │   └── val/                       # Labels de validação (.txt)
│   │       ├── cachorro_val1.txt
│   │       └── gato_val1.txt
│   │
│   └── test/                          # Imagens novas para teste do modelo
│       ├── teste1.jpg
│       └── teste2.jpg
│
└── notebooks/
    └── treino_yolo11.ipynb            # Notebook do Colab com o processo completo
```
## Coleta Imagens

Classes: 
- Cachorro
- Gato
  
    
Ao todo, foram coletadas **80 imagens**, sendo **40 de cada classe**.  
Essas imagens foram divididas proporcionalmente entre as etapas de **treinamento**, **validação** e **teste**, conforme a tabela abaixo:

| Classe     | Total de Imagens | Treino | Validação | Teste |
|-------------|------------------|--------|------------|--------|
| Cachorro  | 40               | 32     | 4          | 4      |
| Gato      | 40               | 32     | 4          | 4      |
| **Total**   | **80**           | **64** | **8**      | **8**  |

## Rotulagem da imagens pelo MakeSense

Aplicamos a Rotulagem das imagens coletadas pelo site do MakeSense

<img src="assets/MakeSensecachorro.png" alt="Execução dos testes" widht="150">


<img src="assets/makeSenseGato.png" alt="Execução dos testes" widht="15">


# <a name="c2"></a>2. Entrega1

## Treinamento 1 - Yolo11s

O primeiro modelo foi treinado utilizando a arquitetura **YOLO11s**, com o objetivo de realizar a detecção de duas classes: **Gato** e **Cachorro**.  
O treinamento foi executado por **40 épocas (epochs)**.



O treinamento foi realizado em GPU **Tesla T4 (CUDA)**, com monitoramento contínuo das métricas de desempenho — **Precision**, **Recall**, **mAP50** e **mAP50-95** — permitindo avaliar o aprendizado e possíveis sinais de *overfitting*.  
Ao final das 40 épocas, o modelo apresentou desempenho satisfatório, validando o fluxo completo de **treinamento, validação e teste** em uma rede YOLO.

###  Resultados do Treinamento 01 - 80 épocas

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Precision** | 0.992 | Percentual de detecções corretas entre todas as predições feitas. |
| **Recall** | 0.5 | Percentual de objetos reais corretamente detectados pelo modelo. |
| **mAP50** |  0.608 | Média de precisão considerando IoU = 0.5. |
| **mAP50-95** | 0.55 | Média de precisão considerando IoU entre 0.5 e 0.95. |

<img src="assets/Entrega1_Yolo.png" alt="Execução dos testes" widht="50">

<img src="assets/Entrega1_Yolo2.png" alt="Execução dos testes" widht="50">


Observando a evolução das métricas ao longo das 80 épocas, Nas primeiras 30–40 épocas, o modelo apresenta ganhos consistentes de precisão e Recall, o que indica aprendizado efetivo das classes “Gato” e “Cachorro”. Porém, após esse ponto, as curvas passam a oscilar fortemente e apresentar tendência de queda, especialmente nas métricas mAP50 e mAP50-95. Indicando assim um overfitting do modelo após certo ponto. Portanto, o YOLO11s atingiu seu melhor desempenho entre as epochs 40 e 55, antes de começar a degradar gradualmente. 

## Treinamento 02 - 60 épocas

O Segundo modelo foi treinado utilizando a mesma arquitetura **YOLO11s**, com o objetivo de realizar a detecção de duas classes: **Gato** e **Cachorro**.  
O treinamento foi executado por **60 épocas** Seguindo a lógica de comparar os resultados finais.

###  Resultados do Treinamento 01 - 80 épocas

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Precision** | 0.834 | Percentual de detecções corretas entre todas as predições feitas. |
| **Recall** | 0.75 | Percentual de objetos reais corretamente detectados pelo modelo. |
| **mAP50** |  0.862 | Média de precisão considerando IoU = 0.5. |
| **mAP50-95** | 0.538 | Média de precisão considerando IoU entre 0.5 e 0.95. |

<img src="assets/Entrega1_Yolo3.png" alt="Execução dos testes" widht="50">

# <a name="c3"></a>3. Entrega2

Para a segunda entrega treinamos mais dois modelos. O Yolov5 tradicional e um modelo customizado, criado do zero de classificação.

## Treinamento 3 - Yolov5 - Tradicional

O terceiro modelo foi treinado utilizando a arquitetura **YOLOv5**, com o objetivo de realizar a detecção de duas classes: **Gato** e **Cachorro**.  
O treinamento foi executado por **60 épocas (epochs)**.

<img src="assets/Entrega2_Yolo2.png" alt="Execução dos testes" widht="50">

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Precision** | 0.738 | Percentual de detecções corretas entre todas as predições feitas. |
| **Recall** | 0.945 | Percentual de objetos reais corretamente detectados pelo modelo. |
| **mAP50** |  0.91 | Média de precisão considerando IoU = 0.5. |
| **mAP50-95** | 0.625 | Média de precisão considerando IoU entre 0.5 e 0.95. |

<img src="assets/Entrega2_Yolo.png" alt="Execução dos testes" widht="50">

O modelo tradicional se mostrou mais desbalanceado, acertando as majoriatamente apenas a classe "Gato".


## Treinamento 4 - Modelo Customizado criado do 0.

O quarto modelo é um modelo de classificação. foi criado com uma arquitetura de seis camadas de extração de features e de redução de dimensionalidade (Conv2D e Pooling) e duas camadas densas de classificação.

Usando Rescaling para normalizar, aplicando 32 filtros na primeira camada e 128 na última.

<img src="assets/Entrega2_Yolo4.png" alt="Execução dos testes" widht="50">

O treinamento foi executado por **60 épocas (epochs)**.

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Precision** | 0.75 | Percentual de detecções corretas entre todas as predições feitas. |
| **Recall** | 0.75 | Percentual de objetos reais corretamente detectados pelo modelo. |

<img src="assets/Entrega2_Yolo3.png" alt="Execução dos testes" widht="50">

O modelo criado do zero seguiu a mesma linha do modelo Yolo, com uma acurácia de 0.75 para ambas as classes. Assim como o modelo Yolo ela identifcou melhor as imagens com gatos.

# <a name="c4"></a>4. IrAlem2
Para o Ir Além 2, a proposta é utilizar Transfer Learning e Fine Tuning, além de aplicar uma rede de segmentação do objeto desejado, criando uma máscara, para facilitar o aprendizado do modelo.

## Treinamento 5 - Modelo com Transfer Learning e Fine Tuning.

O quino modelo foi criado usando o MobileNetV2, que já é pré-treinado no ImageNet, com os pesos congelados. 
Adicionamos 10 epochs de treinamento em uma camada densa.

<img src="assets/IrAlem2.png" alt="Execução dos testes" widht="50">

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Accuracy** | 1.0000 | Percentual de detecções corretas entre todas as predições feitas. |
| **Loss** | 0.0027 | Percentual de erro/distância da predição para a classe certa. |

O Transfer Learning se mostrou o mais poderoso. E o mais propenso a overfitting.

<img src="assets/Entrega2_Yolo3.png" alt="Execução dos testes" widht="50">

## Treinamento 6 - Modelo com dados Segmentados. Transfer Learning e Fine Tuning.

O sexto modelo foi criado com as imagens segmentadas automáticamente, usando um modelo U-Net com um backbone.
Treinamos com MobileNetV2, com os pesos congelados, semelhante ao treinamento do sexto modelo. 

A segmentação autómatica não conseguiu identificar com clareza os pixels.

<img src="assets/IrAlem2_Segment.png" alt="Execução dos testes" widht="50">
<img src="assets/IrAlem2_Segment2.png" alt="Execução dos testes" widht="50">

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Accuracy** | 0.7500| Percentual de detecções corretas entre todas as predições feitas. |
| **Loss** | 0.8014 | Percentual de erro/distância da predição para a classe certa. |

Esse modelo com os dados segmentados obteve um desempenho regular.

<img src="assets/IrAlem2_SCompar.png" alt="Execução dos testes" widht="50">

## Treinamento 7 - Segmentação com FastSAM + Transfer Learning e Fine Tuning.

Utilizamos o FastSAM para segmentar todas as imagens de treino e validação. 
Treinamos com MobileNetV2, com os pesos congelados, semelhante ao treinamento do sexto modelo. 

O modelo deu overfitting, o que reforça a força da segmentação.

| Métrica | Valor | Interpretação |
|----------|--------|---------------|
| **Accuracy** | 1.0000 | Percentual de detecções corretas entre todas as predições feitas. |
| **Loss** | 4.3373e-08 | Percentual de erro/distância da predição para a classe certa. |

<img src="assets/IrAlem2_Segment3.png" alt="Execução dos testes" widht="50">

# Análise e Comparação final
Cada modelo demonstrou resultados unícos e diferentes. O modelo Yolo11s, treinado com diferente epócas, foi muito bom para identificar gatos e cachorros.
O modelo tradicional Yolov5 não conseguiu identificar com clareza as imagens com cachorros. Existem diversas explicações para esse fenômeno, a principal é referente as diferentes raças de cachorros no pequeno volume de dados para treinamento. O que dificultou a extração e aprendizado de features pelo modelo.
Por fim, Usar transfer learning e fine tuning se mostrou a estratégia mais poderosa, mas também mais propícia a dar overfitting. Segmentar os dados se mostrou bem eficiente, trazendo boas métricas, mesmo usando segmentações automáticas.
Dentre os modelos Yolo, o Yolo11s se mostrou o melhor. Algo já previsto, sabendo é a versão mais otimizada.
O modelo customizado, criado do zero foi bom, apesar das limitações e da quantidade de épocas treinadas.
Conseguimos com sucesso treinar diferentes modelos, com diferentes parametros e explorar com sucesso as diferentes estruturas de redes e abordagens, como transfer learning e fine tuning.
