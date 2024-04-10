# Generated by Django 4.2.11 on 2024-04-01 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('about_subtitle', models.CharField(max_length=255)),
                ('about_content', models.TextField()),
                ('about_image', models.ImageField(upload_to='uploads/about_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '03. About',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/blogs_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '9. Blogs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.ImageField(upload_to='uploads/calendar')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('is_default', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '00. Calender',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '11. Contact',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/course_images/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '07. Courses',
            },
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '8. FAQs',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/gallery_images/')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '10. Gallery',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=255)),
                ('title_text', models.CharField(max_length=99)),
                ('sub_text', models.CharField(max_length=55)),
                ('button_text', models.CharField(max_length=20)),
                ('button_url', models.URLField()),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='uploads/hero_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '12. Home Content',
            },
        ),
        migrations.CreateModel(
            name='MessageFrom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/message_from_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '04. Message From',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/notice_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '14. Notices',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PopupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(default=None)),
                ('image', models.ImageField(blank=True, upload_to='uploads/popup_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '13. Popup Message',
            },
        ),
        migrations.CreateModel(
            name='SchoolSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='uploads/logos')),
                ('school_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('opening_hours', models.CharField(max_length=255)),
                ('map_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '01. School Setup',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=255)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedIn_url', models.URLField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '02. Social Media',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/team_images')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '05. Team Members',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/testimonial_images/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '06. Testimonials',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('number', models.IntegerField()),
                ('deadline', models.DateField()),
                ('desc', models.TextField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '15. Vacancy',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.blog')),
            ],
            options={
                'verbose_name_plural': '16. Comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
