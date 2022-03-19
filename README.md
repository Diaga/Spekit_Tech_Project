# Shared Document Store Backend

As part of the hiring process, we would like you to attempt a time-boxed coding challenge project, focused on a RESTful
API service rapid prototype development. In this challenge, you are to create an API that stores “digital documents” in
“folders”. Folders or Documents can have one or many associated “Topics”, with short & long-form descriptors.

**Docs**: Please view [docs](docs/README.md) folder to read about design and development decisions.

## Getting Started

Before proceeding, make sure to create a `.env` file templating form `.env.template`
file and fill the empty values.

### Setup using virtualenv

**Note**: This method requires that Python 3.9 and Postgres have been installed on
your machine.

1. Create virtualenv using the below command:

```shell
$ virtualenv venv
```

2. Install requirements

```shell
$ pip install -r requirements.txt
```

3. Test server.

```shell
$ cd src
$ python manage.py test
```

4. Run server. The development server should be live at localhost:8000.

```shell
$ python manage.py runserver
```

### Setup using docker compose

1. Install docker using the [official documentation](https://docs.docker.com/get-docker/)
2. Use the following command to run tests using docker compose:

```shell
$ docker compose -f docker-compose.test.yaml up
```

3. Use the following command to run server. The development server should be live at localhost:8000.

```shell
$ docker compose up
```

### Optional Steps
#### Migration
Run migrations using the following command if not done already:
```shell
$ python manage.py migrate
```

#### Seeding
In case sample data is required, it can be seeded through the following command:
```shell
$ python manage.py seed v1
```

## Contributing

Please read [CONTRIBUTING](CONTRIBUTING.md) to learn how to contribute to the repository.

## License

[MIT](LICENSE)