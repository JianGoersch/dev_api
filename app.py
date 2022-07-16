from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id':'0','Nome':'Goersch', 'Habilidades':['Python','Flask']},
    {'id':1,'Nome':'Jian','Habilidades':['Python', 'Django']}
]

#devolve, altera e deleta um dev pelo id
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT': #método PUT server para atualizar
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'mensagem': 'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET': #lista todos os devs
        return jsonify(desenvolvedores)


if __name__=='__main__':
    app.run()

