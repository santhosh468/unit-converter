from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/length', methods=['GET', 'POST'])
def length():
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot"]
    result = None
    input_value = ''
    from_unit = units[0]
    to_unit = units[0]
    if request.method == "POST":
        try:
            input_value = request.form['value']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            value = float(input_value)
            result = value * length_conversion_factor(from_unit, to_unit)
        except ValueError:
            return render_template("convert_template.html", title="Length", units=units, error="Invalid input", theme_class="length-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)
    return render_template("convert_template.html", title="Length", units=units, result=result, theme_class="length-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    units = ["Gram", "Kilogram", "Pound", "Ounce"]
    result = None
    input_value = ''
    from_unit = units[0]
    to_unit = units[0]
    if request.method == "POST":
        try:
            input_value = request.form['value']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            value = float(input_value)
            result = value * weight_conversion_factor(from_unit, to_unit)
        except ValueError:
            return render_template("convert_template.html", title="Weight", units=units, error="Invalid input", theme_class="weight-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)
    return render_template("convert_template.html", title="Weight", units=units, result=result, theme_class="weight-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    result = None
    input_value = ''
    from_unit = units[0]
    to_unit = units[0]
    if request.method == "POST":
        try:
            input_value = request.form['value']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            value = float(input_value)
            result = temperature_conversion(value, from_unit, to_unit)
        except ValueError:
            return render_template("convert_template.html", title="Temperature", units=units, error="Invalid input", theme_class="temp-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)
    return render_template("convert_template.html", title="Temperature", units=units, result=result, theme_class="temp-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)

@app.route('/area', methods=['GET', 'POST'])
def area():
    units = ["Square Meter", "Square Kilometer", "Hectare", "Acre", "Square Foot", "Square Inch", "Square Yard", "Square Mile", "Square Centimeter"]
    result = None
    input_value = ''
    from_unit = units[0]
    to_unit = units[0]
    if request.method == "POST":
        try:
            input_value = request.form['value']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            value = float(input_value)
            result = value * area_conversion_factor(from_unit, to_unit)
        except ValueError:
            return render_template("convert_template.html", title="Area", units=units, error="Invalid input", theme_class="area-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)
    return render_template("convert_template.html", title="Area", units=units, result=result, theme_class="area-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)

@app.route('/volume', methods=['GET', 'POST'])
def volume():
    units = ["Liter", "Milliliter", "Cubic Meter", "Cubic Centimeter", "Gallon", "Fluid Ounce", "Cubic Inch", "Cubic Foot"]
    result = None
    input_value = ''
    from_unit = units[0]
    to_unit = units[0]
    if request.method == "POST":
        try:
            input_value = request.form['value']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            value = float(input_value)
            result = value * volume_conversion_factor(from_unit, to_unit)
        except ValueError:
            return render_template("convert_template.html", title="Volume", units=units, error="Invalid input", theme_class="volume-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)
    return render_template("convert_template.html", title="Volume", units=units, result=result, theme_class="volume-theme", input_value=input_value, from_unit=from_unit, to_unit=to_unit)

def length_conversion_factor(from_unit, to_unit):
    factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048
    }
    return factors[from_unit] / factors[to_unit]

def weight_conversion_factor(from_unit, to_unit):
    factors = {
        "Gram": 1,
        "Kilogram": 1000,
        "Pound": 453.592,
        "Ounce": 28.3495
    }
    return factors[from_unit] / factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Unsupported from_unit")
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Unsupported to_unit")

def area_conversion_factor(from_unit, to_unit):
    factors = {
        "Square Meter": 1,
        "Square Kilometer": 1e6,
        "Hectare": 1e4,
        "Acre": 4046.86,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
        "Square Yard": 0.836127,
        "Square Mile": 2.59e6,
        "Square Centimeter": 0.0001
    }
    return factors[from_unit] / factors[to_unit]

def volume_conversion_factor(from_unit, to_unit):
    factors = {
        "Liter": 1,
        "Milliliter": 0.001,
        "Cubic Meter": 1000,
        "Cubic Centimeter": 0.001,
        "Gallon": 3.78541,
        "Fluid Ounce": 0.0295735,
        "Cubic Inch": 0.0163871,
        "Cubic Foot": 28.3168
    }
    return factors[from_unit] / factors[to_unit]

if __name__ == '__main__':
    app.run(debug=True)
