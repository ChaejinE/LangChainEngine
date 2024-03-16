# Reference
- [map-reduce](https://python.langchain.com/docs/use_cases/summarization#option-2.-map-reduce)

# Run on Local
## Setup Environment on Local
```bash
pip install --upgrade pip && pip install pipenv
pipenv install && pipenv shell
```

## Run
```bash
python -m services.thesis_summary.app
```

## Unittest
```bash
TEST_FILENAME=test_chain

# For specific case function
TEST_CLASS_NAME=ChainTest
TEST_FUNCTIONNAME=test_run
TEST_MODULE_CHAIN=${TEST_FILENAME}.${TEST_CLASS_NAME}.${TEST_FUNCTIONNAME}
```

```bash
# Test all
python -m unittest services.thesis_summary.test.${TEST_FILENAME}

# Test specific case function
python -m unittest services.thesis_summary.test.${TEST_MODULE_CHAIN}
```

# Docker run
```bash
PYTHON_VERSION=3.9.6
docker run --name thesis_summary_langchain -it --rm -d --net host -e OPENAI_API_KEY=${OPENAI_API_KEY} -v .:/usr/src/app -p 8000:8000 python:${PYTHON_VERSION}-slim
```

## Installed pkgs
```bash
apt update && apt-get install -y libgl1-mesa-glx libglib2.0-0
```
