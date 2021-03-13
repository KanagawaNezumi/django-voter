from django.test import TestCase
from django.contrib.auth.models import User
from .models import VoterTestModel

# class VoteTestCase(TestCase):
#     def setUp(self):
#         VoterTestModel.objects.create(title="voter test case1")
#         VoterTestModel.objects.create(title="voter test case2")
#         User.objects.create_user('user1', 'user1@gmail.com', 'user1password')
#         User.objects.create_user('user2', 'user2@gmail.com', 'user2password')

#     def test_voter(self):
#         obj1 = VoterTestModel.objects.first()
#         obj2 = VoterTestModel.objects.last()
#         user1 = User.objects.get(username='user1')
#         user2 = User.objects.get(username='user2')
#         obj1.upvote_by(user1)
#         self.assertEqual(obj1.up_count, 1)
#         obj1.upvote_by(user2)
#         self.assertEqual(obj1.up_count, 2)
#         obj1.downvote_by(user1)
#         self.assertEqual(obj1.up_count, 1)
#         self.assertEqual(obj1.down_count, 1)
#         obj1.neutralvote_by(user2)
#         self.assertEqual(obj1.up_count, 0)
#         obj1.upvote_by(user2)
#         obj2.upvote_by(user2)
#         self.assertEqual([user2], list(obj1.get_upvoted_users()))
#         self.assertEqual([user1], list(obj1.get_downvoted_users()))
#         self.assertEqual([user1, user2], list(obj1.get_voted_users()))
#         self.assertEqual([obj1], list(VoterTestModel.voter.get_user_downvoted(user1)))
#         self.assertEqual([obj1, obj2], list(VoterTestModel.voter.get_user_upvoted(user2)))
#         obj2.bulk_downvote_by(user1, user2)
#         self.assertEqual(obj2.down_count, 2)
#         self.assertEqual(obj2.up_count, 0)
#         obj2.bulk_neutralvote_by(user1, user2)
#         self.assertEqual(obj2.down_count, obj2.up_count)
#         obj2.bulk_upvote_by(user1, user2)
#         self.assertEqual(obj2.up_count, 2)
#         self.assertEqual(obj2.down_count, 0)