import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('minimalflaskpandas.default_settings')
app.config.from_envvar('MINIMALFLASKPANDAS_SETTINGS', silent=True)
app.config.from_envvar('settings.cfg', silent=True)

import minimalflaskpandas.views
