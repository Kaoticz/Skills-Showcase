from datetime import datetime
from langchain.retrievers import MultiQueryRetriever
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main():
    model_name: str = 'llama3.1'
    llm: ChatOllama = ChatOllama(model=model_name, temperature=0.4)
    system_prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(
        """
        Answer the question based ONLY on the following context:
        {context}
        Question: {question}
        """
    )

    workdir: str = input('Absolute path to directory to load the PDF files from: ')
    start_time: datetime = datetime.now()
    docs: list[Document] = PyPDFDirectoryLoader(
        path=workdir,
        recursive=True
    ).load()

    print(f'Loaded documents in {datetime.now() - start_time}')
    start_time: datetime = datetime.now()

    vector_db: Chroma = Chroma.from_documents(
        documents=RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100).split_documents(docs),
        embedding=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
        collection_name="local-rag"
    )

    retriever_prompt: PromptTemplate = PromptTemplate(
        input_variables=["question"],
        template="""
        You are an AI language model assistant. Your task is to generate five
        different versions of the given user question to retrieve relevant documents from
        a vector database. By generating multiple perspectives on the user question, your
        goal is to help the user overcome some of the limitations of the distance-based
        similarity search. Provide these alternative questions separated by newlines.
        Original question: {question}
        """
    )

    retriever: MultiQueryRetriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(),
        llm,
        prompt=retriever_prompt
    )

    chain = ({"context": retriever, "question": RunnablePassthrough()} | system_prompt | llm | StrOutputParser())

    print(f'Embedded documents in {datetime.now() - start_time}')
    print('Starting LLM, type "exit" to stop.')

    while True:
        user_input: str = input('>>> ')

        if user_input == 'exit':
            break

        start_time = datetime.now()
        response: str = chain.invoke(user_input)

        print(f'Response generated in {datetime.now() - start_time}')
        print('> ' + response + '\n')


if __name__ == '__main__':
    main()
