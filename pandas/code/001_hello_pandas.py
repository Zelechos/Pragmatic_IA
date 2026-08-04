import pandas as pd

filename = "/home/argusaphocraphex/Desktop/repositories/Pragmatic_IA/pandas/datasets/AirQualityUCI.csv"

dataset = pd.read_csv(filename, delimiter=";", encoding="latin-1")
dataset_utf = pd.read_csv(filename, delimiter=";", encoding="utf-8")

print(dataset.shape[0])
print(dataset_utf.shape[0])
