# CAPSTONE-PROJECT-Inventory-Management-API-
*DOCUMENTATION ON BUILDING INVENTORY MANAGEMENT API*

Project Name:  Inventory Management Api
Framework: Django + Django REST framework
Authentication: JWT(Json Web Token via rest_framework_simplejwt)
Database: Postresql(For project) and Sqlite(For Test).

1. Project started with creating a Git Repo for the project.
2. Then virtual environment was created with dependencies installed.
3. Project was created and project app as well.
4. Followed by models creations for each endpoints to see the relationships between each models.
5. Created serializers for the each models, where fields were handled also views where each viewset was created for the models.
6. Also created authentication and permissions using REST framework and JWT through rest_framework_simplejwt in views.
7. Nested routing was done for orderitem to be accessed through their parent orders using rest_framework_nested.
8. Ran migrations and created a superuser for admin.
9. Tested endpoints locally with localhost and with debug turned on.
10. Then proceeded to test using django REST framework APITestCase.
11. Encountered a couple of issues during testing but was able to debug with support of AI.
12. Five tests were ran and all were successful.
13. Proceeded to go live by deploying on PythonAnywhere, but had set back as Postgresql doesn't run on free mode. 
14. Tried deploying again on Heroku but was also meet with issues.
15. Finally created MySql database on PythonAnywhere for the project and ran migrations, though there were adjustments to settings.
16. Project is not live on PythonAnywhere and can be checked for testing on https://Ennymoney20.pythonanywhere.com.