# vagrant-discovery

Vagrant dynamic inventory script for Ansible.

## installation

tested with only python3.

```
python3 -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Useful for testing. You should use you own Vagrantfile, but you can use my file as example:

Every host split into own group by hostname rule:

`<group>_<host>`

All groups join into common group: vagrant
