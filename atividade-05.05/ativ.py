from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Essa é minha primeira aplicação em Flask!'

#Crie uma rota/login no seu projeto flask que carregue uma página HTML(login.html, por exemplo) contendo um formulário com 2 campos de texto: um para o nome do usuário e outro pra senha. 

@app.route('/login')
def login(): return render_template('login.html')

#Crie uma rota/ alunos que renderize uma página HTML(alunos.html, por exemplo) com o nome e a matrícula de alguns alunos em uma tabela. 

@app.route('/alunos')
def alunos(): 
    lista_alunos = [
        {'nome': 'Alice', 'matricula': '12345678'}, 
        {'nome': 'Bruno', 'matricula': '98765432'}
        {'nome': 'Clara', 'matricula': '45678912'}, 
        {'nome': 'Marcos', 'matricula': '7412345678'},
        {'nome': 'Valéria', 'matricula': '85236974'},
    ]
    
    return render_template('alunos.html', alunos=lista_alunos)

#Crie uma rota/arearestrita que recebe um parâmetro (ex: /arearestrita/ 



@app.route('/arearestrita/<int:id')
def arearestrita(id):
    if id == 1:
        return 'cadeado Fechado'
    elif id == 2:
        return 'cadeado Aberto'
    else:
        return "Acesso inválido"
    return render_template('restita.html'), imagem=imagem

#Crie uma rota/operação que recebe 3 parâmetros (ex: /operacao/<tipo>/<op1>/<op2>).

def operacao(tipo, op1, op2):
    if tipo == "sum":
        resultado = op1 + op2
    elif tipo =="sub":
        resultado = op1 - op2
    elif tipo == "mult":
        resultado = op1 * op2
    elif tipo == "div":
        if op2 == 0:
            return "Erro: divisão por zero"
        resultado = op1 / op2
    else:
        return "Tipo de operação inválido" 
    
    return f"Resultado: {resultado}"


@app.route('/somar', defauts={"n1": "0", "n2": "0"})
@app.route('/somar/<int:n1>/<int:n2')
def somar(n1,n2):
    resultado = n1 + n2
    return str(resultado)

@app.route('/soma', defauts={"n1": "0", "n2": "0"})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1,n2):
    resultado = n1 + n2 
    return render_template('somar.html', n1=n1, 
    resultado=resultado)

if __name__ == '__main__': 
    app.run(debug=True)
    