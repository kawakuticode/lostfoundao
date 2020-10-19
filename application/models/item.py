from application.application_factory import database
from application.application_factory import ma


class Item(database.Model):
    __tablename__ = 'items'
    # __table_args__ = {'extend_existing': True}
    id = database.Column(database.INTEGER, primary_key=True)
    fname = database.Column(database.TEXT)
    lname = database.Column(database.TEXT)
    type_item = database.Column(database.TEXT)
    reference = database.Column(database.TEXT)
    status = database.Column(database.TEXT)
    province = database.Column(database.TEXT)
    email = database.Column(database.TEXT)
    cellphone = database.Column(database.TEXT)
    note = database.Column(database.TEXT)


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instace = True
