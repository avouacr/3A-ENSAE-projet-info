from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, SelectField, FieldList, FormField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app_source.models import User


class LoginForm(FlaskForm):
    """Form object to enable user login."""
    username = StringField("Adresse électronique", validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Connexion')


class RegistrationForm(FlaskForm):
    """Form object to enable user registration."""
    username = StringField('Adresse électronique', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField(
        'Répéter le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Valider")

    def validate_username(self, username):
        """Check if a user is already registered in the database."""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Cette adresse électronique a déjà été utilisée.')


class SpokenLanguagesSubform(FlaskForm):

    class Meta:
        csrf = False

    with open('data/languages_list.txt', 'r') as f:
        languages = f.read().splitlines()[:-1]
    languages = sorted(languages)
    language_choices = list(zip(languages, languages))
    language = SelectField('Langue', choices=language_choices)
    levels = ['Débutant', 'Intermédiaire', 'Avancé', 'Langue maternelle']
    level_choices = list(zip(levels, levels))
    level = SelectField('Niveau', choices=level_choices)


class GeneralInfoForm(FlaskForm):
    """Form object to store general informations about the user."""
    first_name = StringField('Prénom', validators=[DataRequired()])
    last_name = StringField('Nom', validators=[DataRequired()])
    phone_number = StringField('Numéro de téléphone', validators=[DataRequired()])
    city = StringField('Ville de résidence', validators=[DataRequired()])
    mobility = SelectField('Mobilité',
    	choices=[
    	('city', 'Ville'), 
    	('dpt', 'Département'), 
    	('region', 'Région'),
    	('ntn', 'France entière')
    	])
    languages = FieldList(FormField(SpokenLanguagesSubform),
                          min_entries=1, max_entries=10)
    add_language = SubmitField('Ajouter une langue')
    description = TextAreaField("""Présentez-vous en quelques phrases 
    (qui êtes-vous? que recherchez-vous?)""",
                                render_kw={"rows": 5, "cols": 50})
    submit = SubmitField('Valider et continuer')


class DriverLicensesSubform(FlaskForm):

    class Meta:
        csrf = False

    with open('data/french_driver_licenses.txt', 'r') as f:
        licenses = f.read().splitlines()[:-1]
    licenses = sorted(licenses)
    license_choices = list(zip(licenses, licenses))
    driver_license = SelectField('Permis', choices=license_choices)


class OtherCertificationsSubform(FlaskForm):

    class Meta:
        csrf = False

    other_certif = StringField('Autre certification')


class CertificationsForm(FlaskForm):

    driver_licenses = FieldList(FormField(DriverLicensesSubform),
                                min_entries=0, max_entries=10)
    add_license = SubmitField('Ajouter un permis')
    other_certifications = FieldList(FormField(OtherCertificationsSubform),
                                     min_entries=0, max_entries=10)
    add_other_certif = SubmitField('Ajouter une certification')
    submit = SubmitField('Valider et continuer')


class FormationExpererienceSubform(FlaskForm):

    class Meta:
        csrf = False

    date_start = DateField('Date de début', format='%Y-%m-%d')
    date_end = DateField('Date de fin', format='%Y-%m-%d')
    title = StringField('Titre')
    institution = StringField('Établissement')
    desc = TextAreaField('Description', render_kw={"rows": 5, "cols": 50})


class FormationForm(FlaskForm):

    formation_entries = FieldList(FormField(FormationExpererienceSubform),
                                  min_entries=0, max_entries=10)
    add_formation = SubmitField('Ajouter une formation')
    submit = SubmitField('Valider et continuer')


class ExperienceForm(FlaskForm):

    experience_entries = FieldList(FormField(FormationExpererienceSubform),
                                   min_entries=0, max_entries=10)
    add_experience = SubmitField('Ajouter une expérience')
    submit = SubmitField('Valider et continuer')
