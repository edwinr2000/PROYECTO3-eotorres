from flask import Flask
from Controllers.product_controller import product_bp
from Controllers.ingredient_controller import ingredient_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(product_bp)
app.register_blueprint(ingredient_bp)

if __name__ == '__main__':
    app.run(debug=True)
