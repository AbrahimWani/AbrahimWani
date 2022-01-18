from django.db import models

# country Choice
country_choices = [
    ("India", "India"),
]
# state Choices
state_choices = [
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"),
    ("New Delhi", "New Delhi"),
    ("Puducherry", "Puducherry"),
]
# Role Choices
usertype = [
    ("Patient", "Patient"),
    ("Doctor", "Doctor"),
]
# gender choices
gender_choices = [
    ("Male", "Male"),
    ("Female", "Female"),
]
# agegroup choices
agegroup_choices = [
    ("0-6", "0-6"),
    ("6-10", "6-10"),
    ("10-17", "10-17"),
    ("17-45", "17-45"),
    ("45-60", "45-60"),
]
# language_Choices
language_choices = [
    ("English", "English"),
    ("Hindi", "Hindi"),
    ("Punjabi", "Punjabi"),
    ("Bhojpuri", "Bhojpuri"),
]
# status Choices
status_choices = [
    ("Active", "Active"),
    ("Inactive", "Inactive"),
]


# Language model
class Language_table(models.Model):
    langauge_id = models.AutoField(primary_key=True, editable=False)
    language_name = models.CharField(
        choices=language_choices, max_length=20, default="English"
    )
    status = models.CharField(
        max_length=20, choices=status_choices, blank=True, null=True, default="Inactive"
    )


# Create your models here.
class Admin_table(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_email = models.EmailField(null=True, blank=True, unique=True)
    admin_password = models.CharField(max_length=50)


# user Model
class User_table(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(
        max_length=60, null=True, blank=True, choices=gender_choices
    )
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_no = models.IntegerField(null=True, blank=True)
    country = models.CharField(
        choices=country_choices, max_length=50, null=True, blank=True
    )
    state = models.CharField(
        choices=state_choices, max_length=50, null=True, blank=True
    )
    city = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    expertise = models.TextField(max_length=1200, null=True, blank=True)
    qualification = models.TextField(max_length=1200, null=True, blank=True)
    user_type = models.CharField(choices=usertype, max_length=20, null=True, blank=True)
    user_status = models.CharField(
        max_length=60, choices=status_choices, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=60, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True)


# Consult_model
class Consult_table(models.Model):
    consult_id = models.AutoField(primary_key=True, editable=False)
    patient_id = models.ForeignKey(
        User_table,
        related_name="patientconsult",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    accepted_doctor_id = models.ForeignKey(
        User_table,
        related_name="doctorconsult",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    language_id = models.ForeignKey(
        Language_table, on_delete=models.CASCADE, null=True, blank=True
    )
    patient_first_name = models.CharField(max_length=30, null=True, blank=True)
    patient_last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.IntegerField(null=True, blank=True)
    country = models.CharField(choices=country_choices, max_length=50, default="India")
    state = models.CharField(choices=state_choices, max_length=50, default="false")
    city = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        Admin_table, on_delete=models.CASCADE, null=True, blank=True
    )
    approved_at = models.DateTimeField(auto_now_add=True)
    withdraw_date = models.DateTimeField(auto_now_add=True)
    withdraw_reason = models.TextField(max_length=300, null=True, blank=True)
    preferred_time = models.TimeField(null=True, blank=True)


# chat model
class Chat_table(models.Model):
    chat_id = models.AutoField(primary_key=True, editable=False)
    doctor_id = models.ForeignKey(
        User_table,
        related_name="doctorchat",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    patient_id = models.ForeignKey(
        User_table,
        related_name="patientchat",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    chat_at = models.DateTimeField(auto_now_add=True)


# Age model
class Age_table(models.Model):
    age_id = models.AutoField(primary_key=True, editable=False)
    age_min = models.IntegerField(null=True, blank=True)
    age_max = models.IntegerField(null=True, blank=True)
    age_group = models.CharField(
        max_length=60, null=True, blank=True, choices=agegroup_choices
    )
    status = models.CharField(
        choices=status_choices, max_length=60, null=True, blank=True, default="Inactive"
    )


# Preferred_Age
class Preferred_age(models.Model):
    preferred_age_id = models.AutoField(primary_key=True, editable=False)
    age_id = models.ForeignKey(
        Age_table, on_delete=models.CASCADE, null=True, blank=True
    )
    doctor_id = models.ForeignKey(
        User_table, on_delete=models.CASCADE, null=True, blank=True
    )


# Message model
class Message_table(models.Model):
    message_id = models.AutoField(primary_key=True, editable=False)
    chat_id = models.ForeignKey(
        Chat_table, on_delete=models.CASCADE, null=True, blank=True
    )
    sender_id = models.ForeignKey(
        User_table, on_delete=models.CASCADE, null=True, blank=True
    )
    message_type = models.CharField(max_length=60, null=True, blank=True)
    message = models.CharField(max_length=60, null=True, blank=True)
    file_name = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)


# preferred_language model
class Preferred_language(models.Model):
    preferred_language_id = models.AutoField(primary_key=True, editable=False)
    language_id = models.ForeignKey(
        Language_table, on_delete=models.CASCADE, null=True, blank=True
    )
    user_id = models.ForeignKey(
        User_table, on_delete=models.CASCADE, null=True, blank=True
    )


# Country model
class Country_table(models.Model):
    country_id = models.AutoField(primary_key=True, editable=False)
    country_name = models.CharField(
        max_length=60, choices=country_choices, blank=True, null=True, default="India"
    )


# state model
class State_table(models.Model):
    state_id = models.AutoField(primary_key=True, editable=False)
    country_id = models.ForeignKey(
        Country_table, on_delete=models.CASCADE, null=True, blank=True
    )
    state_name = models.CharField(
        choices=state_choices, max_length=60, null=True, blank=True
    )
