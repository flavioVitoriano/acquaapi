import peewee

db = peewee.PostgresqlDatabase('appone', user='appone', password='wearechampions',
                           host='db_acqua', port=5432)


class BaseModel(peewee.Model):
    class Meta:
        database = db
