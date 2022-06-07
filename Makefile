all:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook all.yml --diff

gx:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook galaxy.yml --diff --extra-vars "os_env_umask='022'"

it-test-galaxy:
	./bin/clean-deps.py
	#ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook it-test-galaxy.yml --diff --extra-vars "os_env_umask='022'"

agoge:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook agoge.yml --diff

cocalc:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook cocalc.yml --diff

automation:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook automation.yml --diff

spidergalaxy:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook spidergalaxy.yml --diff --extra-vars "os_env_umask='022'"

pulsar:
	./bin/clean-deps.py
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook pulsar.yml --diff --extra-vars "os_env_umask='022'"
