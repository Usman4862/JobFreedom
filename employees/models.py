from django.db import models
from django.contrib.auth.models import User
# Create your models here.
EDUCATION_CHOICES = (
    ('matric','Matric'),
    ('fsc-nm','Fsc_Non_Medical'),
    ('fsd-m','Fs.c_Medical'),
    ('bs-eng','Bachelor in English'),
    ('bscs', 'Bachelor in Computer Science'),
    ('bs-Math', 'Bachelor in Mathematics'),
    ('bs-IS', 'Bachelor in Islamist'),
    ('bba', 'Bachelor in Business'),
    ('bs_phy', 'Bachelor in Physics'),
    ('ms-eng', 'Masters in English'),
    ('ms-phy', 'Masters in Physics'),
    ('ms-math', 'Masters in Mathematics'),
    ('mscs', 'Master in Computer Science'),
    ("mphil", 'M-Phil'),
    ('phd-cs','P-hd in Computer science')
)

INTEREST_CHOICES= (
    ('Teaching', 'Teaching'),
    ('Business', 'Business'),
    ('it', 'Information Technology'),
    ('cs', 'Computer Science'),
    ('cyber-s', 'Cyber Security'),
    ('ai','Artificial Intelligence'),
    ('mc','Machine Learning'),
    ('army','Army'),
    ('sports','Sports'),
    )



class Employeeprofile(models.Model):
   
   class ChoicesEmployeeSkills(models.TextChoices):
        PYTHON = 'PY', ('Python')
        DJANGO = 'DJ', ('Django')
        FLASK = 'FL', ('Flask')
        JAVASCRIPT = 'JS', ('Javascript')
        RUST = 'RT', ('Rust')
    
   user =  models.OneToOneField(User, on_delete=models.CASCADE)
   skills = models.CharField(max_length=200, choices=ChoicesEmployeeSkills.choices)
   education = models.CharField(max_length=100,choices=EDUCATION_CHOICES)
   about = models.TextField(max_length=500)
   interest =models.CharField(max_length=100, choices=INTEREST_CHOICES)

   def __str__(self):
       return f'{self.user}'

class EmployeeProject(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=60)
    project_description = models.TextField(max_length=500)
    project_link = models.URLField(max_length=200, null=True, blank=True)
    project_file = models.FileField

    def __str__(self) :
        return f'{self.employee.username}'

class Jobapplication(models.Model):
    SALARY_CHOICES = (
        ('50k','50k'),
        ('70k', '70k'),
        ('80k','80k'),
        ('100k','100k'),
        ('150k','150k'),
        ('200k','200k'),
        ('250k','250k')
        )     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='applications/resume', null=True, blank=True)
    expected_salary =models.CharField(max_length=20,choices=SALARY_CHOICES)
    summary = models.TextField(max_length=500)
    
    def __str__(self) :
        return f'{self.user.username}'
