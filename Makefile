flake:
	flake8 http_request.py 
	
clean:
	rm -f `find . -type f -name '*.py[co]'`

