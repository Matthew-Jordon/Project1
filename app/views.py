"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from pathlib import Path
from app import app
from flask import render_template, request, redirect, url_for, flash, send_from_directory

from app.models import Property, db
from .forms import Create
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def newproperty():
    forms = Create()

    if forms.validate_on_submit(): 
        f = request.files.get('pic', False)
        pic=secure_filename(f.filename)
        if f:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] , secure_filename(f.filename)))
    
        property = Property(request.form['title'], 
        request.form['beds'], 
        request.form['baths'],
        request.form['type'], 
        request.form['location'], 
        request.form['price'], 
        request.form['description'],
        pic)

        db.session.add(property)
        db.session.commit()
        

        flash('Property added', 'success')
        return redirect(url_for('home'))
    else:
        flash('Unsupported file type','danger') 
    return render_template('create.html', form = forms)

@app.route('/properties')
def view_properties():
    properties=db.session.query(Property).all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def show_property(propertyid):
    property = db.session.query(Property).filter(Property.id == propertyid).first()
    return render_template('property.html', property = property)

@app.route('/uploads/<filename>')
def get_images(filename):
    root = os.getcwd()
    return send_from_directory(root+'/'+app.config['UPLOAD_FOLDER'], filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
