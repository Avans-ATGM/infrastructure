######################
# Borg backup system #
######################


This role works together with add the student directories, student projects.
In each home directory of a project is a directory called data-storage

All files will be encrypted and stored on a differnt machine
This can be configured in the hostvars

example:
backup_host: midgard.bioinformatics-atgm.nl
backup_location: /mnt/TeacherFiles/project_backup
backup_max_size: 1000


This will set on which machine, where and what the max size (gb) of archives is allowed to be (for monitoring)

Further is also required in the groupvars allowed
example:
atgm_projects:
    - name: project-01
      year: "2022"
      host: galaxy.bioinformatics-atgm.nl

which telles. at which machine the directorie and where is.
