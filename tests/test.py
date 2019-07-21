import os

import pytest

import testinfra.utils.ansible_runner


""" ctorgalson.ssh_keys tests """

@pytest.mark.parametrize("path,mode,file", [
    (".ssh", 0o700, False),
    (".ssh/id_rsa", 0o600, True),
    (".ssh/id_rsa.pub", 0o644, True),
    (".ssh/authorized_keys", 0o600, True),
])
def test_ssh_dir_and_keys(host, path, mode, file):
    type = "is_file" if file else "is_directory"
    file = host.file("/Users/macosbox/{}".format(path))

    with host.sudo():
        assert file.user == "macosbox"
        assert file.group == "staff"
        assert file.mode == mode
        assert getattr(file, type)


def test_authorized_keys_contents(host):
    dest = host.file("/Users/macosbox/.ssh/authorized_keys")
    source = host.file("./tests/files/keys/id_rsa.pub")

    with host.sudo():
        assert source.content_string in dest.content_string


""" ctorgalson.macos_hostname tests """


