from odoo import fields , models

class student(models.model):
    _name = "school.student"
    log_access = False

    name = fields.Char(string='Name' ,  require=True)
    age = fields.Integer(string="Age" , require=True)
    Id = fields.Integer(string='Id' ,  require=True)
    grade = fields.Char(string='Niveux' , require=True)


class Teacher(models.model):
    _name = "school.teacher"
    log_access = False

    name = fields.Char(string='Name', require=True)
    Id = fields.Integer(string='Id', require=True)
    module = fields.Char(string='Mdl' , require=True)
    phone = fields.Integer(string='numP' , require=True)


