# QA API Tests

API автотесты для тестового магазина [fakestoreapi.com](https://fakestoreapi.com).

## Технологии

- Python 3.11
- requests
- pytest

## Тесты

- `test_get_all_products` — проверка статуса 200 на список товаров
- `test_products_count` — проверка количества товаров (20)
- `test_get_single_product` — проверка структуры ответа (статус, id, поля title и price)
- `test_product_price` — проверка что цена > 0
- `test_nonexistent_product` — негативный тест (XFAIL — известный баг API)

## Запуск

```bash
py -m pytest -v
```