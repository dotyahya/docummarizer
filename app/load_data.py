from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader

def load_documents(DATA_PATH):
    doc_loader = PyPDFDirectoryLoader(DATA_PATH)
    return doc_loader.load()

documents = load_documents("../data/")
# print(documents[0])

