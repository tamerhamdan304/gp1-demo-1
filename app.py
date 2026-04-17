from flask import Flask, request, render_template_string

app = Flask(__name__)


HTML_PAGE = """
<!doctype html>
<html>
  <head><title>Addition App</title></head>
  <body style="font-family: Arial; margin: 40px;">
    <h1>Simple Addition Web App</h1>
    <form method="post">
      <label>First number:</label>
      <input type="number" name="a" required><br><br>
      <label>Second number:</label>
      <input type="number" name="b" required><br><br>
      <input type="submit" value="Add">
    </form>
    {% if result is not none %}
      <h2>Result: {{ result }}</h2>
    {% endif %}
  </body>
</html>
"""
 
def add_numbers(a, b):
    return a + b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        result = add_numbers(a, b)
    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)  # nosec
