black: 
	black --line-length 79 .
    
flake8:
	flake8 --extend-ignore=F401,E501  --exclude build,pkg,.ipynb_checkpoints,__pycache__,*.egg-info  .

test:
	pytest .

all: black flake8 test
