# from flask import current_app
# from flask_dance.contrib.google import make_google_blueprint, google

# firebase_config = current_app.config['FIREBASE_CONFIG']

# google_blueprint = make_google_blueprint(
#     client_id=firebase_config['web']['client_id'],
#     client_secret=firebase_config['web']['client_secret'],
#     scope=[
#         "https://www.googleapis.com/auth/userinfo.email",
#         "https://www.googleapis.com/auth/userinfo.profile"
#     ]
# )

# current_app.register_blueprint(google_blueprint, url_prefix="/login/google")

# @current_app.route("/login/google")
# def login_google():
#     if not google.authorized:
#         return redirect(url_for("google.login"))
#     resp = google.get("/oauth2/v2/userinfo")
#     assert resp.ok, resp.text
#     email = resp.json()["email"]
#     user = User.query.filter_by(email=email).first()
#     if user is None:
#         user = User(email=email)
#         db.session.add(user)
#         db.session.commit()
#     login_user(user)
#     return redirect(url_for("index"))

# @current_app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("index"))
