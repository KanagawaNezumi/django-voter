# django-voter

Django contenttypes 实现的通用赞踩系统app.

Add django-voter

```python
INSTALLED_APPS = (
  ...
  'voter',
)
```

Inherit `VoteMixin` for your model, example:

```python
from django.db import models
from voter.models import VoteMixin

class Post(VoteMixin, models.Model): 
  title = models.CharField(max_length=20)
```

Run migrate

```python
manage.py makemigrations
manage.py migrate
```

API Reference 

```python

# upvote/downvote/neutralvote(cancel vote) the post by user
# return True if success
# return False if user already voted the same or 
# trying to cancel an unexisted vote

post.upvote_by(user)
post.downvote_by(user)
post.neutralvote_by(user)

# bulk upvote/downvote/neutralvote(cancel vote) the post by users 
# return the number of users
# never return False

post.bulk_upvote_by(*users)
post.bulk_downvote_by(*user)
post.bulk_neutralvote_by(*user)

# check if the post upvoted/downvoted or just voted by user
# return a Bool

post.is_upvoted_by(user)
post.is_downvoted_by(user)
post.is_voted_by(user)

# get users who upvoted/downvoted (or just voted) the post
# return a QuerySet of users

post.get_upvoted_users()
post.get_downvoted_users()
post.get_voted_users()

# get objs upvoted/downvoted (or just voted) by user
# return a QuerySet of posts or any other model instances

Post.voter.get_user_upvoted(user)
Post.voter.get_user_downvoted(user)
Post.voter.get_user_voted(user)

# all models mixed VoteMixin hava three extra fields

post.up_count # int
post.down_count # int
post.upvote_rate # float (0.0 ~ 1.0)
```
