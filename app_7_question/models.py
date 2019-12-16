from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Rafael'

doc = """
Encuesta demográfica
"""

class Constants(BaseConstants):
    name_in_url = 'app_7_question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    gender = models.IntegerField(
        label = 'Cúal es su genero?',
        choices = [(0, "Femenino"),
                   (1, "Masculino"),
                   (2,"Otro")],
        widget = widgets.RadioSelectHorizontal
    )

    age = models.IntegerField(
        label = '¿Qué edad tiene?',
        min = 18, max = 70
    )

    country = models.StringField(
        label = "¿Cúal es su país de origen?",
    )

    education = models.IntegerField(
        label = '¿Cúal es su nivel de educación (el grado máximo de estudios finalizados)?',
        choices = [(1, "Sin estudios"),
                   (2, "Primaria (educación básica) "),
                   (3, "Formación técnica/profesional"),
                   (4, "Secundaria (bachillerato)"),
                   (5, "Universitaria (2-5 años)"),
                   (6, "Post-grado (master/doctorado)")]
    )

    civil_status = models.IntegerField(
        label = '¿Cúal es su estado civil?',
        choices = [(1, 'Soltero/a (no se ha casado nunca)'),
                   (2, 'Vive en pareja'),
                   (3, 'Casado/a'),
                   (4, 'Separado/a, divorciado/a'),
                   (5, 'Viudo/a')]
    )

    income = models.IntegerField(
        label= '¿Qué nivel de ingresos anuales brutos tiene su hogar?',
        choices = [
            (1, '0 - 20.000 Euros'),
            (2,'20.001 - 40.000 Euros'),
            (3,'40.001 - 60.000 Euros'),
            (4,'60.001 - 80.000 Euros'),
            (5,'80.001 - 100.000 Euros'),
            (6,'Más de 100.000 Euros')])

    online_frequency = models.IntegerField(
        label = '¿Con qué frecuencia suele acceder a internet',
        choices = [
            (1, 'Continuamente/Cada hora'),
            (2, 'Varias veces al día'),
            (3, 'Una vez al día'),
            (4, 'Varias veces a la semana'),
            (5, 'Una vez a la semana'),
            (6, 'Menos de una vez a la semana')
        ]
    )

    online_purchase = models.IntegerField(
        label = 'Cuando compra productos y servicios relacionados con los viajes (tiquetes de tren / avion, reservas de'
                ' hoteles, paquetes turisticos, etc.) ¿Que tan seguido usa internet para este propósito?',
        choices = [
            (0, 'No'),
            (1, 'Si')
        ]
    )
