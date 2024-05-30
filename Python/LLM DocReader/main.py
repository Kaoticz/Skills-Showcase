from datetime import datetime
from langchain.chains import combine_documents
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.llms.ollama import Ollama
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable


def main():
    model_name: str = 'dolphin-mixtral'
    llm: Ollama = Ollama(model=model_name, temperature=0.2)
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
        [
            ('system', 'Answer the question based only on the following context:\n\n{context}'),
            ('user', '{input}')
        ]
    )

    doc_chain: Runnable = combine_documents.create_stuff_documents_chain(llm, prompt)
    workdir: str = input('Absolute path to directory to load the PDF files from: ')
    start_time: datetime = datetime.now()
    docs: list[Document] = PyPDFDirectoryLoader(
        path=workdir,
        recursive=True
    ).load()

    print(f'Loaded documents in {datetime.now() - start_time}')
    print('Starting LLM, type "exit" to stop.')

    while True:
        user_input: str = input('>>> ')

        if user_input == 'exit':
            break

        start_time = datetime.now()
        response: str = doc_chain.invoke(
            {
                'input': 'According to the provided context, ' + user_input,
                'context': docs
            }
        )

        print(f'Response generated in {datetime.now() - start_time}')
        print('> ' + response + '\n')


if __name__ == '__main__':
    main()
