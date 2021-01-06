from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class courses(models.Model):
    c_id = models.CharField(max_length=6, primary_key=True)
    c_name = models.CharField(max_length=30)

    def __str__(self):
        return self.c_name

class academician(models.Model):
    aca_id = models.CharField(max_length=3, primary_key= True)
    aca_name = models.CharField(max_length=15)
    aca_surname = models.CharField(max_length=15)
    aca_email = models.EmailField()
    aca_c_id = models.ForeignKey(courses , on_delete= models.RESTRICT) #academician course id

    def __str__(self):
        return self.aca_name


class student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=15)
    s_surname = models.CharField(max_length=15)
    s_email = models.EmailField()



class lectureNotes(models.Model):
    l_course_id = models.ForeignKey(courses, on_delete=models.RESTRICT)
    l_cname = models.ForeignKey(courses, on_delete= models.RESTRICT)
    l_name = models.CharField(max_length=20)
#
# class videos(models.Model):
#     v_c = models.ForeignKey(courses, on_delete=models.RESTRICT, related_name='c_id')
#     v_cname = models.ForeignKey(courses, on_delete=models.RESTRICT, related_name='c_name')
#     v_name = models.CharField(max_length=20)
#
class books(models.Model):
    b_course_id = models.ForeignKey(courses, on_delete=models.RESTRICT)
    b_cname = models.ForeignKey(courses, on_delete=models.RESTRICT)
    b_name = models.CharField(max_length=20)

# class notes(models.Model):
#     l_notes_id = models.CharField(max_length=3, primary_key=True)
#     l_notes_name = models.CharField(max_length=50)
#
#     b_id = models.CharField(max_length=2,primary_key=True)
#     b_name = models.CharField(max_length=50)


class l_document(models.Model):
    lec_name = models.CharField(max_length=255, default='Document_name')
    l_aca = models.ForeignKey(academician, on_delete=models.CASCADE)
    myfile = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx'])
    ])

    def __str__(self):
        return self.name

class b_document(models.Model):
    book_name = models.CharField(max_length=255, default='Document_name')
    b_aca = models.ForeignKey(academician, on_delete=models.CASCADE)
    myfile = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx'])
    ])

    def __str__(self):
        return self.name