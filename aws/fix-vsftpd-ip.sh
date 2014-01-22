#!/bin/bash

# For use with my show-ip.php script, see http://davidsj.co.uk/linux/auto-fixing-passive-ftp-on-aws-instances/
hostname='ip.domain.com'

newip=`/usr/bin/curl -s $hostname`

/bin/sed -ri "s/pasv_address\=([0-9]{1,3}\.){3}[0-9]{1,3}/pasv_address=$newip/" /etc/vsftpd.conf

/etc/init.d/vsftpd restart
