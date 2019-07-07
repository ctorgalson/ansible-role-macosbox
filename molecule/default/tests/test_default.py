import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('user,path,file,mode', [
    ('molecule', '.ssh', '', 0o700,),
    ('molecule', '.ssh', 'id_rsa', 0o600,),
    ('molecule', '.ssh', 'id_rsa.pub', 0o644,),
    ('molecule', '.ssh', 'authorized_keys', 0o600,),
])
def test_files_and_directories(host, user, path, file, mode):
    f = host.file('/home/{}/{}/{}'.format(user, path, file))

    if file:
        is_type = 'is_file'
    else:
        is_type = 'is_directory'

    assert f.exists
    assert getattr(f, is_type)
    assert f.user == user
    assert f.group == user
    assert f.mode == mode
