import urllib
import webbrowser

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/LFDB.db'
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Item(db.Model):
    __tablename__ = 'item'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.INTEGER, primary_key=True)
    fname = db.Column(db.TEXT)
    lname = db.Column(db.TEXT)
    type_item = db.Column(db.TEXT)
    reference = db.Column(db.TEXT)
    status = db.Column(db.TEXT)
    province = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    cellphone = db.Column(db.TEXT)
    note = db.Column(db.TEXT)


# Global_variables
item_l = Item.query.filter_by(status='Perdido').all()
item_f = Item.query.filter_by(status='Encontrado').all()
type_doc = Item.query.filter(Item.type_item != 'Outros').all()
type_other = Item.query.filter_by(type_item='Outros').all()


# build_message
def build_message(email, subject, message):
    url = 'mailto:' + email + '?'
    params = {'subject': subject, 'body': message}
    link = urllib.parse.urlencode(params)
    url_final = url + link
    return url_final


def valid_parameters(param):
    result = False
    if param != '':
        result = True
    return result


@app.route('/')
def hello_world():
    return render_template("index.html", lost=item_l, found=item_f, docs=type_doc, others=type_other)


@app.route('/home')
def home():
    return render_template("index.html", lost=item_l, found=item_f, docs=type_doc, others=type_other)


@app.route('/about')
def about():
    return render_template("about.html", lost=item_l, found=item_f, docs=type_doc, others=type_other)


@app.route('/lost')
def lost():
    result = Item.query.filter_by(status='Perdido').all()
    return render_template("lost.html", items_perdidos=result)


@app.route('/found')
def found():
    result = Item.query.filter_by(status='Encontrado').all()
    return render_template("found.html", items_encontrados=result)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    me = 'kawakuticode@gmail.com'
    return render_template("contact.html", email=me)


@app.route('/contactown', methods=['POST', 'GET'])
def contactowner():
    if request.method == 'POST':
        email = request.form['email_to']
        return render_template("contact_owner.html", email=email)


@app.route('/sendmessage', methods=['POST'])
def sendcontent():
    if request.method == 'POST':
        email = request.form['email_to']
        subject = request.form['subject']
        message = request.form['message']
        _content = build_message(email, subject, message)
        message = "Mensagem enviada com Sucesso. Aguarde contacto"
        webbrowser.open(_content)
        return render_template("sucess.html", message=message, lost=item_l, found=item_f, docs=type_doc,
                               others=type_other)
    else:
        error = "Nao foi possivel enviar a mensagem "
        return render_template("404.html", message=error)


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/submitform', methods=['POST'])
def submit():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        type_doc = request.form['type_of_doc']
        reference = request.form['reference']
        province = request.form['province']
        status = request.form['status']
        email = request.form['email']
        cellphone = request.form['telefone']
        notes = request.form['message']
        item = Item(fname=fname, lname=lname, type_item=type_doc, reference=reference, province=province,
                    status=status, email=email,
                    cellphone=cellphone, note=notes)
        db.session.add(item)
        db.session.commit()

        if (item.id):
            message = "adicionado a nossa base de dados com sucesso"
            return render_template("sucess.html", message=message, lost=item_l, found=item_f, docs=type_doc,
                                   others=type_other)
        else:
            return render_template("404.html")


@app.route('/search', methods=["POST"])
def search():
    if request.method == 'POST':
        province = request.form['province']
        type_doc = request.form['type_of_doc']
        reference = request.form['reference']

        # if valid_parameters(type_doc):
        if valid_parameters(reference) is False and valid_parameters(province) is False:
            query_by_ref = Item.query.filter(Item.type_item == str(type_doc)).all()
            print("type of document : {} -> reference : {} -> province : {} ".format(type_doc, reference, province))
            return render_template("search.html", items_search=query_by_ref, lost=item_l, found=item_f, docs=type_doc,
                                   others=type_other)
        if valid_parameters(reference) and valid_parameters(province):
            query_by_ref = Item.query.filter(Item.type_item == str(type_doc), Item.reference == str(reference),
                                             Item.province == str(province)).all()
            print("type of document : {} -> reference : {} -> province : {} ".format(type_doc, reference, province))
            return render_template("search.html", items_search=query_by_ref, lost=item_l, found=item_f, docs=type_doc,
                                   others=type_other)
        if valid_parameters(reference) is False and valid_parameters(province):
            query_by_ref = Item.query.filter(Item.type_item == str(type_doc), Item.province == str(province)).all()
            print("type of document : {} -> reference : {} -> province : {} ".format(type_doc, reference, province))
            return render_template("search.html", items_search=query_by_ref, lost=item_l, found=item_f, docs=type_doc,
                                   others=type_other)
        if valid_parameters(reference) and valid_parameters(province) is False:
            query_by_ref = Item.query.filter(Item.type_item == str(type_doc),
                                             Item.reference == str(reference)).all()
            print("type of document : {} -> reference : {} -> province : {} ".format(type_doc, reference, province))
            return render_template("search.html", items_search=query_by_ref, lost=item_l, found=item_f, docs=type_doc,
                                   others=type_other)


if __name__ == '__main__':
    app.run()
