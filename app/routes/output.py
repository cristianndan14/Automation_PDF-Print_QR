from flask import render_template, request, redirect, url_for

from ..models.LotModel import LotModel
from ..models.ButtonModel import ButtonModel


def init_output(app, db):

    @app.route('/button_form', methods=['GET', 'POST'])
    def button_form():
        try:
            lots = LotModel.lot_list(db)
            data = {
                'title': 'Lot list',
                'lots': lots
            }
            if request.method == 'POST':
                id_lot = request.form['Lot']

                lot_buttons = ButtonModel.button_list(db, id_lot)

                data_b = {
                    'title': 'Lot of buttons',
                    'lot_buttons': lot_buttons
                }
                return render_template('button.html', data_b=data_b)

            return render_template('button_form.html', data=data)

        except Exception as ex:
            return ex
