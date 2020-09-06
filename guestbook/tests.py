# from django.test import TestCase
from guestbook.models import fetchlist
import guestbook.models as guestbookmodel


def test_guestboomodel_insert():
    guestbookmodel.insert('김종익', '1234', '안녕하세요')


def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)


def test_guestbookmodel_delete():
    guestbookmodel.delete(11, '1234')


# test_guestboomodel_insert()
test_guestbookmodel_delete()
test_guestbookmodel_fetchlist()