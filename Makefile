install: #toggle env
	poetry install
brain-games: #run brain_games
	poetry run brain-games
brain-even: #run brain_even
	poetry run brain-even
brain-calc: #run vrain-calc
	poetry run brain-calc
build: #build package
	poetry build
publish: #publish package
	poetry publish --dry-run
package-install: #pip install #--force-reinstall
	python3 -m pip install --user dist/*.whl
package-reinstall:git #reinstall package
	python3 -m pip install --force-reinstall dist/*.whl
lint: #run flake8 brain_games_cat
	poetry run flake8 brain_games_catbrain