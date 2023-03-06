from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Recruiter(models.Model):
    class SkillChoices(models.TextChoices):
        PYTHON = 'Py', ('Python')
        REACT = 'React', ('React')
        DJANGO = 'DJ', ('Django')
        FLASK = 'FLASK', ('Flask')
        HTML = 'HTML', ('Html')
        CSS = 'CSS', ('CSS')

    class EducationChoices(models.TextChoices):
        MATRIC = 'matric', ('Matric')
        INTER = 'inter', ('Intermediate')
        BSCS = 'BS', ('BSCS')
        MASTER_IN_MATH = 'Master-in-Math', ('Master in Math')
        SOFTWARE_ENGINEERING = 'S-Engineering', ('Sofware Engineering')


    user = models.OneToOneField(User, verbose_name=("Recruiter"), on_delete=models.CASCADE)
    current_job_post = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=10, choices=SkillChoices.choices)
    education = models.CharField(max_length=30, choices=EducationChoices.choices)
    about = models.TextField(max_length=50, null=True, blank=True)
    total_employees_hired = models.PositiveIntegerField(blank=False, null=False)
    company_name = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self) -> str:
        return self.user.username


class JobPost(models.Model):
    class RequiredSkill(models.TextChoices):
        PYTHON = 'Py', ('Python')
        REACT = 'React', ('React')
        DJANGO = 'DJ', ('Django')
        FLASK = 'FLASK', ('Flask')
        HTML = 'HTML', ('Html')
        CSS = 'CSS', ('CSS')
    
    class MinQualificationRequired(models.TextChoices):
        MATRIC = 'matric', ('Matric')
        INTER = 'inter', ('Intermediate')
        BSCS = 'BS', ('BSCS')
        MASTER_IN_MATH = 'Master-in-Math', ('Master in Math')
        SOFTWARE_ENGINEERING = 'S-Engineering', ('Sofware Engineering')

    class GenderPreference(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F', ('Female')
        OTHERS = 'O', ('Others')

    recruiter = models.ForeignKey(Recruiter, on_delete=models.PROTECT)
    job_title = models.CharField(max_length=50, null=False, blank=False)
    job_description = models.TextField(max_length=150, null=True, blank=True)
    required_skills = models.CharField(max_length=50, choices=RequiredSkill.choices)
    number_of_positions = models.PositiveIntegerField()
    job_location = models.CharField(max_length=30)
    minimum_qualification_required = models.CharField(max_length=20, choices=MinQualificationRequired.choices)
    required_experience = models.CharField(max_length=30)
    minimum_salary = models.PositiveIntegerField()
    maximum_salary = models.PositiveIntegerField()
    salary_visibility = models.BooleanField(default=True)
    gender_prefrences = models.CharField(max_length=20, choices=GenderPreference.choices)

    def __str__(self) -> str:
            return f"{self.job_title}, {self.job_location}"



