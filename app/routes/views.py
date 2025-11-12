from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        property_type = request.form.get('property_type')
        price_range = request.form.get('price_range')
        print(f"Search Query: {location}, {property_type}, {price_range}")
        # You can pass this into a listings page or filter logic

    return render_template('index.html')