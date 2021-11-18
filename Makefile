gx:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook galaxy.yml --diff --extra-vars "__galaxy_dir_perms='0755' os_env_umask='022'"

it-test-galaxy:
	./bin/clean-deps.py
	#ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook it-test-galaxy.yml --diff --extra-vars "__galaxy_dir_perms='0755' os_env_umask='022'"

agoge:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook agoge.yml --diff

cocalc:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook cocalc.yml --diff

monitor:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook monitoring.yml --diff

spidergalaxy:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook spidergalaxy.yml --diff --extra-vars "__galaxy_dir_perms='0755' os_env_umask='022'"

all:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook infra.yml --diff
