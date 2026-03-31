from django.test import TestCase
from django.urls import reverse

from .models import Author, Post, Tag


class ReadLaterViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first="Test",
            last="Author",
            email="author@example.com",
        )
        self.tag = Tag.objects.create(name="django")
        self.post = Post.objects.create(
            title="Read Later Post",
            content="Useful content",
            author=self.author,
        )
        self.post.tags.add(self.tag)

    def test_read_later_page_renders_saved_posts(self):
        session = self.client.session
        session["stored_posts"] = [self.post.id]
        session.save()

        response = self.client.get(reverse("read-later"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_contains_post_id_for_read_later_form(self):
        response = self.client.get(
            reverse("post-details", args=[self.post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="post_id"')

    def test_saving_from_post_detail_redirects_back_to_post(self):
        post_detail_url = reverse("post-details", args=[self.post.slug])
        response = self.client.post(
            reverse("read-later"),
            {"post_id": self.post.id, "next": post_detail_url},
        )

        self.assertRedirects(response, post_detail_url)
        self.assertIn(self.post.id, self.client.session["stored_posts"])
