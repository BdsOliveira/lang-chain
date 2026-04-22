from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("Hello, my name is {name}! Please tell me a joke with {name}.")

prompt = template.format(name="Bruno")

print(prompt)