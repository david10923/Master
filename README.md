
# 🧠 Máster en Ciberseguridad – IMF x Deloitte

Este repositorio reúne **todas las prácticas, módulos técnicos y el Trabajo de Fin de Máster (TFM)** desarrollados durante el Máster en Ciberseguridad impartido por IMF Smart Education junto con Deloitte. Cada módulo contiene ejercicios prácticos, documentación, scripts y herramientas aplicadas a situaciones reales en el ámbito de la ciberseguridad ofensiva, defensiva y forense.

---

## 📁 Estructura del repositorio

```
Master/
├── M1. Ciberinteligencia/           ← OSINT, análisis de amenazas, técnicas de rastreo
├── M2. Hacking ético/               ← Reconocimiento, explotación, post-explotación
├── M3. Desarrollo seguro/           ← Principios de codificación segura, auditoría de código
├── M4. Tecnologías SIEM/            ← Splunk, ELK, correlación de eventos, análisis de logs
├── M5. Ingeniería inversa/          ← Análisis estático y dinámico de binarios, reversing
├── M6. Seguridad en smartphones/    ← Análisis de apps Android/iOS, ingeniería inversa móvil
├── M7. Análisis forense/            ← Análisis de evidencias, timeline forense, herramientas
└── TFM/                             ← Entorno CTF automatizado + memoria del trabajo final
```

---

## 🎯 Objetivos del repositorio

- Consolidar todos los conocimientos adquiridos a través de prácticas estructuradas.
- Simular escenarios reales de seguridad ofensiva y defensiva.
- Automatizar entornos técnicos utilizando herramientas profesionales.
- Desarrollar habilidades en análisis forense, inteligencia de amenazas y desarrollo seguro.
- Documentar y presentar el Trabajo de Fin de Máster como proyecto integral.

---

## 🧰 Herramientas y tecnologías utilizadas

- **Linux, Ubuntu, Kali, Windows** (entornos híbridos)
- **Ansible**, **Vagrant**, **VirtualBox** – Infraestructura como código
- **Nmap**, **Metasploit**, **Burp Suite**, **John the Ripper**
- **Splunk**, **ELK (Elasticsearch, Logstash, Kibana)** – SIEM
- **Ghidra**, **IDA Free**, **APKTool**, **MobSF** – Ingeniería inversa y móvil
- **Python**, **Bash**, **Jinja2**
- **Wireshark**, **Autopsy**, **Volatility** – Análisis forense
- **Flask**, **OpenLDAP**, **BIND9**, **vsftpd**, etc.

---

## 🏁 Trabajo de Fin de Máster (TFM)

El directorio `TFM/` incluye:

- Un entorno tipo **Capture The Flag (CTF)** con múltiples servicios vulnerables.
- Configuración automatizada con Vagrant y Ansible.
- Máquina atacante basada en Kali Linux y máquina víctima con servicios DNS, LDAP, FTP, Flask, SSH.
- Resolución paso a paso: reconocimiento, explotación, escalada, mitigación.
- Memoria técnica (`Memoria_TFM.pdf`) con justificación académica.

---

## ✅ Requisitos para usar el entorno

- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)
- Git

### Despliegue rápido del entorno CTF

```bash
git clone https://github.com/david10923/Master.git
cd Master/TFM/ansible/ansible
vagrant up         # Despliega el entorno
vagrant ssh        # Accede a la máquina atacante
```

---

## 📚 Licencia y uso

Este contenido ha sido creado con fines **formativos y académicos exclusivamente**. Su uso indebido en sistemas reales sin autorización está **prohibido**. El autor no se responsabiliza por un mal uso.

---

## ✍️ Autor

**David Fernández Alejo**  
Máster en Ciberseguridad · Promoción 2023–2025  
Tutor TFM: Raimundo Alcázar Quesada

---

> “Todo lo que tenemos que decidir es qué hacer con el tiempo que se nos da.” – *Gandalf*
