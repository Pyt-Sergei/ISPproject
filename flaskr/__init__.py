from . flask_app import app

# registering blueprints
from . import auth
app.register_blueprint(auth.bp)
from . import main
app.register_blueprint(main.bp)
from . import site_auth
app.register_blueprint(site_auth.bp)
from . import site_main
app.register_blueprint(site_main.bp)
