from flask import Flask, render_template_string, request

app = Flask(__name__)

# ==============================
# HTML incrustado (Bootstrap 5)
# ==============================
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Profesional Flask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #007bff, #6610f2);
            color: #fff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }
        .form-control {
            border-radius: 10px;
        }
        .btn-custom {
            background-color: #fff;
            color: #007bff;
            border-radius: 25px;
            transition: 0.3s;
        }
        .btn-custom:hover {
            background-color: #007bff;
            color: #fff;
        }
        footer {
            position: absolute;
            bottom: 15px;
            width: 100%;
            text-align: center;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card p-5 text-center bg-light text-dark" style="max-width: 500px; margin: auto;">
            <h2 class="mb-4 text-primary">Bienvenido a tu App Flask</h2>
            <form method="POST" action="/">
                <div class="mb-3">
                    <label for="nombre" class="form-label">Ingresa tu nombre</label>
                    <input type="text" class="form-control" id="nombre" name="nombre" placeholder="Ejemplo: Miguel Sosa" required>
                </div>
                <button type="submit" class="btn btn-custom px-4">Enviar</button>
            </form>
            {% if nombre %}
            <div class="alert alert-success mt-4" role="alert">
                ¡Hola, <b>{{ nombre }}</b>! 👋 Bienvenido a tu aplicación profesional Flask.
            </div>
            {% endif %}
        </div>
    </div>
    <footer>
        Desarrollado con ❤️ por Miguel Sosa — Flask & Bootstrap 5
    </footer>
</body>
</html>
"""

# ==============================
# Rutas Flask
# ==============================
@app.route("/", methods=["GET", "POST"])
def home():
    nombre = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
    return render_template_string(HTML, nombre=nombre)

# ==============================
# Ejecución en puerto 80
# ==============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
