install: #toggle env
	poetry install
brain-games: #run brain_games
	poetry run brain-games
build: #build package
	poetry build
publish: #publish package
	poetry publish --dry-run
package install: #pip install
	python3 -m pip install --user dist/*.whl