from django.db import models


def get_ip(request):
    """Получение IP адреса клиента"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Survey(models.Model):
    """Модель опроса"""
    title = models.CharField('Заголовок', max_length=128)
    start_date = models.DateTimeField('Дата старта', auto_now_add=True)
    finish_date = models.DateTimeField('Дата окончания')
    text = models.CharField('Текст', max_length=256)
    is_active = models.BooleanField('Активен', default=True, db_index=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопроса"""
    TEXT = 'TX'
    CHOICE = 'CE'
    CHOICES = 'CS'
    TYPE_CHOICES = (
        (TEXT, 'Текст'), (CHOICE, 'Выбор варианта'), (CHOICES, 'Выбор вариантов')
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions', verbose_name='Опрос')
    text = models.CharField('Текст', max_length=128)
    type = models.CharField('Тип вопроса', max_length=2, choices=TYPE_CHOICES, default='CE')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True, db_index=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.text}({self.survey})'


class Response(models.Model):
    """Модель ответа"""
    ip = models.CharField('IP адрес', max_length=15)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Ответ')
    choice_text = models.CharField('Текст ответа', max_length=256)
    pub_date = models.DateTimeField('Дата ответа', auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.choice_text} ({self.question}_)'
