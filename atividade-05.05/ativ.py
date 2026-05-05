from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    nome_usuario = "João Silva"
    
    return render_template('login.html', name=nome_usuario)

if __name__ == '__main__':
    app.run(debug=True)
