import os

import pytest

import testinfra.utils.ansible_runner

def test_passwd_file(host):
    d = host.file("/Users/macosbox/.ssh")

    assert d.user == "macosbox"
    assert d.group == "staff"
    assert d.mode == 0o700
