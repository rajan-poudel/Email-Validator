from flask import Flask , render_template ,request
import requests


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if (request.method=='POST'):
        email = request.form.get('username')
        url = """https://api.emailvalidation.io/v1/info?apikey=ema_live_DZSD4gt6BF34G60SlP1lBrLQGa6wt9RDCQo5EwrV&email="""+email
        res = requests.get(url)
        result = res.json()
        dynamic_content = ''
        for key in result.keys():
            value = result[key]
            if isinstance(value, str) and value.strip() != "":
                dynamic_content += f"<div>{key}: {value}</div>"
        return render_template("index.html",dynamic_content=dynamic_content)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)