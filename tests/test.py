import os

import pytest

import testinfra.utils.ansible_runner

@pytest.mark.parametrize("path,mode,file", [
    (".ssh", 0o700, False),
    (".ssh/id_rsa", 0o600, True),
    (".ssh/id_rsa.pub", 0o644, True),
    (".ssh/authorized_keys", 0o600, True),
])
def test_ssh_dir_and_keys(host, mode, file):
    t = "is_file" if file else "is_directory"
    f = host.file("/Users/macosbox/{}".format(path))

    assert f.user == "macosbox"
    assert f.group == "staff"
    assert f.mode == mode
    assert f.getattr(t)
