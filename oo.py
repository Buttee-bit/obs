# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="padmajabfrl/Gender-Classification")
