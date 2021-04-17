# ansible_basics
First Ansible deployment exemple of MediaWiki serveur

Ansible sample that deploy two servers for installing MediaWiki
- apache serveur with PHP the web site
- MariaDB database for the content

# Requirements
## Ansible
Debian server to install ansible 2.7.10
create user user-ansible

## Apache
Centos 8 server to install apache
create user user-ansible

## MariaDB
Centos 8 server to install MariaDB database
create user user-ansible

# Execution
On ansible server with user user-ansible launch playbooks
ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-apache.yml
ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-mariadb.yml
ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-mediawiki.yml
