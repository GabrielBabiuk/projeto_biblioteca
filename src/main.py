from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando banco de dados em memória
equipamentos = [
    {"id": 1, "nome": "Microscópio", "disponivel": True},
    {"id": 2, "nome": "Notebook Dell", "disponivel": True},
    {"id": 3, "nome": "Kit Arduino", "disponivel": True}
]

emprestimos = []

@app.route("/equipamentos", methods=["GET"])
def listar_equipamentos():
    return jsonify(equipamentos)

@app.route("/emprestar/<int:equip_id>", methods=["POST"])
def emprestar_equipamento(equip_id):
    for eq in equipamentos:
        if eq["id"] == equip_id:
            if eq["disponivel"]:
                eq["disponivel"] = False
                emprestimos.append({"equipamento": eq["nome"]})
                return jsonify({"mensagem": f"{eq['nome']} emprestado com sucesso."})
            else:
                return jsonify({"erro": "Equipamento indisponível."}), 400
    return jsonify({"erro": "Equipamento não encontrado."}), 404

@app.route("/devolver/<int:equip_id>", methods=["POST"])
def devolver_equipamento(equip_id):
    for eq in equipamentos:
        if eq["id"] == equip_id:
            eq["disponivel"] = True
            return jsonify({"mensagem": f"{eq['nome']} devolvido com sucesso."})
    return jsonify({"erro": "Equipamento não encontrado."}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)