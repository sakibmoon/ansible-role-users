Ansible Role - Users
=========

An ansible role to manage users on RHEL/Centos and Debian/Ubuntu servers

Requirements
------------

Ansible version 2.6 or greater

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):
    passwordless_sudo_all: false
    create_users: []

`passwordless_sudo_all`: Add passwordless sudo for all sudo/wheel user
`create_users`: A list of users to manage(create/delete/modify)
    
You can use all the options provided in [user modules](https://docs.ansible.com/ansible/latest/modules/user_module.html) as individual user options

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: sakibmoon.users }

License
-------

MIT

Author Information
------------------

This role was created by sakibmoon in 2018.
