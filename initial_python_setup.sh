pipenv --python 3.10.4
pipenv install --dev pytest
pipenv install --dev pytest-cov 
pipenv install --dev blue # PEP8 Formater linter
pipenv install --dev isort # import libs sorting linter
pipenv install --dev taskipy # automation scripting


pipenv requirements > requirements.txt
pipenv requirements --dev > dev-requirements.txt