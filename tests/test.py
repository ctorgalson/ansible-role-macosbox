import os

import pytest

import testinfra.utils.ansible_runner

@pytest.mark.parametrize("path,mode", [
    (".ssh", 0o700),
    (".ssh/id_rsa", 0o600),
    (".ssh/id_rsa.pub", 0o644),
    (".ssh/authorized_keys", 0o600),
])
def test_ssh_dir_and_keys(host, mode):
    d = host.file("/Users/macosbox/{}".format(path))

    assert d.user == "macosbox"
    assert d.group == "staff"
    assert d.mode == mode
