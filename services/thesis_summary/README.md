# Setup Environment on Local
```bash
pip install --upgrade pip && pip install pipenv
pipenv install && pipenv shell
```

# Unittest
```bash
TEST_FILENAME=test_prompt

# For specific case function
TEST_CLASS_NAME=PromptTest
TEST_FUNCTIONNAME=test_generate
TEST_MODULE_CHAIN=${TEST_FILENAME}.${TEST_CLASS_NAME}.${TEST_FUNCTIONNAME}
```

```bash
# Test all
python -m unittest test.${TEST_FILENAME}

# Test specific case function
python -m unittest test.${TEST_MODULE_CHAIN}
```
