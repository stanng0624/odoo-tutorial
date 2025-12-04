from odoo import models, fields

class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World'

    name = fields.Char(string='Name', default='Hello World')
    message = fields.Char(string='Message', readonly=True)

    def action_say_hello(self):
        self.message = f"Hello, {self.name}!"