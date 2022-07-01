from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, RadioField, FloatField
from wtforms.validators import DataRequired, NumberRange


class FightForm(FlaskForm):
    player_hp = FloatField('Your hp',
        validators=[NumberRange(min=0)],
        render_kw = {
            'class': "form-control"
        })
    enemy_hp = FloatField('Enemy hp',
        validators=[NumberRange(min=0)],
        render_kw = {
            'class': "form-control"
        })
    # your_points = IntegerField('Your points',
    #     render_kw = {
    #         'class': "form-control"
    #     })
    # enemy_points = IntegerField('Enemy points',
    #     render_kw = {
    #         'class': "form-control"
    #     })
    attack_target = RadioField(
        'What enemy part u wanna attack?',
        default='head',
        choices=[
            ('head','head'),
            ('body','body'),
            ('hands','hands'),
            ('legs','legs'),
        ],
        render_kw = {
            'class': 'attack-target'
        }
    )
    attack_button = SubmitField(
        'Hit',
        render_kw = {
            'class':"btn btn-danger"
        }
    )
    player = SelectField(
        'Player',
        choices=[
            ('Knight','Knight'),
            ('Magician','Magician'),
            ('Archer','Archer'),
        ],
        render_kw = {
            'class': 'form-select player-select'
        }
    )
    # fight_button = SubmitField(
    #     'Fight',
    #     render_kw = {
    #         'class':"btn btn-danger"
    #     }
    # )
