#!/bin/bash

newip=`/usr/bin/curl -s http://169.254.169.254/latest/meta-data/public-ipv4`

/bin/sed -ri "s/pasv_address\=([0-9]{1,3}\.){3}[0-9]{1,3}/pasv_address=$newip/" /etc/vsftpd.conf

/etc/init.d/vsftpd restart
