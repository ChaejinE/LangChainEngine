import os, sys
import logging

logging.basicConfig(level=logging.WARNING)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes, CustomUserType
from chain.chains import ThesisSummaryChain
from langchain_core.runnables import RunnableLambda
from langchain.pydantic_v1 import Field
from engine_logger.langchain_logger import logger

app = FastAPI(title="Thesis Summary Server")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ThesisSummaryReuqest(CustomUserType):
    url: str = None
    file: bytes = Field(default=None, extra={"widget": {"type": "base64file"}})


def main(request: ThesisSummaryReuqest) -> str:
    save_path = "/tmp/tmp.pdf"
    if request.file:
        import base64

        b = base64.decodebytes(request.file)
        with open(save_path, "wb") as f:
            f.write(b)

    chain_manager = ThesisSummaryChain()
    chain = chain_manager.make_chain()
    try:
        logger.info("Start to invoke")
        result = chain.invoke({"file_uri": request.url, "file_path": save_path})
        logger.info("Success to invoke")

    except Exception as e:
        logger.info("Fail to invoke")
        raise e

    return result["output_text"]


add_routes(
    app,
    RunnableLambda(main),
    path="/summary",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
