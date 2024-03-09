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
python services.thesis_summary.app.py
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
