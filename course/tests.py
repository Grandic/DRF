from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Subscription
from lesson.models import Lesson
from users.models import User

class LessonsTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test'
        )
        self.lesson = Lesson.objects.create(
            name='test',
            course=self.course
        )

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
                        "course": self.course.name,
                        "name": self.lesson.name,
                        "description": self.lesson.description,
                        "image": self.lesson.image,
                        "link": self.lesson.link
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


class LessonsUpdateTestCase(APITestCase):
    """Lesson update tests"""

    def setUp(self):
        self.lesson = Lesson.objects.create(
            name='test',
            description='test'
        )

    def test_lesson_update(self):
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
                        "image": self.lesson.image,
                        "link": self.lesson.link
                    }
        )


    def test_lesson_delete(self):

        url = reverse('lesson:delete-update', kwargs={'pk': self.lesson.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists(),
        )


class CreateSubscription(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test111',
            is_staff=True,
            is_active=True,
        )
        self.user.set_password('12345678')
        self.user.save()
        self.client.force_authenticate(self.user)

        self.course = Course.objects.create(
            name='test'
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
            is_active=True
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

        url = reverse('course:subscribe-detail', kwargs={'pk': self.subscription.pk})

        data = {
            'user': self.subscription.user.pk,
            'is_active': False
        }

        response = self.client.put(url, data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'user': self.user.pk, 'course': self.course.pk, 'is_active': False}

        )


    def test_sub_delete(self):
        """Test sub delete"""

        url = reverse('course:subscribe-detail', kwargs={'pk': self.subscription.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists(),
        )