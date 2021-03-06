from flask import Flask,request,render_template
from flask import jsonify
import uvicorn
from scraper import  get_channelinfo


app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('my-form.html')


@app.route('/',methods=['POST'])
def look_up():
    # results = get_comments(videoid)
    channelid=request.form.get("channelid")
    results = get_channelinfo(channelid)
    return jsonify(results)

#videoid="3dHJ00mAQAY"
#print(get_comments(videoid))
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=True)
    uvicorn.run(app, port=8080, host='0.0.0.0')
    #app.run()
