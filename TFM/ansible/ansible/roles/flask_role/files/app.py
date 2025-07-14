from flask import Flask, request, jsonify

app = Flask(__name__)
VALID_TOKEN = "YWRtaW4="

@app.route('/')
def index():
    return "CTF Token Validator Service"

@app.route('/validate', methods=['GET'])
def validate():
    token = request.args.get('token')
    if token == VALID_TOKEN:
        return jsonify({
            "user": "cn=admin,dc=ctf,dc=local",
            "ldap_base": "dc=ctf,dc=local",
            "next_hint": "Search for uid=david"
        })
    else:
        return jsonify({"error": "Invalid token"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
