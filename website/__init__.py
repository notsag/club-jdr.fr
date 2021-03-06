from flask import Flask
from datetime import timedelta
from flask_discord import DiscordOAuth2Session
from flask_wtf.csrf import CSRFProtect
import os
import locale

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_AUTH_SECRET")
app.config["DISCORD_CLIENT_ID"] = os.environ.get("DISCORD_CLIENT_ID")
app.config["DISCORD_CLIENT_SECRET"] = os.environ.get("DISCORD_CLIENT_SECRET")
app.config["DISCORD_BOT_TOKEN"] = os.environ.get("DISCORD_BOT_TOKEN")
app.config["DISCORD_REDIRECT_URI"] = os.environ.get("DISCORD_REDIRECT_URI")
app.config["GUILD_NAME"] = "Club JDR"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=10)

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

if "https" not in app.config["DISCORD_REDIRECT_URI"]:
    # OAuth2 must make use of HTTPS in production environment.
    os.environ[
        "OAUTHLIB_INSECURE_TRANSPORT"
    ] = "true"  # !! Only in development environment.

discord = DiscordOAuth2Session(app)

csrf = CSRFProtect()
csrf.init_app(app)

from website import models
from website import views
