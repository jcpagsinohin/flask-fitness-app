from app import create_app

app = create_app()
debug = app.config['DEBUG']


if __name__ == "__main__":
    app.run(debug=debug)
