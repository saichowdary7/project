from flask import flask

app=Flask(__name__)

@app.route('/')
def Sai():
    return 'welcome visakhapatnam'



    if __name__=='__main__':
        app.run()