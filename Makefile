install: #toggle env
	poetry install
brain-games: #run brain-games
	poetry run brain-games
brain-even: #run brain_even
	poetry run brain-even
brain-calc: #run brain-calc
	poetry run brain-calc
brain-gcd: #run brain-gcd
	poetry run brain-gcd
brain-progression: #run brain-progression
	poetry run brain-progression
brain-prime: #run brain-prime
	poetry run brain-prime
build: #build package
	poetry build
publish: #publish package
	poetry publish --dry-run
package-install: #pip install #--force-reinstall
	python3 -m pip install --user dist/*.whl
package-reinstall: #reinstall package
	python3 -m pip install --force-reinstall dist/*.whl
lint: #run flake8 brain_games_cat
	poetry run flake8 brain_games_cat