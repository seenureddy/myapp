How to deploy django app using Gunicorn :

	To install gunicorn on your local machine use 

		pip install gunicorn==version    #version=19.1

	There are different procedure to run gunicorn some create bash script, some run using the following command 

		gunicorn djangoappname.wsgi:application  # for this project djangoappname = myapp

	if localprot is busy on your local machine, you can bind so port address

	    gunicorn myapp.wsgi:application --bind=127.0.0.1:8001 #Here i use 8001 you can change

# Nginx acts as a reverse proxy here. All our request will initially come to nginx. It's for nginx to 
# decide what requests it wants to serve and what requests it wants to pass to some other server.
# In our case, we want nginx to serve requests for static resources and to pass any other request to 
# gunicorn.

In this project to deploy static files we use Nginx:

    To install nginx on your local machine use

		sudo apt-get install nginx==version        # version=16.1

	We need to tell nginx the location of our static resources and for that we need to make sure all our static resources are at a single location

		STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')

	Run collectstatic:

		python manage.py collectstatic

		You should see that a directory staticfiles gets created at the same level as manage.py

	Create a file /etc/nginx/sites-enabled/example and add following content to it.

		server {
			
			listen localhost:8000;

			location / {
				proxy_pass httP://127.0.0.1:8001;
			}

			location /static/ {

				autoindex on;
				# alias "The static files path on your local machine"
				alias /home/seenu/Agiliq/app/myapp/staticfiles/;
			}

		}

	Make sure nginx is running:

		sudo services nginx restart


Depoly on a publically acessible server:

	I will use domain example.com for illustration

	We don't need any change for gunicorn and can run it in the same way:

		gunicorn myapp.wsgi:application --bind==127.0.0.1:8001

	Already created file /etc/nginx/sites-enabled/example on the server and add content:

		Server{

			listen 80;
			server_name: example.com
		}

	After setting server_name you need add some content hosts in /etc/ file :

		127.0.0.1 example.com

	With this, gunicorn runs as a background process and we can quit from the server without affecting gunicorn.

		gunicorn myapp.wsgi:application --bind==127.0.0.1:8001 --deamon


<!-- How to deploy django app on heroku :
 
 	To interact with heroku command line install following 
 
 	pip install heroku-toolbelt
 
 	pip install django-toolbelt 
 
 	pip freeze > requirments/heroku.txt
 
 	ssh-keygen -t rsa
 
 	heroku login 
 
 	foreman start
 
 	heroku keys
     
     heroku keys:add
 
 	heroku create myapp 
     
     heroku apps:create mydjapp
 
     heroku unlock --app myapp
 
     heroku list
 
 	git remote add heroku git@heroku.com:mydjapp.git
     
     git remote -v
 
     reuirements.txt file should be in manage.py folder
 
     heroku logs -t 
      
 	heroku run python manage.py syncdb
 
 	heroku ps:scale web=1
  
 	heroku config:set DJANGO_SETTINGS_MODULE=myapp.config.settings_heroku
  --> 


