from wtforms import Form, StringField, TextAreaField


class NewPaper(Form):
    title = StringField('Название')
    text = TextAreaField('Текст')
    tags = StringField('Теги через пробел')
