from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'porção',
        'preparation_steps': fake.text(3000),
        'create_at': fake.date_time(),
        'auth': {
            'first_name': fake.first_name(), 
            'last_name': fake.last_name(), 
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'http://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

