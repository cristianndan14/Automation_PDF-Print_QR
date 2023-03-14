from .entities.button import Button

import pymysql

class ButtonModel():

    @classmethod
    def button_list(cls, db, id_lot):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT code, passcode, qr_image
                FROM button WHERE id_lot = '{0}'""".format(id_lot)
            cursor.execute(sql)
            data = cursor.fetchall()
            buttons = []
            for row in data:
                b = Button(None, row[0], row[1], row[2], None)
                buttons.append(b)
            return buttons
        except Exception as ex:
            raise Exception(ex)

        finally:
            cursor.close()