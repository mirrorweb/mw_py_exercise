from quart import Quart, render_template
from webapp.controller import mod_app

from db import connection

app = Quart(__name__)


@app.before_serving
async def create_db_conn():
    print("Starting app")
    app.sac = await connection()


@app.after_serving
async def close_db_conn():
    print("Closing down app")
    await app.sac.close()


app.register_blueprint(mod_app)
