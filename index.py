import pickle

import pandas as pd
from flask import Flask, render_template, request

# molezinha, só tem que setar as pastas de template e assets
app = Flask(__name__, template_folder='template', static_folder='template/assets')

# Treina lá, usa cá
modelo_pipeline = pickle.load(open('./models/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/dados_cliente')
def dados_cliente():
    return render_template("form.html")

# Orden colunas na rede
# 	idade	renda	propriedadeCasa	tempoEmpregado	intensaoInvestimento valorInvestimento	taxaJuros	retornoInvestimento	tempoInvestimento

def get_data():
    idade = request.form.get('idade')
    renda = request.form.get('renda')
    propriedadeCasa = request.form.get('propriedadeCasa')
    tempoEmpregado = request.form.get('tempoEmpregado')
    intensaoInvestimento = request.form.get('intensaoInvestimento')
    valorInvestimento = request.form.get('valorInvestimento')
    taxaJuros = request.form.get('taxaJuros')
    retornoInvestimento = request.form.get('retornoInvestimento')
    tempoInvestimento = request.form.get('tempoInvestimento')


    d_dict = {'idade': [idade], 'renda': [renda], 'propriedadeCasa': [propriedadeCasa],
              'tempoEmpregado': [tempoEmpregado], 'intensaoInvestimento': [intensaoInvestimento],
              'valorInvestimento': [valorInvestimento], 'taxaJuros': [taxaJuros], 
              'retornoInvestimento': [retornoInvestimento], 'tempoInvestimento': [tempoInvestimento]}

    return pd.DataFrame.from_dict(d_dict, orient='columns')



@app.route('/send', methods=['POST'])
def show_data():
    df = get_data()
    df = df[['idade', 'renda', 'propriedadeCasa', 'tempoEmpregado', 'intensaoInvestimento',
       'valorInvestimento', 'taxaJuros', 'retornoInvestimento', 'tempoInvestimento']]


    prediction = modelo_pipeline.predict(df)[0]  # Acessa o primeiro elemento da previsão
    
    if prediction == 0:
        outcome = 'Conservador-0'
        imagem = 'Conservador.png'
    elif prediction == 1:
        outcome = 'Conservador-1'
        imagem = 'Conservador.png'
    elif prediction == 2:
        outcome = 'Moderado-2'
        imagem = 'Moderado.png'
    elif prediction == 3:
        outcome = 'Moderado-3'
        imagem = 'Moderado.png'
    elif prediction == 4:
        outcome = 'Conservador-4'
        imagem = 'conservador.png'
    elif prediction == 5:
        outcome = 'Conservador-5'
        imagem = 'conservador.png'
    elif prediction == 6:
        outcome = 'Conservador-6'
        imagem = 'conservador.png'
    elif prediction == 7:
        outcome = 'Conservador-7'
        imagem = 'conservador.png'

    return render_template('result.html', tables=[df.to_html(classes='data', header=True, col_space=10)], 
                           result=outcome, imagem=imagem)


if __name__ == '__main__':
    app.run(debug=True)






    # prediction = modelo_pipeline.predict(df) 
    #variavel prediction recebe o modelo treinado, fazendo predicao no df com dados recebidos do form.

#     if prediction == 0:
#         outcome = 'Conservador-0'
#         imagem = 'Conservador.png'

#     if prediction == 1:
#         outcome = 'Conservador-1'
#         imagem = 'Conservador.png'

#     if prediction == 2:
#         outcome = 'Moderado-2'
#         imagem = 'Moderado.png'

#     if prediction == 3:
#         outcome = 'Moderado-3'
#         imagem = 'Moderado.png'

#     if prediction == 4:
#         outcome = 'Conservador-4'
#         imagem = 'conservador.png'

#     if prediction == 5:
#         outcome = 'Conservador-5'
#         imagem = 'conservador.png'

#     if prediction == 6:
#         outcome = 'Conservador-6'
#         imagem = 'conservador.png'

#     if prediction == 7:
#         outcome = 'Conservador-7'
#         imagem = 'conservador.png'



#     return render_template('result.html', tables=[df.to_html(classes='data', header=True, col_space=10)], 
#                            result=outcome, imagem=imagem)


# if __name__ == "__main__":
#     app.run(debug=True)
