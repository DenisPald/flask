from wtforms import Form, StringField, TextAreaField


class NewPaper(Form):
    title = StringField('Название')
    text = TextAreaField('Текст')
