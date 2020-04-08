from watchlist import db,app
from watchlist.models import User,Movie
import click

# 自定义命令
@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")


# 向数据库中插入数据
@app.cli.command()
def forge():
    m = [
            {"title": "萨霍", "year": "2019"},
            {"title": "星游记", "year": "2020"},
            {"title": "急速备战", "year": "2019"},
            {"title": "叶问4", "year": "2019"},
            {"title": "三人行", "year": "2016"},
    ]
    for i in m:
        movie = Movie(title=i["title"], year=i["year"])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据完成")


# 自定义指令，生成管理员账号flask admin
@app.cli.command()
@click.option('--username',prompt=True,help='登录的用户名')
@click.option('--password',prompt=True,help='登陆的密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建管理员用户')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('管理员账号更新/创建完成')