Ansible Role - Users
=========

An ansible role to manage users on RHEL/Centos and Debian/Ubuntu servers

Requirements
------------
Ansible version 2.6 or later

Role Variables
--------------

Available variables are listed below. See [Example Playbooks](#example-playbooks) and [`defaults/main.yml`](./defaults/main.yml) for more details and example

    passwordless_sudo_all: false
    create_users: []

`passwordless_sudo_all`: Add passwordless sudo for all sudo/wheel user  
`create_users`: A list of users to manage(create/delete/modify)

`create_users` contains following options

| Parameter Name | Parameter Type | Default Value | Description |
|----------------|----------------|---------------|-------------|
| `name`         | string <br> (Required) |       | Name of the user to create, remove or modify. |
| `append`       | boolean <br> `no` <br> `yes` | `no` | If `yes`, add the user to the groups specified in groups.<br>If `no`, user will only be added to the groups specified in groups, removing them from all other groups. |
| `comment`      | string         |               | Optionally sets the description (aka GECOS) of user account. |
| `create_home`  | boolean <br> `no` <br> `yes` | `yes` | Unless set to no, a home directory will be made for the user when the account is created or if the home directory does not exist. |
| `force`        | boolean <br> `no` <br> `yes` | `no` | This only affects `state=absent`, it forces removal of the user and associated directories on supported platforms.<br>The behavior is the same as `userdel --force`, check the man page for userdel on your system for details and support.<br>When used with `generate_ssh_key=yes` this forces an existing key to be overwritten. |
| `generate_ssh_key` | boolean <br> `no` <br> `yes` | `no` | Whether to generate a SSH key for the user in question. <br>This will not overwrite an existing SSH key unless used with `force=yes`. |
| `group`        | string         |               | Optionally sets the user's primary group (takes a group name). |
| `groups`       | list           |               | List of groups user will be added to. When set to an empty string '', the user is removed from all groups except the primary group. |
| `home`         | path           |               | Optionally set the user's home directory. |
| `move_home`    | boolean <br> `no` <br> `yes` | `no` | If set to `yes` when used with `home:` , attempt to move the user's old home directory to the specified directory if it isn't there already and the old home exists. |
| `non_unique`   | boolean <br> `no` <br> `yes` | `no` | Optionally when used with the -u option, this option allows to change the user ID to a non-unique value. |
| `password`     | string         |               | Optionally set the user's password to this crypted value. <br> To create a disabled account on Linux systems, set this to '!' or '\*'. <br>See https://docs.ansible.com/ansible/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module for details on various ways to generate these password values. |
| `password_lock` | boolean <br> `no` <br> `yes` |     | Lock the password (usermod -L, pw lock, usermod -C). <br>BUT implementation differs on different platforms, this option does not always mean the user cannot login via other methods. <br> This option does not disable the user, only lock the password. Do not change the password in the same task. |
| `passwordless_sudo` | boolean <br> `no` <br> `yes` | `no` | Enable passwordless sudo for this user only. `sudo_user` must be set to `yes` |
| `remove`       | boolean <br> `no` <br> `yes` | `no` | This only affects `state=absent`, it attempts to remove directories associated with the user. <br>The behavior is the same as `userdel --remove`, check the man page for details and support. 
| `seuser`       | string         |               | Optionally sets the seuser type (`user_u`) on selinux enabled systems. |
| `shell`        | string         |               | Optionally set the user's shell. <br>The default shell is determined by the underlying tool being used. |
| `skeleton`     | string         |               | Optionally set a home skeleton directory. <br>Requires `create_home` option!
| `ssh_key_bits` | integer        | "default set by ssh-keygen" | Optionally specify number of bits in SSH key to create. |
| `ssh_key_comment` | string      | "ansible-generated on $HOSTNAME" | Optionally define the comment for the SSH key. |
| `ssh_key_file` | path           | `.ssh/id_rsa` | Optionally specify the SSH key filename. <br>If this is a relative filename then it will be relative to the user's home directory. <br>If `generate_ssh_key` is set, This parameter defaults to `.ssh/id_rsa`. |
| `ssh_key_type` | string         | "rsa"         | Optionally specify the type of SSH key to generate. <br>Available SSH key types will depend on implementation present on target host. |
| `state`        | string <br> `absent` <br> `present` | `present` | Whether the account should exist or not, taking action if the state is different from what is stated. |
| `sudo_user`    | boolean <br> `no` <br> `yes` | `no` | Add the user to `sudo`/`wheel` group |
| `system`       | boolean <br> `no` <br> `yes` | `no` | When creating an account `state=present`, setting this to yes makes the user a system account. <br>This setting cannot be changed on existing users. <br>This does not work as intended. It creates user home directory which should not exists for system user and the uid is not set under 1000 if not explicitly set by `uid` |
| `uid`          | integer        |               | Optionally sets the UID of the user. |
| `update_password` | string <br> `always` <br> `on_create` | `always` | `always` will update passwords if they differ. <br>`on_create` will only set the password for newly created users. |
| `authorized_key` | dictionary   |               | Optionally adds or removes an SSH authorized key. |
| `authorized_key`.`key` | string <br> Required  |     | The SSH public key(s), as a string or url |
| `authorized_key`.`comment` | string |           | Change the comment on the public key. <br>Rewriting the comment is useful in cases such as fetching it from GitHub or GitLab. <br>If no comment is specified, the existing comment will be kept. |
| `authorized_key`.`exclusive` | boolean <br> `no` <br> `yes` | `no` | Whether to remove all other non-specified keys from the `authorized_keys` file. Multiple keys can be specified in a single key string value by separating them by newlines. |
| `authorized_key`.`exclusive` | boolean <br> `no` <br> `yes` | `no` | Follow path symlink instead of replacing it. |
| `authorized_key`.`key_options` | string   |    | A string of ssh key options to be prepended to the key in the `authorized_keys` file. |
| `authorized_key`.`manage_dir` | boolean <br> `no` <br> `yes` | `yes` | Whether this module should manage the directory of the authorized key file. If set to `yes`, the module will create the directory, as well as set the owner and permissions of an existing directory. Be sure to set `manage_dir=no` if you are using an alternate directory for `authorized_keys`, as set with path, since you could lock yourself out of SSH access. |
| `authorized_key`.`path` | path   |    | Alternate path to the authorized_keys file. When unset, this value defaults to `~/.ssh/authorized_keys`. |
| `authorized_key`.`state` | string <br> `absent` <br> `present` | `present` | Whether the given key (with the given key_options) should or should not be in the file. |
| `authorized_key`.`validate_certs` | boolean <br> `no` <br> `yes` | `yes` | This only applies if using a https url as the source of the keys. <br>If set to `no`, the SSL certificates will not be validated. <br>This should only set to no used on personally controlled sites using self-signed certificates as it avoids verifying the source site. |


Dependencies
------------

None

Example Playbooks
----------------

Use the following playbook to create a sudo/wheel user named `deployer` with passwordless sudo
and authorization key located at `/home/local/.ssh/id_rsa.pub`

``` yaml
- hosts: servers
  become: true
  roles:
    - role: sakibmoon.users
  vars:
    users_list:
      - name: deployer
        state: present
        sudo_user: yes
        passwordless_sudo: yes
        authorized_keys:
          key: /home/local/.ssh/id_rsa.pub
```
           
Use the following plabook to remove a user named `alice`

``` yaml
- hosts: servers
  become: true
  roles:
    - role: sakibmoon.users
  vars:
    users_list:
      - name: alice
        state: absent
```

Create `user1` and add the user to only `group1` and `group2`(append: false). Add `user2` and set `group2` as his primary group. 

``` yaml
- hosts: servers
  become: true
  roles:
    - role: sakibmoon.users
  vars:
    users_list:
      - name: user1
        state: present
        groups:
          - group1
          - group2
        append: no
      - name: user2
        state: present
        group: group2 
```

License
-------

MIT

Author Information
------------------

This role was created by sakibmoon in 2020.
