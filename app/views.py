from generate import create_qr
from flask import render_template, flash, redirect, url_for, request, make_response
from app import app
from forms import QRCodeForm
@app.route('/qr_code_generator', methods = ["GET", "POST"])
def form():
    form = QRCodeForm()
    if form.validate_on_submit():
        # This should be done with ajax
        flash("Cool, get you that STL in just a sec...")
        stl = create_qr(str(form.qr_text.data), bool(form.in_or_out.data), int(form.border_size.data),
                float(form.length_width.data), float(form.height.data), float(form.base_percentage.data)
                )
        response = make_response(stl)
        response.headers["Content-Disposition"] = "attachment; filename=qr_code.stl"
        return response

    return render_template("qr_code_generator.html", title = "QR Code Form", form = form)
