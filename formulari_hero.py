from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def formulari():
    if request.method == 'POST':
        tipus = request.form['tipus']
        nom = request.form['nom']
        atac = request.form['atac']
        defensa = request.form['defensa']
        moviment = request.form['moviment']
        cos = request.form['cos']
        ment = request.form['ment']
        habilitats = request.form['habilitats']

        #  Aqui retorna la pagina html amb el resultat
        return render_template("retorno_hero.html", tipus=tipo, nom=nombre, atac=ataque, 
                               defensa=defensa, moviment=movimiento, cos=cuerpo, 
                               ment=mente, habilitats=habilidades)
    # Aqui et dona la pagina html amb el formulari
    return render_template("formulari.html")

if __name__ == '__main__':
    app.run(debug=True)