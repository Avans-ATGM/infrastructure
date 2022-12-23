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
Erebor      | BML                     | Filebrowser 
Isengard    | BML                     | Student accounts 
Midgard     | BML                     | Sequencing projects & fast5 will be kept with SNELLIUS basecalling / Student
Asgard      | BML                     | Intern Machine / Teachers
145.48.6.40 | DIF                     | Galaxy Test Server, we deploy here simultaneously (or use it really for testing if we like.)
145.48.6.41 | DIF                     | Galaxy Production Server
145.48.6.42 | DIF                     | Cocalc

## user account policy

discussion to be finialised. 

## backup storage policy


Project accounts of students will get an directory called ```data_storage```.<br>
Everything in this directory will be backed up in other machines.
this directory should contain:
- Input data.
- pipelines (scripts and galaxy workflows).
- remove fast5 files once basecalling protocol is satisfying.

Backup frequency is every friday 20:00 till sunday 20:00.

