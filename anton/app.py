from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-nejy$#gi#$s123"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/")
from forms import DemoForm
def index():
    user_name = "123"
    return render_template("index.j2", user_name=user_name)


@app.route('/test')
def test():
    return render_template("test.j2")


@app.route("/users")
def users():
    page_title = "Список пользователей, кто заполнил форму"
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", page_title=page_title, users=user_list_db)


@app.route("/thanks")
def thanks():
    page_title = "Спасибо за заполнение формы!"
    return render_template("thanks.j2", page_title=page_title)


@app.route("/form", methods=["GET", "POST"])
def demo_form():
    page_title = "Демо-форма"
    form = DemoForm()
    if form.validate_on_submit():
        print(f"Имя кто заполнил: {request.form.get('name')}, \nEmail: {request.form.get('email')}")
        user_db = UserSubmit(
            name=f"{request.form.get('name')} {request.form.get('last_name')}",
            email=request.form.get('email')
        )
        db.session.add(user_db)
        db.session.commit()

        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email)
        return redirect("thanks")
    return render_template("test-form.j2", page_title=page_title, form=form)
