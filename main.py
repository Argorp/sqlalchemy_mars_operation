from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime as dt

app = Flask(__name__)
app.config['key'] = 'special_key'

jobs, users = [], []

def main():
    global jobs, users_names
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    cur_job = Jobs(
        team_leader = 4,
        job="process a vaccination",
        work_size=40,
        collaborators="1, 2, 3, 5",
        start_date = dt.date.today(),
        is_finished=False
    )
    db_sess.add(cur_job)
    db_sess.commit()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    users_names = {user.id: f"{user.name} {user.surname}" for user in users}
    app.run(host='127.0.0.1', port=8080)


@app.route('/')
def jobs_log():
    return render_template(
        'jobs_log.html',
        title='Текущие задачи',
        jobs=jobs,
        users=users_names
    )


if __name__ == "__main__":
    main()