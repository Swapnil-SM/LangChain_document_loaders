from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])  # here u can apply lazy load and with the help of LLM u can ask questions on the data like what is the average age of people who bought the product