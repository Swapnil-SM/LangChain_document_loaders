from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', #it will  load all files that matches with this pattern
    loader_cls=PyPDFLoader #specify which loader to use for loading the files since here i have pdf files
)

docs = loader.load()
print(len(docs)) # it will give total number of pages in all the pdf files combined
print(docs[0].page_content)  # it will give content of 1st page of 1st pdf file
print(docs[1].metadata)  # it will give metadata of 2nd page of 1st pdf file
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)