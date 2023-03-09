from .entities.lot import Lot

import pymysql


class LotModel():

    @classmethod
    def lot_list(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_lot, title, date_created FROM lot"""
            cursor.execute(sql)
            data = cursor.fetchall()
            lots = []
            for row in data:
                lot = Lot(row[0], row[1], row[2])
                lots.append(lot)
            return lots
        except Exception as ex:
            raise Exception(ex)

        finally:
            cursor.close()