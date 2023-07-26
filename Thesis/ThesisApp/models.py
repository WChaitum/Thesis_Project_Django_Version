from django.db import models

class Person(models.Model):
    Parent_name = models.CharField(max_length=100)
    Parent_key = models.CharField(max_length=100)
    children_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    time = models.TimeField(default='00:00:00')  # กำหนดค่าเริ่มต้นเป็น '00:00'
    Parent_image = models.ImageField(upload_to='Images',blank=True)
    children_image = models.ImageField(upload_to='Images',blank=True)

    # โค้ดอื่นๆ ของโมเดล Person ที่คุณมีอยู่

    def __str__(self):
        return "Name : "+self.Parent_name +" "+"Tine : "+str(self.time)