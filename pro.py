from flask import Flask, render_template, request, send_from_directory
import sqlite3 as sql


app = Flask(__name__)


@app.route("/")
def healthy():
    return render_template("home2.html")


@app.route("/filecreate", methods=['POST'])
def product_create():
    file_name = request.form['file_name']
    #print(str(file_name))
    from PIL import Image
    import pytesseract
    im = Image.open(file_name)
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text)
    return render_template("asd.html", msg=text)
   # try:
    #    with sql.connect("database.db") as con:
     #       cur = con.cursor()
      #      cur.execute("create table if not exists products (name TEXT, price INT)")
       #     cur.execute("INSERT INTO products (name,price)"
        #                "VALUES (?,?)", (product_name, product_price))
         #   con.commit()
          #  msg = "Record saved successfully"
    #except:
     #   con.rollback()
      #  msg = "Error in inserting record"
    #finally:
     #   con.close()
      #  return render_template("asd.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)