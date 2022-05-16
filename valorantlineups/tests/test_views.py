from django.test import TestCase
from lineups.views import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

class TestCalls(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        ChildLineup.objects.create(name='Test Lineup', 
        content='www.youtube.com/embed/QRysR76_gMA?start=147', 
        xPos=10, 
        yPos=20)

    def test_home_view(self):
        url = reverse(home)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
    def test_bind_view(self):
        url = reverse(bind)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_haven_view(self):
        url = reverse(haven)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_split_view(self):
        url = reverse(split)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_ascent_view(self):
        url = reverse(ascent)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_get_lineup_creator_view(self):
        url = reverse(lineup_creator)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
    def test_get_pin_creator_view(self):
        url = reverse(pin_creator)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_login_view(self):
        url= reverse(login_request)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_login_success(self):

        # create url by looking up what the view's url is, create test client object 
        # reverse is a function from Django, useful for quickly writing
        # shorthand urls, instead of hardcoding them
        url= reverse(login_request)
        c = Client()

        # response object to test the response code, which should be a redirect code of 302
        resp = c.post(url, {'username': 'testuser', 'password': '12345'})
        self.assertEqual(resp.status_code, 302)

    def test_login_failure(self):

        url= reverse(login_request)
        c = Client()

        resp = c.post(url, {'username': 'testuser', 'password': '54321'})
        
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        c = Client()
        c.post(reverse(login_request), {'username': 'testuser', 'password': '54321'})

        url= reverse(logout_request)

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)

    def test_register_success(self):

        # create url by looking up what the view's url is, create test client object 
        # reverse is a function from Django, useful for quickly writing
        # shorthand urls, instead of hardcoding them
        url= reverse(register_request)
        c = Client()

        # response object to test the response code, which should be a redirect code of 302
        resp = c.post(url, {'username': 'bestuserever', 'email': 'test@test.com', 'password1': 'testpassword@123', 'password2': 'testpassword@123'})
        self.assertEqual(resp.status_code, 302)

    def test_register_failure(self):

        # create url by looking up what the view's url is, create test client object 
        # reverse is a function from Django, useful for quickly writing
        # shorthand urls, instead of hardcoding them
        url= reverse(register_request)
        c = Client()

        # response object to test the response code, which should be a redirect code of 302
        resp = c.post(url, {'username': 'bestuserever', 'email': 'test@test.com', 'password1': 'testpassword', 'password2': 'testpassword@123'})
        self.assertEqual(resp.status_code, 200)

    def test_lineups_list_view(self):
        url= reverse(lineups_list)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_child_lineups_list_view(self):
        url= reverse(child_lineups_list)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_get_latest_child_lineup_id(self):
        url= reverse(get_latest_childlineup_id)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    """def test_get_latest_child_lineup_id_emptydb(self):
        ChildLineup.objects.filter(id=1).delete()
        url= reverse(get_latest_childlineup_id)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)"""

    def test_pin_creator_post_success(self):
        # url to post form data to
        url = reverse(pin_creator)
        # form data which must conform to form template otherwise will fail
        form_data = {'name':'test',
        'content': 'www.youtube.com/embed/QRysR76_gMA?start=147',
        'xPos': 20,
        'yPos': 30}

        # send post request with filled data to target url 
        resp = self.client.post(url, form_data)
        self.assertEqual(resp.status_code, 200)

    def test_pin_creator_post_fail(self):
        url = reverse(pin_creator)
        # make sure form data is invalid as this will test the fail state
        form_data = {'name':'test',
        'content': 'www.youtube.com/embed/QRysR76_gMA?start=147',
        'xPos': "invalid",
        'yPos': 30}

        resp = self.client.post(url, form_data)
        self.assertEqual(resp.status_code, 200)

    def test_lineup_creator_post_success(self):
        url = reverse(lineup_creator)
        form_data = {'character':'sage', 'ability':'slow_orb', 'xPos':20,'yPos':20, 'map':'ascent', 'childPinAmount':2, 'childPinIds':'', 'isAttacking':False,
        'rating':0, 'createdOn':'', 'author':''}

        resp = self.client.post(url, form_data)
        self.assertEqual(resp.status_code, 200)

    







