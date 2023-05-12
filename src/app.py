from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Rambo!!'

@app.route('/country/<year>/<country>', methods=['GET'])
def get_country(year, country):
    if year == '2023' and country == 'CR':
        return 'La cantidad de peliculas es igual a 50'
    else:
        return f'Yera: {year}, country: {country}'
    


def page_not_found(error):
    return '<h1>Pagina no existe</h1>', 404



if __name__  == '__main__':
    app.register_error_handler(404,page_not_found)
    app.run(debug=True)
