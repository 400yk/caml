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
class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length = 63)
    password = models.CharField(max_length = 63)
    email = models.EmailField()
    phone = models.IntegerField(max_length = 31)
    skype_id = models.CharField(max_length = 63)
    qq_id = models.CharField(max_length = 63)
    fav_program = models.ManyToManyField(Program) # Favorite program 
    fav_school = models.ManyToManyField(School) # Favorite School    
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

class Question(models.Model):
    question_id = models.IntegerField(primary_key = True)
    question = models.TextField()
    
    def __unicode__(self):
        return question

# A table recording the purchase for a user and how many hours of consulting has been used
class Package(models.Model):
    package_id = models.IntegerField(primary_key = True)
    package_name = models.CharField(max_length = 255)
    price = models.DecimalField() # Original price for each package, maybe overwritten by any promotion
    freq = models.CharField(max_length = 31) # Hourly, each time, one time, Daily, Weekly, Monthly, Quarterly, Annually
    
    def __unicode__(self):
        return self.package_name

class Tracking(models.Model):
    package = models.ForeignKey(Package)
    user = models.ForeignKey(User)
    total = models.IntegerField()
    remaining = models.IntegerField()
    unit = models.CharField(max_length = 31)

class Program(models.Model):
    program_id = models.IntegerKey(primary_key = True)
    name = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255)
    major = models.CharField(max_length = 63)
    department = models.CharField(max_length = 255)
    link = models.TextField()
    contact = models.EmailField()
    length = models.DecimalField()
    description = models.TextField()
    enrolling = models.CharField(max_length = 31) # If enrolling in Spring or Fall, or other month of the year
    application_deadline = models.TextField() # Application deadline
    application_fee = models.DecimalField()
    application_material = models.TextField()
    required_tests = models.CharField(max_length = 255)
    english_requirement = models.TextField()
    application_review = models.CharField(max_length = 255) # Rolling basis, or one at a time
    admission_decision = madels.CharField(max_length = 255) # When will the decision come out
    acceptance_rate = models.DecimalField() 
    attendance_rate = models.DecimalField()
    number_students = models.IntegerField() # Number of students in the program in the most recent year
    percentage_international = models.DecimalField() # Percentage of international students
    percentage_chinese = models.DecimalField() # Percentage of Chinese students
    average_gpa = models.





class Calendar(models.Model):
    pass
