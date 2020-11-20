#!/bin/bash
# set dates for backup rotation
NOWDATE=`date +%Y-%m-%d`

# set backup directory variables
SRCDIR='/tmp/s3backups'
DESTDIR='/data/'
BUCKET='mysql-backups'

# database access details
HOST='127.0.0.1'
PORT='3306'
USER='root'
PASS='12345678' #change it to your real password

#### END CONFIGURATION ####

# make the temp directory if it doesn't exist
mkdir -p $SRCDIR

# repair, optimize, and dump each database to its own sql file
for DB in $(mysql -h$HOST -P$PORT -u$USER -p$PASS -BNe 'show databases' | grep -Ev 'mysql|information_schema|performance_schema|sys')
do
        mysqldump -h$HOST -P$PORT -u$USER -p$PASS --quote-names --create-options --force $DB > $SRCDIR/$DB.sql
        mysqlcheck -h$HOST -P$PORT -u$USER -p$PASS --auto-repair --optimize $DB
done

# tar all the databases into $NOWDATE-backups.tar.gz
cd $SRCDIR
tar -czPf $NOWDATE-backup.tar.gz *.sql

# upload backup to s3
# before you upload your backups to s3,you need aws config first 
# aws config
# input your aws S3 endpoint、your aws access id and accesskey
aws s3 cp  $SRCDIR/$NOWDATE-backup.tar.gz s3://$BUCKET/$DESTDIR/

# delete old backups from s3
#aws s3 rm s3://$BUCKET/$DESTDIR/$LASTDATE-backup.tar.gz
#if you wanna to delete old backups from s3,I suggest that set S3 Buckets Lifecycle to delete your old backups