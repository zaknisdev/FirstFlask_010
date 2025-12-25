from flask import Flask, render_template, request  
app = Flask(__name__)                              

@app.route('/', methods=['GET', 'POST'])
def index():
    pesan_hasil = ""
    if request.method == 'POST':
        try:
            angka = int(request.form['input_angka'])
            
            if angka % 2 == 0:
                pesan_hasil = f"Angka {angka} adalah GENAP."
            else:
                pesan_hasil = f"Angka {angka} adalah GANJIL."
        except:
            pesan_hasil = "Input harus angka bulat!"

    return render_template('index.html', hasil=pesan_hasil)

if __name__ == '__main__':
    app.run(debug=True)