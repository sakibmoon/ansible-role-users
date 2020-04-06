import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_newuser(host):
    user = host.user('newuser')
    groups = user.groups

    assert user.exists
    assert user.home == '/home/newuser'
    assert user.uid >= 1000
    assert len(groups) == 3
    assert 'group1' in groups
    assert 'group2' in groups


def test_sudouser(host):
    user = host.user('sudouser')
    groups = user.groups
    visudo_file = host.file('/etc/sudoers.d/sudouser')

    assert user.exists
    assert 'sudo' in groups or 'wheel' in groups
    assert visudo_file.exists
    assert visudo_file.is_file
    assert user.home == '/home/sudouser'


def test_testuser(host):
    user = host.user('testuser')
    groups = user.groups

    assert user.exists
    assert user.home == '/home/testuser'
    assert len(groups) == 1
    assert 'testuser' in groups


def test_appendremoveuser(host):
    user = host.user('appendremoveuser')
    groups = user.groups

    assert len(groups) == 2
    assert 'group1' in groups


def test_priamrygroupuser(host):
    user = host.user('primarygroupuser')

    assert user.group == 'randomgroup'


def test_homeuser(host):
    user = host.user('homeuser')

    assert user.home == '/home/testhome'


def test_sshkeyuser(host):
    keyfile = host.file('/home/sshkeyuser/.ssh/id_rsa')

    assert keyfile.exists
    assert keyfile.is_file


def test_sshkeyfileuser(host):
    keyfile = host.file('/home/sshkeyfileuser/.ssh/customkey')
    homedir = host.file('/home/sshkeyfileuser')

    assert homedir.exists
    assert keyfile.exists
    assert keyfile.is_file


def test_uiduser(host):
    user = host.user('uiduser')

    assert user.uid == 1099


def test_bashshell(host):
    user = host.user('bashuser')

    assert user.shell == '/bin/bash'


def test_dashshell(host):
    user = host.user('dashuser')

    assert user.shell == '/bin/dash'


def test_systemuser(host):
    user = host.user('systemuser')

    user_home = host.file('/home/systemuser/')
    assert not user_home.exists
    assert user.home == '/home/systemuser'
