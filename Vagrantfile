# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.provider "virtualbox"
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
     vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
     vb.name = "vm_seolondon"
  end

  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vm.network "forwarded_port", guest: 8000, host: 8080

  #############################################
  # install required softwares

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y postgresql
    sudo apt-get install -y python-pip
    sudo apt-get install -y libpq-dev

    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    sudo apt-get install -y nodejs

  SHELL

  #############################################
  # Setup python virtual environment plus nodejs

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    pip install --user --upgrade pip
    pip install --user --upgrade pew
    if [ ! -d '.local/share/virtualenvs/' ]; then
        echo 'source $(SHELL=/bin/bash ~/.local/bin/pew shell_config)' >> .bashrc
    fi
    mkdir -p .local/share/virtualenvs/
    cd /vagrant/
    pew new -d seolondon -a /vagrant -r /vagrant/requirements.txt
    npm install

  SHELL

  #############################################
  # Database setup

  config.vm.provision "shell", inline: <<-SHELL
    sudo -i -u postgres psql -c "CREATE USER seolondon LOGIN PASSWORD 'seolondon';"
    sudo -i -u postgres psql -c "CREATE DATABASE seolondon;"
    sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE seolondon TO seolondon;"
  SHELL

end
