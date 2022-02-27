from flask import Flask,request,render_template
from flask import jsonify

from scraper import  get_channelinfo, get_search_results


app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('my-form.html')


@app.route('/',methods=['POST'])
# def look_up():
#     # results = get_comments(videoid)
#     channelid=request.form.get("channelid")
#     results = get_channelinfo(channelid)
#     return jsonify(results)
    
def look_up():
    # results = get_comments(videoid)
    keyword=str(request.form.get("channelid"))
    titles,thumbnails = get_search_results(keyword)
    
    return render_template('results.html', title='Results', dat=titles, data=thumbnails, search=keyword)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    