In order to deploy the environment
- Install vagrant
- Run "vagrant up"
- Run "vagrant provision" if the machine is up and you want to deploy ansible on it 
- Run "vagrant ssh" to access to the machine
- Run "vagrant rsync-auto" to rsync folders to vagran machine
- Run "vagrant destroy -f" to destroy the machine 



Ldap commands: 
- ldapsearch -x -s base -b "" -H ldap://ns-server-1 namingContexts // to check the base
- 