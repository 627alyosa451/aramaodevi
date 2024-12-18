import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Kırtasiye malzemelerini ve resim dosyalarını tanımlayan bir sözlük
data = {
    "kalem": "static/images/kalem.jpg",
    "silgi": "static/images/silgi.jpg",
    "defter": "static/images/defter.jpg",
    "cetvel": "static/images/cetvel.jpg",
    "makas": "static/images/makas.jpg",
    "yapıştırıcı": "static/images/yapistirici.jpg",
    "zımbalık": "static/images/zimbalık.jpg",
    "klasör": "static/images/klasor.jpg",
    "kalemtıraş": "static/images/kalemtiras.jpg",
    "boya": "static/images/boya.jpg"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query").lower()
    image_path = data.get(query, None)
    if image_path:
        return render_template("result.html", item=query, image=image_path)
    else:
        return render_template("result.html", item=None, image=None)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()