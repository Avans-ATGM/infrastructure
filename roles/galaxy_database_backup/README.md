######################
# Borg backup system #
######################


This role works together with add the student directories, student projects.
In each home directory of a project is a directory called data-storage

All files will be encrypted and stored on a differnt machine
This can be configured in the hostvars

to install add role and run the galaxy_database_backup_init.sh script underroot 

example:
backup_host: cocalc.atgm.avans.nl
manual_database_backup: /data/galaxy_database_backup
backup_max_size: 1000
backups_to_keep: 10


which telles. at which machine the directorie and where is.



# how to retrieve a backup

#perform from the machine the backup is created and fill int the following to make life easy

```
Borg_backup@midgard:/home/artemis$ export BORG_RSH="ssh -i //home/(backup user)/.ssh/id_rsa"
Borg_backup@midgard:/home/artemis$ export BORG_PASSPHRASE=(staat in secret file)
#data is findable in hostvars under the machine it i used
Borg_backup@midgard:/home/artemis$ export BORG_REPO=(borg user)@(machine):(path)
```
##### for tips on how to fill in. check the script in /bin/usr/

# find all current backups
borg list
#this command will produce a list, use the first column for the next command to retrieve the backup 
#this command will exstract the backup in the directry you are in
borg extract $BORG_REPO::project-2022-2022MBI_04-2022-05-14T12-00-26

# for archive

sshfs to the the backup directory /home/gringott/backup archive_mounpoint
borg list archive mountpont
#### select your favourite backup
borg exstract archive_mountpoint::backupname