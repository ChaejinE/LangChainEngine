import os, sys
import logging

logging.basicConfig(level=logging.WARNING)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi import FastAPI
from langserve import add_routes, CustomUserType
from chain.chains import ThesisSummaryChain
from langchain_core.runnables import RunnableLambda

app = FastAPI(title="Thesis Summary Server")


class ThesisSummaryReuqest(CustomUserType):
    map_document_variable: str = "pages"
    map_system_prompt_template: str = (
        "You are the best AI thesis summary assistant about pages. This is partial of documents. Please summary about this page well."
    )
    map_partial_document_prompt_template: str = "{pages}"
    reduce_system_prompt_template: str = "{doc_summaries}"
    reduce_partial_document_prompt_template: str = (
        "You are the best AI thesis summary assistant about documents. This is set of thesis summary. Please summary about this set well."
    )
    reduce_document_variable: str = "doc_summaries"
    url: str = "https://arxiv.org/pdf/1706.03762.pdf"


def main(request: ThesisSummaryReuqest) -> str:
    chain_manager = ThesisSummaryChain()
    chain_manager.make_chain(
        map_document_variable=request.map_document_variable,
        map_system_prompt_template=request.map_system_prompt_template,
        map_user_prompt_template=request.map_partial_document_prompt_template,
        reduce_system_prompt_template=request.reduce_system_prompt_template,
        reduce_user_prompt_template=request.reduce_partial_document_prompt_template,
        reduce_document_variable=request.reduce_document_variable,
    )
    result = chain_manager.invoke(file_uri=request.url)
    return result


add_routes(app, RunnableLambda(main), path="/summary")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
