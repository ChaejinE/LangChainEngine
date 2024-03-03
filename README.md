# LangChainEngine
```bash
SERVICE_PATH="services/thesis_summary"
cd $SERVICE_PATH
```

```bash
pip install --upgrade pip && pip install pipenv
pipenv install && pipenv shell
```

## Unittest
```bash
# Test all
TEST_FILENAME=test_load_pdf
python -m unittest services.thesis_summary.test.${TEST_FILENAME}

# Test specific case function
TEST_CLASS_NAME=LoadPdfTest
TEST_FUNCTIONNAME=test_load
TEST_MODULE_CHAIN=${TEST_FILENAME}.${TEST_CLASS_NAME}.${TEST_FUNCTIONNAME}
python -m unittest services.thesis_summary.test.${TEST_MODULE_CHAIN}
```