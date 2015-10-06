release: clean lint
	git diff --exit-code # ensure there are no uncommitted changes
	git tag -a \
			-m v`python -c 'import gabbi_html; print gabbi_html.__version__'` \
			v`python -c 'import gabbi_html; print gabbi_html.__version__'`
	git push origin master --tags
	python setup.py sdist upload

dist:
	python setup.py sdist

lint:
	pep8 *.py gabbi_html/*.py

clean:
	find . -name "*.pyc" | xargs rm || true
	rm -r gabbi_html.egg-info || true
	rm -r dist || true

.PHONY: release dist lint clean
