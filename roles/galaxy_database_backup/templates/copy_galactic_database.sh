rm /data/databases/.galaxy_database.sql.gz
pg_dump galaxy | gzip > /data/databases/.galaxy_database.sql.gz


info $?