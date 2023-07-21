from flask import Flask, render_template

# Declarando las variables
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola 2687386'


@app.route('/paises')
def paises():
    # Listas
    continentes = [
        {
            "nombre": "America",
            "paises": [
                {
                    "nombre": "Colombia",
                    "capital": "Bogota",
                    "moneda": "Cop",
                    "poblacion": "51.522.000",
                    "superficie": "1.142 millones km²"
                },
                {
                    "nombre": "Peru",
                    "capital": "Lima",
                    "moneda": "Soles",
                    "poblacion": "33.722.000",
                    "superficie": "1.285 millones km²"
                },
                {
                    "nombre": "Argentina",
                    "capital": "Buenos aires",
                    "moneda": "Peso aregentino",
                    "poblacion": "45.811.000",
                    "superficie": "2.78 millones km²"
                }
            ]
        },

        {
            "nombre": "Europa",
            "paises": [
                {
                    "nombre": "España",
                    "capital": "Madrid",
                    "moneda": "Euro",
                    "poblacion": "47.422.000",
                    "superficie": "505,990 km²"
                },
                {
                    "nombre": "Italia",
                    "capital": "Roma",
                    "moneda": "Euro",
                    "poblacion": "59.111.000",
                    "superficie": "302,073 km²"
                },
                {
                    "nombre": "Reino unido",
                    "capital": "Londres",
                    "moneda": "Libra Esterlina",
                    "poblacion": "67.333.000",
                    "superficie": "243,610 km²"
                }
            ]
        },
        {
            "nombre": "Asia",
            "paises": [
                {
                    "nombre": "Mongolia",
                    "capital": "Ulán Bator",
                    "moneda": "Tugrik mongol",
                    "poblacion": "3.348.000",
                    "superficie": "1.564 millones km²"
                },
                {
                    "nombre": "China",
                    "capital": "Pekin",
                    "moneda": "Yuan",
                    "poblacion": "1.412.000.000",
                    "superficie": "9.597 millones km²"
                },
                {
                    "nombre": "Tailandia",
                    "capital": "Bangkok",
                    "moneda": "Baht tailandés",
                    "poblacion": "71.600.000",
                    "superficie": "513,120 km²"
                }
            ]
        }
    ]
    
    america = len(continentes[0]["paises"])
    europa = len(continentes[1]["paises"])
    asia = len(continentes[2]["paises"])
    paises_totales = america + europa + asia
    
    print("Paises de américa en total: ",america)
    print("Paises de europa en total: ",europa)
    print("Paises de asia en total: ",asia)
    
    
    user = "Sebastian Rivera"
    return render_template('paises_listas.html',
                           user = user,
                           continentes = continentes,
                           america = america,
                           europa = europa,
                           asia = asia,
                           paises_totales = paises_totales)