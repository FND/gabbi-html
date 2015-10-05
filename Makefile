release: clean lint
	git diff --exit-code # ensure there are no uncommitted changes
	# TODO: automate SCM tagging
	python setup.py sdist upload

dist:
	python setup.py sdist

lint:
	pep8 *.py

clean:
	find . -name "*.pyc" | xargs rm || true
	rm -r gabbi_html.egg-info || true
	rm -r dist || true

.PHONY: release dist lint clean
