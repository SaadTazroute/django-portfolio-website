import os
from datetime import timezone

from django.db import models
from django.contrib.auth.models import User
import boto3,io
# s3 = boto3.client('s3')

from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

from PIL import Image

from stazroute import settings


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
	bio = models.TextField(null=True, blank=True)
	twitter = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = str(self.first_name)
		if self.last_name:
			name += ' ' + str(self.last_name)
		return name

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1

			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = Post.objects.filter(slug=slug).exists()

			self.slug = slug
		super().save(*args, **kwargs)
		# # Open the thumbnail image using PIL
		# img_path = self.thumbnail.url
		#
		# # Read the image from S3
		# s3_response = s3.get_object(Bucket='stazroute-portfolio-personal', Key=img_path)
		# image_content = s3_response['Body'].read()
		#
		# # Open the image using Pillow
		# img = Image.open(io.BytesIO(image_content))
		#
		# # Resize the image
		# img = img.resize((640,360))
		#
		# # Save the resized image to a buffer
		# buffer = io.BytesIO()
		# img.save(buffer, format='JPEG')
		# buffer.seek(0)
		#
		# # Upload the resized image to S3
		# s3.put_object(Bucket='stazroute-portfolio-personal', Key='resized/' + image_path, Body=buffer.getvalue())



class PostComment(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.body

	@property
	def created_dynamic(self):
		now = timezone.now()
		return now
	