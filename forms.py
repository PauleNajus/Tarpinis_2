from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError, Email, EqualTo
from app.models import User
from app import db
import re

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    balance = DecimalField('Balance', validators=[DataRequired(), NumberRange(min=0)])
    is_admin = BooleanField('Is Admin')
    password = PasswordField('Password', render_kw={"placeholder": "Leave empty if not changing"})
    confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Leave empty if not changing"}, validators=[EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_password(self, password):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password.data):
            raise ValidationError('Password must be at least 8 characters long, include letters and numbers.')

    def save_user(self):
        user = User(username=self.username.data, email=self.email.data)
        user.set_password(self.password.data)
        db.session.add(user)
        db.session.commit()
        return user

class BalanceForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0, message="Amount must be positive")])
    submit = SubmitField('Submit')

class CartForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add to Cart')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    description = TextAreaField('Description')
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Add Product')

    def validate_price(form, field):
        if field.data < 0:
            raise ValidationError('Price must be non-negative.')

    def validate_quantity(form, field):
        if field.data < 0:
            raise ValidationError('Quantity must be non-negative.')

class DiscountForm(FlaskForm):
    product_id = SelectField('Product', choices=[], coerce=int, validators=[DataRequired()])
    discount_percentage = FloatField('Discount Percentage', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Set Discount')

    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)
        self.product_id.choices = [(product.id, product.name) for product in Product.query.all()]


class OrderHistoryForm(FlaskForm):
    submit = SubmitField('View Order History')

class PasswordChangeForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

class ChangeEmailForm(FlaskForm):
    old_email = StringField('Old Email', validators=[DataRequired(), Email()])
    new_email = StringField('New Email', validators=[DataRequired(), Email()])
    confirm_new_email = StringField('Confirm New Email', validators=[DataRequired(), Email(), EqualTo('new_email')])
    submit = SubmitField('Change Email')

class ChangeUsernameForm(FlaskForm):
    old_username = StringField('Old Username', validators=[DataRequired()])
    new_username = StringField('New Username', validators=[DataRequired()])
    confirm_new_username = StringField('Confirm New Username', validators=[DataRequired()])
    submit = SubmitField('Change Username')