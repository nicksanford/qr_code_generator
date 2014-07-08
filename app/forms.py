from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required

class QRCodeForm(Form):
    qr_text =           TextField("qr_text", validators = [Required()])
    in_or_out =         SelectField("in_or_out", choices=[("out","out"),("in","in")], default = "out")
    border_size =       TextField("border_size", default = "2", validators = [Required()])
    length_width =      TextField("length_width", default = "40", validators = [Required()])
    height =            TextField("height", default = ".02", validators = [Required()])
    base_percentage =   TextField("base_percentage", default = "2.0", validators = [Required()])

