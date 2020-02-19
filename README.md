Ansible Role - Users
=========

An ansible role to manage users on RHEL/Centos and Debian/Ubuntu servers

Requirements
------------

Ansible version 2.6 or later

Role Variables
--------------

Available variables are listed below. See [`defaults/main.yml`](./defaults/main.yml) for more details and example

    passwordless_sudo_all: false
    create_users: []

`passwordless_sudo_all`: Add passwordless sudo for all sudo/wheel user
`create_users`: A list of users to manage(create/delete/modify)

See [user module](https://docs.ansible.com/ansible/2.8/modules/user_module.html) for all the options related to user creation
See [authorized key module](https://docs.ansible.com/ansible/2.8/modules/authorized_key_module.html) for all the options related to `authorized_keys` section

The following options for individual users are not part of the above modules
`sudo_user`: whether to add this user to sudo/wheel group. Default: false
`passwordless_sudo`: whether to enable passwordless sudo for this user. Default: false
   
You can use all the options provided in [user modules](https://docs.ansible.com/ansible/latest/modules/user_module.html)
as individual user options

Dependencies
------------

None

Example Playbook
----------------

Use the following playbook to create a sudo/wheel user named `deployer` with passwordless sudo
and authorization key located at `/home/local/.ssh/id_rsa.pub`

    - hosts: servers
      become: true
      roles:
        - role: sakibmoon.users
      vars:
        users_list:
          - name: deployer
            state: present
            sudo_user: true
            passwordless_sudo: true
            authorized_keys:
              key: /home/local/.ssh/id_rsa.pub
           
Use the following plabook to remove a user named `alice`

    - hosts: servers
      become: true
      roles:
        - role: sakibmoon.users
      vars:
        users_list:
          - name: alice
            state: absent
        

License
-------

MIT

Author Information
------------------

This role was created by sakibmoon in 2020.
