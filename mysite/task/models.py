from django.db import models


class FirstUserModel(models.Model):
    TEXT = (
        ('Предложения', '1'),
        ('Предложения', '2'),
        ('Предложения', '3'),
        ('Предложения', '4'),
    )

    first_name = models.CharField(max_length=32, verbose_name="first name")
    last_name = models.CharField(max_length=32, verbose_name="last name")
    Job = models.CharField(max_length=32, verbose_name="Job")
    email = models.EmailField(verbose_name='email', null=True)
    domain_name = models.CharField(max_length=32, verbose_name="domain name")
    phone_number = models.CharField(max_length=20, verbose_name="phone number")
    company_name = models.CharField(max_length=32, verbose_name="company name")
    order = models.CharField(max_length=32, choices=TEXT, verbose_name="order")
    address = models.CharField(max_length=32, verbose_name="address")
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'