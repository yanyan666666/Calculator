FROM python:3

ADD src /scr



CMD [ "python", "./src/CalculatorTests.py" ]