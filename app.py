from website import create_app

# entry point to app
if __name__=="__main__":
    app = create_app()
    app.run(debug=True)