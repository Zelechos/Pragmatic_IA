# Pragmatic IA

![Pragmatic IA](https://user-images.githubusercontent.com/41464891/209026004-31795ff6-3e44-4086-9064-a503b88189a6.jpg)

**Es un Proyecto de Experimentación en Inteligencia Artificial**

Este repositorio está dedicado a la experimentación, investigación y aprendizaje de diversas tecnologías en el campo de la Inteligencia Artificial (IA). 
El objetivo principal es crear un compendio de Codigo que aborden una variedad de temas relacionados con la IA. 
Este proyecto está dirigido por mi Msc. Alex T.H., para encaminarme en busca de mi doctorado y expandir mis conocimientos en este fascinante campo.

**Objetivo**
El objetivo principal de este repositorio es servir como una plataforma para la exploración y el estudio profundo de conceptos clave en inteligencia artificial. Se abordarán diversos temas, desde algoritmos de aprendizaje automático hasta redes neuronales profundas, pasando por técnicas de procesamiento de lenguaje natural y visión por computadora.

**Contenido**
El repositorio contendrá una colección de Codigo organizado temáticamente, cubriendo áreas clave de la inteligencia artificial. Cada Codigo incluirá explicaciones detalladas, código Python interactivo y ejemplos prácticos para facilitar el aprendizaje y la comprensión.

**Contribuciones**
Se alienta a la comunidad de IA y a cualquier persona interesada en el tema a contribuir al proyecto. Las contribuciones pueden incluir la adición de codigo nuevo, correcciones de errores, mejoras en la documentación o cualquier otra forma de colaboración que enriquezca el contenido y la experiencia de aprendizaje para todos.

**Contacto**
Para más información sobre el proyecto o para discutir posibles contribuciones, no dudes en ponerte en contacto con Msc. Alex T.H. a través de los siguientes medios:

**Ambiente**
Para crear un nuevo ambiente se utiliza el siguiente comando : 

```python
python3 -m venv .venv
```

Para activar el ambiente desde una terminal fish se utiliza el siguiente comando :

```python
source .venv/bin/activate.fish
```
Para desactivar el ambiente se utiliza el siguiente comando:

```python
deactivate
```
Para actualizar las despendencias de mi requirements.txt se utiliza el siguiente comando:

```python
pip frezze > requirements.txt
``` 

Sí. Pero haría una precisión importante: **5 meses no alcanzan para ser “experto mundial” en Deep Learning**, pero sí pueden darte una **base muy fuerte y práctica**, al nivel de poder leer papers, implementar modelos desde cero, entrenarlos, optimizarlos y empezar investigación seria.

Como quieres que **Deep Learning sea tu especialización principal**, yo no repartiría los 5 meses entre NLP, Computer Vision y Audio. Primero construiría el **núcleo de Deep Learning + PyTorch**.

## 🎯 Objetivo al terminar los 5 meses

Quiero que llegues a poder hacer esto sin depender de tutoriales:

```text
                 DEEP LEARNING
                       │
       ┌───────────────┴───────────────┐
       │                               │
   MATEMÁTICAS                       PYTORCH
       │                               │
       └───────────────┬───────────────┘
                       │
                NEURAL NETWORKS
                       │
                 BACKPROPAGATION
                       │
                  OPTIMIZATION
                       │
             ┌─────────┴─────────┐
             │                   │
        CNN / Vision        RNN / Sequence
             │                   │
             └─────────┬─────────┘
                       │
                   ATTENTION
                       │
                  TRANSFORMERS
                       │
                  EMBEDDINGS
                       │
              REPRESENTATION
                  LEARNING
                       │
            SELF-SUPERVISED
                  LEARNING
                       │
                 FINE-TUNING
                       │
          ┌────────────┴────────────┐
          │                         │
   DISTRIBUTED TRAINING       MODEL EFFICIENCY
                                    │
                           ┌────────┴────────┐
                           │                 │
                      QUANTIZATION    COMPRESSION
```

---

# 🗺️ Roadmap de 5 meses

Asumiendo aproximadamente **2–3 horas por día**, que es compatible con el tiempo de estudio que me has mencionado.

**6 días por semana**.

Una estructura que recomiendo:

```text
Lunes–Viernes: 2–3 h/día
Sábado:        3–4 h
Domingo:       descanso/revisión ligera
```

Y una regla:

> **30% teoría + 70% código.**

No quiero que pases cinco meses viendo cursos.

---

# MES 1 — Fundamentos de Deep Learning + PyTorch

### Objetivo

Entender realmente **qué está haciendo una red neuronal**.

No empezar todavía con Transformers.

### Semana 1 — Matemáticas para Deep Learning

Repasar:

* vectores
* matrices
* producto matricial
* derivadas
* derivadas parciales
* gradiente
* regla de la cadena
* funciones
* probabilidad básica
* distribución
* esperanza
* varianza

Especialmente:

### Gradiente

Debes entender:

```text
f(x,y)
  ↓
∂f/∂x
∂f/∂y
  ↓
∇f
```

No necesitas convertirte en matemático.

Necesitas poder **interpretar matemáticamente un paper**.

---

# Semana 2 — Perceptrón y redes neuronales

Implementar desde cero:

```text
Input
  ↓
Linear
  ↓
Activation
  ↓
Linear
  ↓
Output
```

Estudiar:

* perceptrón
* neurona
* pesos
* bias
* función de activación
* sigmoid
* tanh
* ReLU
* GELU
* softmax

Y entender:

```text
y = Wx + b
```

---

# Semana 3 — Backpropagation

Esta semana es **fundamental**.

Debes entender:

```text
Forward
   ↓
Prediction
   ↓
Loss
   ↓
Backward
   ↓
Gradients
   ↓
Update weights
```

Estudiar:

* computational graph
* chain rule
* gradients
* loss
* backpropagation
* autograd

### Proyecto

Implementa una pequeña red neuronal **sin PyTorch autograd**.

Después:

> implementa exactamente la misma red utilizando `torch.autograd`.

Esto te hará entender qué está haciendo PyTorch internamente.

---

# Semana 4 — PyTorch fundamental

Aquí empieza tu dominio real de PyTorch.

Aprender:

```python
import torch
```

y:

* Tensor
* shape
* dtype
* device
* CPU/GPU
* broadcasting
* indexing
* matrix operations
* autograd
* `nn.Module`
* `nn.Linear`
* `nn.ReLU`
* `nn.Sequential`

Después:

* Dataset
* DataLoader
* training loop
* validation loop
* loss functions
* optimizers

Debes poder escribir un training loop **sin copiarlo**.

---

# 🧠 MES 2 — Optimización + arquitecturas neuronales

Aquí empiezas a pensar como alguien de Deep Learning y no solamente como alguien que utiliza PyTorch.

---

# Semana 5 — Optimization

Estudia profundamente:

* Gradient Descent
* SGD
* Momentum
* Adam
* AdamW
* learning rate
* learning-rate schedules
* weight decay
* initialization

Conceptualmente:

```text
θ_new = θ_old - η ∇L(θ)
```

Comprender:

> ¿Qué pasa si learning rate es demasiado grande?

> ¿Qué pasa si es demasiado pequeño?

> ¿Por qué Adam funciona?

> ¿Qué diferencia hay entre Adam y AdamW?

---

# Semana 6 — Regularización

Estudiar:

* overfitting
* underfitting
* bias/variance
* dropout
* weight decay
* early stopping
* data augmentation
* normalization

Y:

* BatchNorm
* LayerNorm
* RMSNorm

---

# Semana 7 — CNN

Aunque quieras especializarte posteriormente en NLP, **debes estudiar CNN**.

Porque necesitas entender arquitecturas neuronales.

Estudiar:

* convolution
* filters
* kernels
* stride
* padding
* pooling
* receptive field

Arquitecturas:

* LeNet
* AlexNet
* VGG
* ResNet

### Proyecto

Entrena:

```text
CNN → CIFAR-10
```

Después implementa una versión simplificada de:

> **ResNet**

---

# Semana 8 — RNN y secuencias

Estudiar:

* sequence modeling
* RNN
* vanishing gradient
* exploding gradient
* LSTM
* GRU

Implementa:

```text
RNN
LSTM
GRU
```

en PyTorch.

Y haz un pequeño proyecto de predicción de secuencias.

---

# 🚀 MES 3 — Attention + Transformers

Este será uno de los meses más importantes para ti.

---

# Semana 9 — Embeddings

Entender profundamente:

> ¿Qué significa representar algo como un vector?

Estudiar:

* one-hot encoding
* dense representations
* word embeddings
* embedding matrix
* semantic similarity
* cosine similarity

Implementar:

```python
nn.Embedding
```

Después:

* Word2Vec
* Skip-gram
* CBOW

No necesitas entrenar Word2Vec gigante.

Necesitas entender **cómo funciona**.

---

# Semana 10 — Attention

Aquí debes ir muy profundo.

Entender:

```text
Query
Key
Value
```

y:

```text
Attention(Q,K,V)
=
softmax(QKᵀ / √dk)V
```

Estudiar:

* self-attention
* scaled dot-product attention
* multi-head attention
* masking

### Proyecto

Implementar:

> **Multi-Head Self Attention desde cero en PyTorch.**

No uses `nn.MultiheadAttention` inicialmente.

Hazlo tú.

Después compara tu implementación contra PyTorch.

---

# Semana 11 — Transformers

Ahora sí:

**Transformer completo.**

Entender:

```text
Input
 ↓
Embedding
 ↓
Positional Encoding
 ↓
Multi-Head Attention
 ↓
Add & Norm
 ↓
Feed Forward
 ↓
Add & Norm
 ↓
Output
```

Estudiar:

* encoder
* decoder
* positional encoding
* residual connections
* LayerNorm
* feed-forward network
* causal masking

Leer el paper:

> **Attention Is All You Need**

Y no solamente leerlo.

**Implementar un Transformer pequeño.**

---

# Semana 12 — GPT/BERT

Ahora estudias dos familias fundamentales.

### BERT

```text
Transformer Encoder
```

### GPT

```text
Transformer Decoder
```

Entender:

* masked language modeling
* causal language modeling
* tokenization
* positional embeddings
* pretraining

### Proyecto

Construir un:

> **Mini-GPT**

con PyTorch.

Pequeño.

No necesitas millones de dólares. 😄

Puedes entrenarlo con un dataset pequeño.

---

# 🔬 MES 4 — Representation Learning + Self-Supervised + Fine-Tuning

Aquí empiezas a entrar en terreno de investigación.

---

# Semana 13 — Representation Learning

Pregunta fundamental:

> ¿Cómo aprende una red una representación útil de los datos?

Estudiar:

* latent representations
* feature learning
* embeddings
* dimensionality reduction
* autoencoders
* representation spaces

Implementa:

> Autoencoder con PyTorch.

Después visualiza el espacio latente.

---

# Semana 14 — Self-Supervised Learning

Este concepto es extremadamente importante para el Deep Learning moderno.

Estudia:

* pretext tasks
* contrastive learning
* masked prediction
* positive/negative samples

Modelos/conceptos:

* SimCLR
* MoCo
* BYOL
* MAE

En NLP:

```text
Texto
 ↓
Mask
 ↓
Transformer
 ↓
Predicción
```

En visión:

```text
Imagen
 ↓
Mask
 ↓
Model
 ↓
Reconstrucción
```

Comprenderás que **no siempre necesitas etiquetas humanas para entrenar modelos potentes**.

---

# Semana 15 — Fine-Tuning

Ahora:

```text
Pretrained Model
       ↓
Fine-tuning
       ↓
Specific Task
```

Estudiar:

* transfer learning
* freezing
* unfreezing
* learning rates
* catastrophic forgetting
* full fine-tuning
* parameter-efficient fine-tuning

Después:

* LoRA
* adapters
* QLoRA

Y aquí ya puedes trabajar con modelos reales de Hugging Face + PyTorch.

---

# Semana 16 — Training avanzado

Aprender:

* mixed precision
* AMP
* gradient accumulation
* gradient clipping
* checkpointing
* experiment tracking
* reproducibility
* profiling

PyTorch:

```python
torch.cuda
torch.amp
torch.profiler
```

Debes saber responder:

> "Mi modelo necesita 24 GB de VRAM y tengo 8 GB. ¿Qué hago?"

Y pensar en:

* batch size
* gradient accumulation
* mixed precision
* checkpointing
* quantization
* model architecture

---

# ⚡ MES 5 — Distributed Training + Quantization + Compression

Aquí pasas de:

**"sé entrenar modelos"**

a:

**"sé entrenar modelos de manera eficiente."**

---

# Semana 17 — GPU y performance

Entender:

* CPU vs GPU
* CUDA
* VRAM
* tensor operations
* memory bandwidth
* compute
* bottlenecks

PyTorch:

* CUDA
* device management
* profiling

Aprender a encontrar:

> ¿por qué mi modelo tarda 2 horas?

---

# Semana 18 — Distributed Training

Estudiar:

* data parallelism
* model parallelism
* distributed data parallel
* gradient synchronization
* all-reduce

PyTorch:

```text
DistributedDataParallel
```

Después estudiar conceptualmente:

* FSDP
* DeepSpeed
* ZeRO

No necesitas convertirte en experto en infraestructura distribuida todavía.

Pero debes entender **cómo se entrenan modelos grandes**.

---

# Semana 19 — Quantization

Fundamental para AI Engineering.

Estudiar:

```text
FP32
 ↓
FP16
 ↓
INT8
 ↓
INT4
```

Entender:

* quantization
* calibration
* dynamic quantization
* static quantization
* quantization-aware training
* post-training quantization

Y posteriormente:

* GPTQ
* AWQ

---

# Semana 20 — Model Compression + proyecto final

Estudiar:

* pruning
* knowledge distillation
* parameter sharing
* low-rank approximation
* quantization
* efficient architectures

Y aquí haces **TU PROYECTO FINAL**.

---

# 🏆 Proyecto final de los 5 meses

Yo haría algo bastante más ambicioso que un simple clasificador.

## "Tiny Foundation Model"

Construir:

```text
Dataset
   ↓
Tokenizer
   ↓
Embeddings
   ↓
Transformer
   ↓
Pretraining
   ↓
Evaluation
   ↓
Fine-tuning
   ↓
Quantization
   ↓
Compression
   ↓
Inference
```

Con PyTorch.

Y documentarlo como si fuera un pequeño paper.

### Debes implementar tú:

* tokenizer básico
* embedding
* positional encoding
* attention
* multi-head attention
* Transformer block
* Transformer
* loss
* training loop
* validation
* checkpointing
* fine-tuning
* evaluación
* quantization

Y después comparar:

```text
                    Model
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
    FP32           FP16           INT8
       │              │              │
    Size X          Size X/2       Size X/4
       │              │              │
   Accuracy         Accuracy       Accuracy
```

Eso te dará una experiencia **muchísimo más profunda** que completar 20 cursos.

---

# 🔥 ¿Y PyTorch?

Yo quiero que después de 5 meses tengas este nivel:

### Nivel 1

```python
torch.tensor()
torch.matmul()
torch.mean()
torch.sum()
```

### Nivel 2

```python
nn.Module
nn.Linear
nn.Conv2d
nn.Embedding
nn.LayerNorm
```

### Nivel 3

```python
Dataset
DataLoader
Optimizer
Scheduler
Autograd
```

### Nivel 4

```python
AMP
CUDA
Profiler
Checkpointing
DistributedDataParallel
```

### Nivel 5

Que puedas abrir un paper y decir:

> "Voy a implementar esta arquitectura en PyTorch."

Y hacerlo.

**Ese es el objetivo real.**

---

# 📚 Orden exacto de estudio

No estudiaría 12 temas independientes.

Los organizaría así:

```text
FASE 1
Mathematics
     ↓
Neural Networks
     ↓
Backpropagation
     ↓
PyTorch
     ↓

FASE 2
Optimization
     ↓
Regularization
     ↓
CNN
     ↓
RNN/LSTM
     ↓

FASE 3
Embeddings
     ↓
Attention
     ↓
Transformers
     ↓
GPT/BERT
     ↓

FASE 4
Representation Learning
     ↓
Self-Supervised Learning
     ↓
Fine-Tuning
     ↓
LoRA / QLoRA
     ↓

FASE 5
GPU Optimization
     ↓
Distributed Training
     ↓
Quantization
     ↓
Model Compression
```

---

# ⏱️ Y algo MUY importante

No intentes aprender **NLP + Computer Vision + Audio simultáneamente durante estos cinco meses**.

Tu objetivo debería ser:

> **"Quiero dominar el motor."**

Ese motor es **Deep Learning + PyTorch**.

Después:

```text
             DEEP LEARNING
                   │
              PYTORCH
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
       NLP       Vision      Audio
        │          │          │
       LLMs       ViT       Speech
        │          │          │
       RAG       Diffusion   TTS/ASR
```

Correo electrónico: alextumirihuanca@gmail.com
LinkedIn: https://www.linkedin.com/in/alex-tumiri-huanca-6234b3195/ 

Alex Tumiri, M.sc.
