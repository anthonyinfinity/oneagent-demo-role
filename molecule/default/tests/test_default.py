import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dt_user(host):
    os = host.system_info.distribution
    if os == 'redhat':
        user = host.user('dtuser')
        assert user.exists
        assert user.shell == '/sbin/nologin'
        assert user.home == '/var/cache/dtuser'
        assert user.group == 'dtuser'


def test_oneagent_running_and_enabled(host):
    oneagent = host.service("oneagent")
    assert oneagent.is_running
    assert oneagent.is_enabled


def test_oneagent_listening_port_one(host):
    socket = host.socket('tcp://127.0.0.1:50000')
    assert socket.is_listening


def test_oneagent_listening_port_three(host):
    socket = host.socket('tcp://127.0.0.1:50001')
    assert socket.is_listening


def test_oneagent_listening_port_four(host):
    socket = host.socket('tcp://127.0.0.1:50002')
    assert socket.is_listening


def test_oneagent_listening_port_five(host):
    socket = host.socket('tcp://127.0.0.1:50003')
    assert socket.is_listening
