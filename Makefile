lint:
	pep8 *.py

clean:
	find . -name "*.pyc" | xargs rm || true

.PHONY: lint clean
