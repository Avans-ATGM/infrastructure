# ATGM Infrastructure in Ansible

These playbooks manage our machines and define what software needs to be setup and ensures everything stays updated.

## Setup

After you've cloned the repository, you'll need to install Ansible

```bash
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

You'll need to get the `.vault_password` file from Helena, which is used to decrypt the secrets.

## Running the playbook

```
make
```

## Infrastructure

Service     | Infrastructure Provider | Notes
---         | ---                     | ---
7kingdoms   | BML                     | Deprecated
OldGalaxy   | BML                     | Galaxy head node
Midgard     | BML                     | Deprecated
Asgard      | BML                     | Deprecated
145.48.6.40 | DIF                     | Galaxy Test Server, we deploy here simultaneously (or use it really for testing if we like.)
145.48.6.41 | DIF                     | Galaxy Production Server
145.48.6.42 | DIF                     | Cocalc
