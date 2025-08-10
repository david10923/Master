
# 🛡️ CTF Hacking Ético - TFM Máster Ciberseguridad

Este proyecto forma parte del Trabajo de Fin de Máster en Ciberseguridad, centrado en el diseño, despliegue y resolución de un entorno **Capture The Flag (CTF)** vulnerable, con fines **formativos y de evaluación técnica** en el ámbito del hacking ético y la auditoría de sistemas.

El entorno incluye la configuración automatizada de múltiples servicios vulnerables (DNS, LDAP, FTP, SSH, aplicación web en Flask), permitiendo al usuario realizar un ciclo completo de pentesting: reconocimiento, explotación, post-explotación y escalada de privilegios.

---

## 🎯 Objetivos del proyecto

- Diseñar un entorno realista tipo CTF replicando servicios comunes en entornos corporativos.
- Introducir vulnerabilidades intencionadas para su posterior identificación y explotación.
- Automatizar el despliegue mediante herramientas de **infraestructura como código**.
- Documentar la resolución completa del CTF como ejercicio práctico de hacking ético.
- Servir como laboratorio formativo para estudiantes, docentes y entusiastas de la seguridad.

---

## 🧰 Tecnologías utilizadas

- [Vagrant](https://www.vagrantup.com/) – Automatiza el despliegue de las máquinas virtuales.
- [Ansible](https://www.ansible.com/) – Configura los servicios de forma repetible y escalable.
- [VirtualBox](https://www.virtualbox.org/) – Hipervisor de virtualización.
- [Ubuntu 22.04 LTS](https://ubuntu.com/download/desktop) – Sistema base para las VMs.
- [OpenLDAP](https://www.openldap.org/) – Servicio de directorio vulnerable.
- [BIND9](https://bind9.readthedocs.io/) – Servidor DNS mal configurado.
- [Flask](https://flask.palletsprojects.com/) – Aplicación web con vulnerabilidades.
- [vsftpd](https://security.appspot.com/vsftpd.html) – Servidor FTP con acceso anónimo.
- [Nmap](https://nmap.org/) – Herramienta de escaneo y enumeración.
- [John The Ripper](https://www.openwall.com/john/) – Herramienta para crackeo de contraseñas.

---

## 🧱 Estructura del entorno CTF

```
CTF Environment
├── Máquina CTF (192.168.1.86)
│   ├── DNS (BIND9)
│   ├── LDAP (OpenLDAP)
│   ├── SSH (OpenSSH)
│   ├── FTP (vsftpd)
│   └── Web App (Flask)
│
└── Máquina atacante (192.168.1.87)
    └── Kali Linux (herramientas de pentesting)
```

---

## 🚀 Instalación y despliegue

> ⚠️ Requisitos previos:  
> - VirtualBox instalado  
> - Vagrant instalado (versión 2.2+ recomendada)  
> - Git

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/david10923/Master.git
   cd Master/TFM/ansible/ansible
   ```

2. **Despliega las máquinas (CTF y atacante)**:

   Desde cada carpeta donde se encuentra el VagrantFile: 
   ```bash
   vagrant up
   ```

   Esto descargará las cajas de Ubuntu y Kali, instalará Ansible y configurará automáticamente los servicios vulnerables.

3. **Accede a la máquina atacante**:

   Desde cada carpeta donde se encuentra el VagrantFile:
   ```bash
   vagrant ssh
   ```

---

## 🕵️‍♂️ Resolución del CTF

El entorno está diseñado para ser resuelto siguiendo fases estructuradas de un pentest:

1. **Reconocimiento activo** (con `nmap`, `whois`, `dig`)
2. **Explotación de servicios** (FTP anónimo, DNS zone transfer, LDAP injection)
3. **Escalada de privilegios** (mediante uso de `sudo vim`)
4. **Captura de flags** que validan la progresión del reto

Cada servicio incluye al menos una vulnerabilidad explotable, y cada paso está documentado en la [memoria del TFM](./Memoria_TFM.pdf).

---

## 📘 Documentación

- `Memoria_TFM.pdf`: Documento detallado con la explicación del entorno, justificación académica, fases de ataque y medidas de mitigación.
- `playbooks/`, `roles/`: Archivos Ansible con la configuración de cada servicio.
- `Vagrantfile`: Configura las máquinas virtuales y automatiza la instalación.

---

## 🔐 Flags (orientativas)

| Servicio  | Ruta (dentro de la máquina víctima) | Tipo                |
|-----------|--------------------------------------|---------------------|
| FTP       | `/srv/ftp/anonymous_flag.txt`        | Acceso anónimo      |
| DNS       | Tras transferencia de zona           | Flag oculta         |
| Flask     | En `/validate` + `/ldapquery`        | Inyección / bypass  |
| LDAP      | En atributo de usuario `David`       | Enumeración LDAP    |
| SSH       | Escalada con `sudo vim`              | Flag final (root)   |

---

## 🎓 Licencia y uso académico

Este entorno ha sido creado **exclusivamente con fines formativos y educativos** como parte del Trabajo de Fin de Máster. El uso del entorno para propósitos distintos al aprendizaje y práctica de técnicas defensivas debe hacerse bajo responsabilidad y cumpliendo con las normativas legales vigentes.

---

## ✍️ Autor

**David Fernández Alejo**  
Máster en Ciberseguridad · Madrid, 2025  
Tutor: Raimundo Alcázar Quesada

---

> “Todo lo que tenemos que decidir es qué hacer con el tiempo que se nos da.” – *Gandalf*
