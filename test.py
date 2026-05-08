from utils.llm import generate_summary

text = "We only have 4 months of runway left and growth has slowed."

response = generate_summary(text)

print(response)