from typing import Union

from tests.fakes_example.fakes import FakeCategoryRepository
from tests.repositories import CategoryRepository


def fill_categories(cat_repo: Union[CategoryRepository, FakeCategoryRepository], categories: list):
    for category in categories:
        if len(category['category_name']) > 2:
            cat_repo.add_category(**category)
