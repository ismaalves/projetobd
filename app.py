from flask import Flask, render_template

app = Flask(__name__)

class Filme:
    def __init__(self, nome, ano, desc, img) -> None:
        self.nome = nome
        self.ano = ano
        self.desc = desc
        self.img = img

f1 = Filme("Pantera Negra: Wakanda Para Sempre", 2022, "Apos a morte do rei TChalla, Shuri, Okoye, Nakia e Ramonda \
     enfrentam os acontecimentos seguintes do trono de Wakanda. Alem de ter que manter a diplomacia com outros paises,\
     Wakanda tera que manter boas relacoes com Talokan, um reino subaquatico, e seu rei Namor.",
     "https://claudia.abril.com.br/wp-content/uploads/2022/11/pantera-negra-2-marvel-critica.jpg")

f2 = Filme("Pantera Negra: Wakanda Para Sempre", 2022, "Apos a morte do rei TChalla, Shuri, Okoye, Nakia e Ramonda \
     enfrentam os acontecimentos seguintes do trono de Wakanda. Alem de ter que manter a diplomacia com outros paises,\
     Wakanda tera que manter boas relacoes com Talokan, um reino subaquatico, e seu rei Namor.",
     "https://claudia.abril.com.br/wp-content/uploads/2022/11/pantera-negra-2-marvel-critica.jpg")

f3 = Filme("Pantera Negra: Wakanda Para Sempre", 2022, "Apos a morte do rei TChalla, Shuri, Okoye, Nakia e Ramonda \
     enfrentam os acontecimentos seguintes do trono de Wakanda. Alem de ter que manter a diplomacia com outros paises,\
     Wakanda tera que manter boas relacoes com Talokan, um reino subaquatico, e seu rei Namor.",
     "https://claudia.abril.com.br/wp-content/uploads/2022/11/pantera-negra-2-marvel-critica.jpg")

filmes = [f1,f2,f3,f1,f2]

@app.route("/")
def hello_world():
    return render_template("index.html", filmes=filmes)

if __name__ == '__main__':
    app.run(debug=True)