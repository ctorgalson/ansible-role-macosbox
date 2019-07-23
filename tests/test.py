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
    file = host.file("/Users/travis/{}".format(path))

    with host.sudo():
        assert file.user == "travis"
        assert file.group == "staff"
        assert file.mode == mode
        assert getattr(file, type)


def test_authorized_keys_contents(host):
    dest = host.file("/Users/travis/.ssh/authorized_keys")
    source = host.file("./tests/files/keys/id_rsa.pub")

    with host.sudo():
        assert source.content_string in dest.content_string


""" ctorgalson.macos_hostname tests """

@pytest.mark.parametrize("property,value", [
    ("ComputerName", "macOS Box Travis"),
    ("LocalHostName", "MacOsBoxTravis"),
])
def test_hostname(host, property, value):
    output = host.check_output("scutil --get {}".format(property))

    assert output == value


""" ctorgalson.files tests """

@pytest.mark.parametrize("path", [
    "/Users/travis/Dev",
    "/Users/travis/Dev/travis",
])
def test_directory_structure(host, path):
    dir = host.file(path)

    assert dir.user == "travis"
    assert dir.group == "staff"
    assert dir.is_directory


""" ctorgalson.dotfiles tests """

@pytest.mark.parametrize("dotfile,type", [
    (".vim", "directory"),
    (".vimrc", "file"),
    (".zshrc", "file"),
])
def test_dotfiles(host, dotfile, type):
    home = "/Users/travis/{}"
    config = "/Users/travis/.ansible-managed-config/dotfiles/{}"
    dir = host.file(config.format(""))
    file = host.file(config.format(dotfile))
    link = host.file(home.format(dotfile))
    is_type = "is_{}".format(type)

    assert dir.is_directory
    assert getattr(file, is_type)
    assert link.is_symlink


""" elliotweiser.osx-command-line-tools tests """



