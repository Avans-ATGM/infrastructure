gx: roles
	ansible-playbook galaxy.yml --diff --extra-vars "__galaxy_dir_perms='0755' os_env_umask='022'"

all: roles
	ansible-playbook infra.yml

roles: requirements.yml
	ansible-galaxy install -p roles -r requirements.yml
