from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine

app = Flask('pokemon')

engine = create_engine('postgresql://localhost/pokemon')

@app.route('/pokemons/types')
def types():
    return jsonify(types=[
        ['Bug', 69],
        ['Dragon', 32],
        ['Fighting', 27],
        ['Psychic', 57],
        ['Steel', 27],
        ['Ice', 24],
        ['Rock', 44],
        ['Fire', 52],
        ['Grass', 70],
        ['Ground', 32],
        ['Electric', 44],
        ['Dark', 31],
        ['Flying', 4],
        ['Normal', 98],
        ['Ghost', 32],
        ['Water', 112],
        ['Poison', 28],
        ['Fairy', 17],
    ])

@app.route('/')
def index():
    return render_template('index.html')


app.run()
