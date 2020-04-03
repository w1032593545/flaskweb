import os
import sys

from flask import Flask, url_for, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"  # windows平台
else:
    prefix = "sqlite:////"  # Mac，linux
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = prefix + \
    os.path.join(app.root_path, 'data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '1903_dev'
db = SQLAlchemy(app)


# 数据层
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        # 获取表单的数据
        title = request.form.get("title")
        year = request.form.get("year")

        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('index'))
        # 将数据保存到数据库
        movie = Movie(title=title,year=year) #创建记录
        db.session.add(movie)
        db.session.commit()
        flash("创建成功")
        return redirect(url_for("index"))

    movie = Movie.query.all()
    return render_template("index.html", movies=movie)


# 自定义命令
@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help="先删除在创建")
def initdb(drop):
    if drop:
        db.create_all
    db.create_all()
    click.echo("初始化数据库完成")


# 向数据库中插入数据
@app.cli.command()
def forge():
    name = "李白"
    m = [
            {"title": "萨霍", "year": "2019"},
            {"title": "星游记", "year": "2020"},
            {"title": "急速备战", "year": "2019"},
            {"title": "叶问4", "year": "2019"},
            {"title": "三人行", "year": "2016"},
    ]
    user = User(name=name)
    db.session.add(user)
    for i in m:
        movie = Movie(title=i["title"], year=i["year"])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据完成")



# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# 模板上下文处理函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)

