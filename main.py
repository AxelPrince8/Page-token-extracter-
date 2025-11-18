from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
  <title>FB Page Token Extractor</title>
</head>
<body>
  <h2>Facebook Page Token Extractor</h2>
  <form method="post">
    User Access Token: <input type="text" name="user_token" style="width:400px;" required>
    <input type="submit" value="Extract Page Tokens">
  </form>
  {% if results %}
    <h3>Page Tokens:</h3>
    <ul>
      {% for page in results %}
        <li><strong>{{page['name']}}</strong> (ID: {{page['id']}}) : {{page['access_token']}}</li>
      {% endfor %}
    </ul>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_token = request.form["user_token"]
        url = f"https://graph.facebook.com/v20.0/me/accounts?fields=id,name,access_token&access_token={user_token}"
        resp = requests.get(url)
        data = resp.json()
        results = data.get('data', [])
        return render_template_string(HTML_FORM, results=results)
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
