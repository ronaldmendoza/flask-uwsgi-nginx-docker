## Supported tags and respective `Dockerfile` links

* [`python3.7.7`, `latest` _(Dockerfile)_](https://github.com/ronaldmendoza/flask-uwsgi-nginx-docker/blob/master/python3.7/Dockerfile)
# uwsgi-nginx-flask

**Docker** image with **uWSGI** and **Nginx** for **Flask** web applications in **Python 3.7**.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Flask**](http://flask.pocoo.org/) web applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

The combination of uWSGI with Nginx is a [common way to deploy Python Flask web applications](http://flask.pocoo.org/docs/1.0/deploying/uwsgi/). It is widely used in the industry and would give you decent performance. (*)

**GitHub repo**: [https://github.com/ronaldmendoza/flask-uwsgi-nginx-docker](https://github.com/ronald.mendoza/flask-uwsgi-nginx-docker)
**Docker Hub image**: [https://hub.docker.com/r/rontype1/flask-uwsgi-nginx/](https://hub.docker.com/r/rontype1/flask-uwsgi-nginx/)

```Dockerfile
FROM rontype1/flask-uwsgi-nginx:latest
COPY ./app /app
```

This Docker image is based on [**rontype1/uwsgi-nginx**](https://hub.docker.com/r/rontype1/uwsgi-nginx/). That Docker image has uWSGI and Nginx installed in the same container and was made to be the base of this image.
