from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from course.models import Course, Subscription
from lesson.models import Lesson
from users.models import User, UserRoles


class LessonsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@yandex.ru',
            is_staff=True,
            is_active=True,
            is_superuser=True,
            role=UserRoles.SUPERUSER
        )
        self.user.set_password('test')
        self.user.save()

        self.access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.course = Course(
            name='test',
            owner=self.user,
            link='youtube',
        )
        self.course.save()

        self.lesson = Lesson(
            name='test',
            owner=self.user,
            link='youtube',
        )

        self.lesson.save()

        self.sub = Subscription(
            user=self.user,
            course=self.course,
            is_active=True
        )

        self.sub.save()

    def test_create_subscription(self):
        subscription = {'course': self.course.pk, 'user': self.user.pk, 'is_active': True}
        response = self.client.post('/subscribe/', subscription)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['user'], self.user.pk)
        self.assertEqual(response.json()['course'], self.course.pk)
        response = self.client.get(f'/courses/{self.course.pk}/')
        self.assertEqual(bool(response.json()['active_sub']), True)

    def test_get_list(self):
        """Test for getting list of lessons"""

        response = self.client.get(
            reverse('lesson:lesson-list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "course": None,
                        "name": self.lesson.name,
                        "description": self.lesson.description,
                        "image": None,
                        "link": self.lesson.link,
                        "owner": self.lesson.owner.pk
                    }
                ]
            }
        )

    def test_get_create(self):
        """Test lesson create"""

        data = {
            'name': 'test2',
            'course': self.course.id,
            "link": "https://www.youtube.com/"

        }

        response = self.client.post(
            reverse('lesson:lesson-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            2
        )

    #
    def test_lesson_validation_error(self):
        """Test lesson validation error"""

        data = {
            'title': 'test3',
            'course': self.course.id,
            'url': 'ссылка'
        }

        response = self.client.post(
            reverse('lesson:lesson-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_lesson_update(self):
        """Test lesson update"""
        url = reverse('lesson:lesson-update', kwargs={'pk': self.lesson.pk})

        data = {
            'name': self.lesson.name,
            'description': 'update_test'
        }

        response = self.client.put(url, data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {
                "id": self.lesson.id,
                "course": None,
                "name": self.lesson.name,
                "description": 'update_test',
                "image": None,
                "link": self.lesson.link,
                "owner": self.lesson.owner.pk
            }
        )

    #
    def test_lesson_delete(self):
        """Test lesson delete"""

        url = reverse('lesson:delete-update', kwargs={'pk': self.lesson.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists(),
        )

    def test_sub_create(self):
        """Subscribe create test"""

        data = {
            'user': self.user,
            'is_active': True,
            'course': self.course
        }

        response = self.client.post(
            reverse('course:subscribe-list'),
            data=data
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    #
    #
    def test_sub_list(self):
        """Subscribe list test"""


        response = self.client.get(
            reverse('course:subscribe-list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{'user': self.user.pk, 'course': self.course.pk, 'is_active': self.subscription.is_active}]

        )

    def test_sub_update(self):
        """Test update sub"""

        url = reverse('course:subscribe-detail', kwargs={'pk': self.sub.pk})

        data = {
            'is_active': False
        }

        response = self.client.put(url, data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': self.user.pk, 'is_active': False, 'user': self.user.pk, 'course': self.course.pk, }

        )

    def test_sub_delete(self):
        """Test sub delete"""

        response = self.client.delete(f'/subscribe/{self.course.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)