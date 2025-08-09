from flask import Flask, request, jsonify, abort, make_response
import subprocess

app = Flask(__name__)

# Token válido en base64 (corresponde a 'admin')
VALID_TOKEN = "YWRtaW4="

# Nombre de dominio esperado
ALLOWED_HOST = "www.ctf.local"

# Lista de tokens autorizados (simulación de sesión)
authorized_tokens = set()

@app.before_request
def enforce_hostname():
    host = request.host.split(':')[0]
    if host != ALLOWED_HOST:
        abort(403)


@app.errorhandler(403)
def forbidden(e):
    return make_response(
        "Forbidden - Did you forget to set the correct Host header?", 403
    )

@app.route('/robots.txt')
def robots():
    return "Disallow: /\n# Host: www.ctf.local\n"

@app.route('/')
def index():
    return "CTF Token Validator Service, access /validate"

@app.route('/validate', methods=['GET'])
def validate():
    token = request.args.get('token')
    if token == VALID_TOKEN:
        authorized_tokens.add(token)
        return jsonify({
            "user": "cn=admin,dc=ctf,dc=local",
            "ldap_base": "dc=ctf,dc=local",
            "next_hint": "Now access /ldapquery?token=...&cmd=...",
            "status": "Token accepted"
        })
    else:
        return jsonify({"error": "Invalid token"}), 403

@app.route('/ldapquery', methods=['GET'])
def ldapquery():
    token = request.args.get('token')
    cmd = request.args.get('cmd')

    if token not in authorized_tokens:
        return jsonify({"error": "Unauthorized: invalid or missing token"}), 403

    if not cmd:
        return jsonify({"error": "Missing command parameter"}), 400

    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=5)
        return "<pre>" + output.decode() + "</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Command failed:\n{e.output.decode()}</pre>", 500
    except Exception as e:
        return f"<pre>Execution error: {str(e)}</pre>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
