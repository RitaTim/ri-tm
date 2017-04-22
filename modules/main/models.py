# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


def get_photo_path(instance, filename):
    return "img/photo/%s" % filename


def get_project_img_path(instance, filename):
    return "img/projects/%s" % filename


class Employee(models.Model):
    """
        Работник
    """
    name = models.CharField(u"ФИО", max_length=100)
    position = models.CharField(u"Должность", max_length=100)
    address = models.CharField(u"Адрес", max_length=100)
    phone = models.CharField(u"Телефон", max_length=100)
    email = models.EmailField(u"E-mail", max_length=100)
    site = models.CharField(u"Сайт", max_length=100)
    about = models.TextField(u"О себе", blank=True, null=True)
    photo = models.ImageField(upload_to=get_photo_path, verbose_name=u"Фото", blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = u'Работник'
        verbose_name_plural = u'Работники'


class Skill(models.Model):
    """
        Навык работника в процентах владения
    """
    title = models.CharField(u"Название", max_length=100)
    percent = models.IntegerField(u"Процент владения")
    employee = models.ForeignKey(Employee, verbose_name="Работник", related_name="skills")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Навык'
        verbose_name_plural = u'Навыки'


class Organization(models.Model):
    """
        Организация
    """
    title = models.CharField(u"Название", max_length=100)
    link = models.CharField(u"Ссылка", max_length=100)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'


class Experience(models.Model):
    """
        Опыт
    """
    employee = models.ForeignKey(Employee, verbose_name=u"Работник")
    organization = models.ForeignKey(Organization, verbose_name=u"Организация", max_length=100)
    working_time = models.CharField(u"Время работы", max_length=100)
    duties = models.TextField(u"Обязанности", blank=True, null=True)
    technologies = models.TextField(u"Технологии", blank=True, null=True)

    def __str__(self):
        return self.organization.title


    class Meta:
        verbose_name = u'Опыт работы'
        verbose_name_plural = u'Опыт работы'


class Project(models.Model):
    """
        Выполненные проекты
    """
    employee = models.ForeignKey(Employee, verbose_name="Исполнитель")
    title = models.CharField(u"Название", max_length=100)
    link = models.CharField(u"Ссылка", max_length=100)
    customer = models.ForeignKey(Organization, verbose_name=u"Заказчик")
    duties = models.TextField(u"Обязанности", blank=True, null=True)
    technologies = models.TextField(u"Технологии", blank=True, null=True)
    img = models.ImageField(upload_to=get_project_img_path,
                             verbose_name=u"Картинка", blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'