'''
from flask import Flask, render_template, redirect, url_for, request
from flask import make_response
# import search
import gensim
from gensim.models import Word2Vec

app = Flask(__name__)
model = gensim.models.Word2Vec.load("category_model.model")


@app.route("/")
def home():
    return "python test"


# @app.route("/index")

@app.route('/respon', methods=['GET', 'POST'])
def login():
    temp = request.args.get('what', 'none')
    return temp


# message = None
# if request.method == 'POST':
#      datafromjs = request.form['mydata']
#      result = "return this"
#      resp = make_response('{"response": '+result+'}')
#      resp.headers['Content-Type'] = "application/json"
#      return resp
#      return render_template('login.html', message='')
@app.route('/run', methods=['GET', 'POST'])
def run():
    # temp = request.args.get('what', 'none')
    # return render_template('loging.html')
    return render_template('ani_.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    # temp = request.args.get('what', 'none')
    if request.method == 'POST':
        result = request.form
        print(result['Word'])
        # res = search_category(result['Word'])
        # result['Word'] = res
        return render_template("result.html", result=result)
    # return render_template('result.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    temp = request.args.get('what', 'none')
    res = search_category(temp)
    # str = ''
    # for i in range(len(res)):
    #   str = str + res[i]
    return res  # str(res[0][0]) + str(res[0][1])


def search_category(word):
    try:
        return model.wv.most_similar(word)
    except:
        return ''


if __name__ == "__main__":
    app.run(debug=True)
'''

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/run')
def run():
    return render_template('search.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    # temp = request.args.get('what', 'none')
    #if request.method == 'POST':
        # result = request.form
        # print(result['Word'])
        # res = search_category(result['Word'])
        # result['Word'] = res
        return render_template("result.html", result=result)
    # return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)