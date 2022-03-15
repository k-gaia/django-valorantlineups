from unicodedata import name
from django.test import TestCase
from lineups.models import ChildLineup

# Child Lineup Test Class, Derived from Test Case
class ChildLineupTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):

        # setup non modified objects used by all test methods
        # i.e. create an example Child Lineup Entry
        ChildLineup.objects.create(name='Test Lineup', 
        content='www.youtube.com/embed/QRysR76_gMA?start=147', 
        xPos=10, 
        yPos=20)

    # test field name on 'name field'
    def test_name_label(self):
        childlineup = ChildLineup.objects.get(id=1)
        field_label = childlineup._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test field name on 'content field'
    def test_content_label(self):
        childlineup = ChildLineup.objects.get(id=1)
        field_label = childlineup._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    # test field name on 'xPos'
    def test_xPos_label(self):
        childlineup = ChildLineup.objects.get(id=1)
        field_label = childlineup._meta.get_field('xPos').verbose_name
        self.assertEqual(field_label, 'xPos')

    # test field name on 'yPos'
    def test_yPos_label(self):
        childlineup = ChildLineup.objects.get(id=1)
        field_label = childlineup._meta.get_field('yPos').verbose_name
        self.assertEqual(field_label, 'yPos')

    # test name max length value
    def test_name_max_length(self):
        childlineup = ChildLineup.objects.get(id=1)
        max_length = childlineup._meta.get_field('name').max_length
        self.assertEqual(max_length, 32)

    # test to string method, is called when object is selected in admin page
    def test_object_name_is_id_and_fields(self):
        childlineup = ChildLineup.objects.get(id=1)
        
        # expected name is of form id - name - content - xpos - ypos
        expected_object_name = f'{str(childlineup.id)} - \
        {childlineup.name} - \
        {childlineup.content} - \
        {str(childlineup.xPos)} - \
        {str(childlineup.yPos)}'

        # call the to string method on child lineup object
        self.assertEqual(str(childlineup), expected_object_name)
