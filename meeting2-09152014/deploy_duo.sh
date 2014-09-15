#!/bin/bash
# Provisioning Duo

#Update repositories
echo "=== Update Repositories ==="
apt-get update

#Installing Pre-Reqs
echo "=== Installing Prerequisites ==="
apt-get install cmake make gcc g++ flex bison libpcap-dev libssl-dev python-dev swig zlib1g-dev

#Downloading Duo Tarball
echo "=== Downloading Duo ==="
wget https://dl.duosecurity.com/duo_unix-latest.tar.gz

#Decompressing Duo Tarball
echo "=== Uncompressing Duo ==="
tar zxf duo_unix-latest.tar.gz

#Build Duo package from Source
echo "=== Building Duo from source ==="
cd duo_unix-1.9.11/
./configure --prefix=/usr && make && make install

#SSH Configuration Changes
echo "=== Optimize sshd for Duo ==="
echo "UseDNS yes" >> /etc/ssh/sshd_config
echo "#Duo Modifications" >> /etc/ssh/sshd_config
echo "PermitTunnel no" >> /etc/ssh/sshd_config
echo "AllowTcpForwarding no" >> /etc/ssh/sshd_config
echo "ForceCommand /usr/sbin/login_duo" >> /etc/ssh/sshd_config
service ssh reload

#Verification Message
echo "=== Verifying that it works ==="
/usr/sbin/login_duo echo 'Congrats, you did it! Now you just need to add host, ikey, or skey in /etc/duo/login_duo.conf'

#login_duo mods needed
echo "=== Opening a text editor for you ==="
vim /etc/duo/login_duo.conf
