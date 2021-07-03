# Pragmatic_IA
## Todo Sobre Inteligencia Artificial , 1000 Júpiter Notebooks para Aprender y Practicar
### Recursos
---------------------------------------------------------------------------------------------
- [Continuar estudio de IA aqui](https://www.youtube.com/watch?v=JuQz-SFN8CY&list=PLkgbkukKg_Nrk7OtpwZEdVa10LijfpyZ1&index=4)
- [Respositorio sensio](https://github.com/juansensio/blog)
- [Repositorio Sis 421](https://github.com/cwpachecol/SIS421)
--------------------------------------------------------------------------------------------

# Protocolo para Crear modelos con Datasets Desconocidos
--------------------------------------------------------------------------------------------
## [Paso 0] Crear un dataset o descargar a dataset a usar y estudiar su estructura y su tipo de dato
--------------------------------------------------------------------------------------------
## [Paso 1] Descargar los Datos o importar el dataset que vayas a trabajar a tu proyecto
--------------------------------------------------------------------------------------------
## [Paso 2] Preprosesar los datos y obtener los datos relevantes que serian los datos que nos interesan del dataset
--------------------------------------------------------------------------------------------
## [Paso 3] Una vez que hayamos obtenido los datos relevantes, convertirlos a tensores dado que la libreria que usaremos que es Pytorch trabaja con tensores pytorch 
--------------------------------------------------------------------------------------------
## [Paso 4] Teniendo los tensores crear el dataset que es heredada de torch.utils.data.Dataset
--------------------------------------------------------------------------------------------
## [Paso 5] Creamos el Dataloader para entrenar nuestro algoritmo con iteraciones de batches donde tenemos que pasarle nuestro dataset como parametro
--------------------------------------------------------------------------------------------
## [Paso 6] Creamos el modelo o importamos el modelo que vayamos a utilizar para el entrenamiento
--------------------------------------------------------------------------------------------
## [Paso 7] Creamos la funcion de perdida y utilizamos el descenso de gradiente que viene implementados en pytorch
--------------------------------------------------------------------------------------------
## [Paso 8] Entrenamos el modelos con el conjunto de baches por iteracion que me genere el dataloader
--------------------------------------------------------------------------------------------
