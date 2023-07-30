from django.db import models

# Create your models here.
class RequestExchange(models.Model):
    input = models.CharField(verbose_name='Валюта продажи', max_length=255, blank=True, null=True)
    amount_input = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Сумма продажи', blank=True, null=True)
    output = models.CharField(verbose_name='Валюта покупки', max_length=255, blank=True, null=True)
    amount_output = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Сумма покупки', blank=True, null=True)
    telegram_login = models.CharField(verbose_name='Логин телеграм', max_length=255, blank=True, null=True)
    fio = models.CharField(verbose_name='ФИО', max_length=1024, blank=True, null=True)
    description = models.CharField(verbose_name='Примечание', max_length=1024, blank=True, null=True)
    input_card = models.CharField(verbose_name='Кошелек или карта отправителя', max_length=1024, blank=True, null=True)
    output_card = models.CharField(verbose_name='Кошелек или карта получателя', max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return '{0} {1} - {2} {3}. {4}'.format(self.input, self.amount_input, self.output, self.amount_output, self.fio)
