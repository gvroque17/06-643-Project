flake8:
	flake8 --extend-ignore=F401,E501  --exclude build,.ipynb_checkpoints,__pycache__,*.egg-info  .

black: 
	black .

test:
	pytest .

all: black flake8 test
