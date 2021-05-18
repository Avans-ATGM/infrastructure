gx:
	bash bin/clean-deps.sh
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook galaxy.yml --diff --extra-vars "__galaxy_dir_perms='0755' os_env_umask='022'"


agoge:
	bash bin/clean-deps.sh
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook agoge.yml --diff

cocalc:
	bash bin/clean-deps.sh
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook cocalc.yml --diff

monitor:
	bash bin/clean-deps.sh
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook monitoring.yml --diff

all:
	bash bin/clean-deps.sh
	ansible-galaxy install -p roles -r requirements.yml
	ansible-playbook infra.yml --diff
