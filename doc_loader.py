from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs)) # it will give number of pages in the pdf as length of list

print(docs[0].page_content)  # it will give content of 1st page
print(docs[1].metadata)  # it will give metadata of 2nd page