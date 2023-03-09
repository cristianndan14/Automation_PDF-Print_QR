from flask import render_template

from ..models.LotModel import LotModel


def init_index(app, db):

    @app.route('/')
    def index():
        try:
            lots = LotModel.lot_list(db)
            data = {
                'title': 'Lot list',
                'lots': lots
            }
            return render_template('home.html', data=data)
        except Exception as ex:
            return ex