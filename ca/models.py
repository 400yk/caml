# TODO: Add foreign key relationship from program to university
from django.db import models
''' User table:
    Profile/Password editor
    Favourite programs
    Resume/CV
    Brainstorming exercises
    Letters of recommendation
    Preparing for the interview
    Package purchase list/consuming list
    Scheduled calendar
'''
class Question(models.Model):
    question_id = models.IntegerField(primary_key = True)
    question = models.TextField(blank = True)
    
    def __unicode__(self):
        return question

# A table recording the purchase for a user and how many hours of consulting has been used
class Package(models.Model):
    package_id = models.IntegerField(primary_key = True)
    package_name = models.CharField(max_length = 255, blank = True)
    price = models.DecimalField(max_digits = 19, decimal_places = 5, blank = True, null = True) # Original price for each package, maybe overwritten by any promotion
    freq = models.CharField(max_length = 31, blank = True) # Hourly, each time, one time, Daily, Weekly, Monthly, Quarterly, Annually
    
    def __unicode__(self):
        return self.package_name

class University(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    year_founded = models.IntegerField(blank = True, null = True)
    public_private = models.CharField(max_length = 31, blank = True)
    enrollment = models.CharField(blank = True, max_length = 255)
    location = models.CharField(max_length = 255, blank = True)
    setting = models.CharField(max_length = 255, blank = True)

    def __unicode__(self):
        return self.name

class Program(models.Model):
    program_id = models.IntegerField(primary_key = True)
    program_category = models.CharField(max_length = 255, blank = True)
    university = models.CharField(max_length = 255, blank = True)
    name = models.CharField(max_length = 255, blank = True)
    # Academics
    degree = models.CharField(max_length = 255, blank = True)
    major = models.CharField(max_length = 63, blank = True)
    academic_professional = models.CharField(max_length = 63, blank = True)
    department = models.CharField(max_length = 255, blank = True)
    link = models.TextField(blank = True)
    contact = models.EmailField(blank = True)
    description = models.TextField(blank = True)
    #length = models.DecimalField(max_digits = 7, decimal_places = 4, blank = True, null = True)
    length = models.CharField(max_length = 255, blank = True)
    career = models.CharField(max_length = 255, blank = True)
    faculty = models.CharField(max_length = 255, blank = True)
    # Admission
    enrolling = models.CharField(max_length = 31, blank = True) # If enrolling in Spring or Fall, or other month of the year
    application_deadline = models.TextField(blank = True) # Application deadline
    application_fee = models.DecimalField(max_digits = 10, decimal_places = 4, null = True, blank = True)
    application_material = models.TextField(blank = True)
    required_tests = models.CharField(max_length = 255, blank = True)
    english_requirement = models.TextField(blank = True)
    application_review = models.CharField(max_length = 255, blank = True) # Rolling basis, or one at a time
    admission_decision = models.CharField(max_length = 255, blank = True) # When will the decision come out
    acceptance_rate = models.DecimalField(max_digits = 5, decimal_places = 4, blank = True, null = True) 
    attendance_rate = models.DecimalField(max_digits = 5, decimal_places = 4, blank = True, null = True)
    # Class Profile
    #number_students = models.IntegerField(blank = True, null = True) # Number of students in the program in the most recent year
    number_students = models.CharField(max_length = 255, blank = True)
    percentage_international = models.DecimalField(max_digits = 5, decimal_places = 4, blank = True, null = True) # Percentage of international students
    percentage_chinese = models.DecimalField(max_digits = 5, decimal_places = 4, blank = True, null = True) # Percentage of Chinese students
    average_gpa = models.DecimalField(max_digits = 6, decimal_places = 4, blank = True, null = True)
    average_gre = models.CharField(max_length = 255, blank = True)
    undergrad_institution = models.CharField(max_length = 255, blank = True) # Undergrad instituion represented
    # Cost
    tuition = models.IntegerField(blank = True, null = True)
    books_supplies = models.IntegerField(blank = True, null = True)
    living_cost = models.IntegerField(blank = True, null = True)
    scholarships_aid = models.TextField(blank = True)
    
    def __unicode__(self):
        return self.name

class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length = 63)
    password = models.CharField(max_length = 63)
    email = models.EmailField()
    phone = models.IntegerField(max_length = 31, blank = True, null = True)
    skype_id = models.CharField(max_length = 63, blank = True)
    qq_id = models.CharField(max_length = 63, blank = True)
    fav_program = models.ManyToManyField(Program) # Favorite program 
    fav_university = models.ManyToManyField(University) # Favorite School    
    packages = models.ManyToManyField(Package, through = 'Tracking')

    def __unicode__(self):
        return self.user_name

# One user can have multiple resumes
class Resume(models.Model):
    resume_id = models.IntegerField(primary_key = True)
    user = models.ForeignKey(User)
    content = models.TextField(null = True, blank = True)

# Personal Statement
class PS(models.Model):
    ps_id = models.IntegerField(primary_key = True)
    user = models.ForeignKey(User)
    title = models.TextField(null = True, blank = True)
    content = models.TextField(null = True, blank = True)

# Letter of Recommendation
class LOR(models.Model):
    lor_id = models.IntegerField(primary_key = True)
    user = models.ForeignKey(User)
    content = models.TextField(null = True, blank = True)

# Brain Storming questions, this table contains each user's response to 
# each question that applies to that user (question_id isn't unique)
class BS(models.Model):
   bs_id = models.IntegerField(primary_key = True)
   question_id = models.ForeignKey(Question)
   user_id = models.ForeignKey(User)
   answer = models.TextField(null = True, blank = True)

class Tracking(models.Model):
    package = models.ForeignKey(Package)
    user = models.ForeignKey(User)
    total = models.IntegerField(blank = True, null = True)
    remaining = models.IntegerField(blank = True, null = True)
    unit = models.CharField(max_length = 31, blank = True)

class Calendar(models.Model):
    pass
