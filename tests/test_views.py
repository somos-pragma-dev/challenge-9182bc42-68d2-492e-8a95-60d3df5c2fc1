class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        self.profile = UserProfile.objects.create(user=self.user, bio='Test Bio')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/login.html')

    def test_admin_panel_view(self):
        self.client.login(username='testuser', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('admin_panel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/admin_panel.html')