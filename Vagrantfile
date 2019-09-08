# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # first step
  config.vm.box = "bento/ubuntu-18.04"

  config.vm.box_check_update = true

  config.vm.provider "parallels" do |prl|
    prl.name = "vagrant_pcidss_log"
    prl.check_guest_tools = false
    prl.memory = 2048
    prl.cpus = 2
  end

  config.vm.provider "vmware_fusion" do |vmware|
    vmware.gui = false
    vmware.vmx["memsize"] = 2048
    vmware.vmx["numvcpus"] = 2
  end

  config.vm.provider "virtualbox" do |v, override|
    # http://askubuntu.com/questions/238040/how-do-i-fix-name-service-for-vagrant-client
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--memory", 2048]
    v.cpus = 2
  end

  # config.vm.synced_folder ".", "/vagrant"
  config.ssh.insert_key = false

  config.vm.define "app_vagrant1" do |vagrant1|
    vagrant1.vm.box = "bento/ubuntu-18.04"
    # vagrant1.vm.network "forwarded_port", guest: 80, host: 9080
    # vagrant1.vm.network "forwarded_port", guest: 443, host: 9443
  end

  config.vm.define "db_vagrant2" do |vagrant2|
    vagrant2.vm.box = "bento/ubuntu-18.04"
    # vagrant2.vm.network "forwarded_port", guest: 80, host: 9080
    # vagrant2.vm.network "forwarded_port", guest: 443, host: 9443
  end

  config.vm.define "lb_vagrant3" do |vagrant3|
    vagrant3.vm.box = "bento/ubuntu-18.04"
    # vagrant3.vm.network "forwarded_port", guest: 80, host: 9080
    # vagrant3.vm.network "forwarded_port", guest: 443, host: 9443
  end

  config.vm.define "vagrant4" do |vagrant4|
    vagrant4.vm.box = "bento/ubuntu-18.04"
    # vagrant3.vm.network "forwarded_port", guest: 80, host: 9080
    # vagrant3.vm.network "forwarded_port", guest: 443, host: 9443
  end

  config.vm.define "app_vagrant5" do |vagrant5|
    vagrant5.vm.box = "bento/ubuntu-18.04"
    # vagrant1.vm.network "forwarded_port", guest: 80, host: 9080
    # vagrant1.vm.network "forwarded_port", guest: 443, host: 9443
  end
end
