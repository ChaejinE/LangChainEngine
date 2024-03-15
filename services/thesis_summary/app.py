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
    url: str = "https://arxiv.org/pdf/1706.03762.pdf"
    file: bytes = Field(..., extra={"widget": {"type": "base64file"}})


def main(request: ThesisSummaryReuqest) -> str:
    save_path = "/tmp/tmp.pdf"
    if request.file:
        import base64

        b = base64.decodebytes(request.file)
        with open(save_path, "wb") as f:
            f.write(b)

    chain_manager = ThesisSummaryChain()
    chain = chain_manager.make_chain(file_uri=request.url, file_path=save_path)
    result = chain.invoke()
    return result


add_routes(
    app,
    RunnableLambda(main).with_types(input_type=ThesisSummaryReuqest, output_type=str),
    path="/summary",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
