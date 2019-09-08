#!/usr/bin/env python3
import subprocess
import sys
import json
import argparse
import paramiko
import shlex
import io
import re
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Vagrant inventory script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host', action='store')
    return parser.parse_args()

def list_running_hosts():
    cmd = "vagrant status --machine-readable"
    status = subprocess.check_output(cmd.split()).decode()
    hosts = defaultdict(dict)
    hosts['vagrant']['hosts'] = []
    hosts['vagrant']['vars'] = {
        'ansible_ssh_user': 'vagrant',
        'ansible_ssh_private_key_file': '~/.vagrant.d/insecure_private_key',
    }

    for line in status.split('\n'):
        if len(line.split(',')) == 4:
            (_, host, key, value) = line.split(',')[:4]
            if key == 'state' and value == 'running':
                hosts['vagrant']['hosts'].append(host)

    groups = []
    for host in hosts['vagrant']['hosts']:
        g = re.split(r'_', host, 1)
        if len(g) > 1:
            groups.append(g[0])
            if hosts[g[0]]:
                hosts[g[0]]['hosts'].append(host)
            else:
                hosts[g[0]]['hosts'] = [ host ]
    hosts['vagrant']['children'] = list(set(groups))


    hosts['_meta']['hostvars'] = defaultdict(dict)
    for host in hosts['vagrant']['hosts']:
        host_details = get_host_details(host)
        hosts['_meta']['hostvars'][host]['ansible_port'] = host_details['ansible_port']
        hosts['_meta']['hostvars'][host]['ansible_host'] = host_details['ansible_host']
    return(hosts)

def get_host_details(host):
    cmd = "vagrant ssh-config {}".format(host)
    p = subprocess.run(shlex.split(cmd), capture_output=True)
    config = paramiko.SSHConfig()
    config.parse(io.StringIO(p.stdout.decode()))
    c = config.lookup(host)
    return {'ansible_host': c['hostname'],
            'ansible_port': c['port'],
            'ansible_user': c['user'],
            'ansible_private_key_file': '~/.vagrant.d/insecure_private_key',
            }

def main():
    args = parse_args()
    if args.list:
        hosts = list_running_hosts()
        json.dump(hosts, sys.stdout)
    else:
        details = get_host_details(args.host)
        json.dump(details, sys.stderr)

if __name__ == "__main__":
    main()