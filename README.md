
## Getting Started
Follow the steps below to get started with the Django Portfolio Website:

Install the requirements by running the following command in your terminal:

'''pip install -r requirements.txt'''

1 - Start the development server on port 8000:
'''python manage.py runserver'''

This will start the server and you can access the website at http://127.0.0.1:8000/.

2 - Create a superuser account:

'''python manage.py createsuperuser'''

This command will prompt you to enter a username, email, and password for the superuser account. This account will allow you to access the admin panel of the website and add, edit, or delete your portfolio projects.

3 - Usage

The Django Portfolio Website comes with pre-built templates and views for showcasing your portfolio projects. You can customize the templates or views according to your needs.

To add a new project to your portfolio, log in to the admin panel at http://127.0.0.1:8000/admin/ using the superuser account you created earlier. From here, you can add a new project by clicking on the "Add" button in the "Projects" section.

To edit or delete an existing project, click on the project name in the "Projects" section and make the necessary changes.





You can also customize the appearance of the website by modifying the CSS and HTML files in the "static" and "templates" folders respectively.

## Contributing
If you would like to contribute to the Django Portfolio Website, please create a new branch and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License
The Django Portfolio Website is licensed under the MIT license. See the LICENSE file for more details.