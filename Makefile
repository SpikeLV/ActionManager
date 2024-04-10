install:
	# install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
form:
	#form code
test:
	#test
deploy:
	#deploy
all: install test deploy