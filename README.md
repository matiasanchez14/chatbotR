# chatbotR

Ejemplo de integraci\u00f3n con WooCommerce pensado para ser utilizado por ChatGPT u otras aplicaciones que consuman una API. Permite buscar productos, consultar pedidos y crear nuevas \u00f3rdenes.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

Instalaci\u00f3n de dependencias:

```bash
pip install -r requirements.txt
```

## Configuraci\u00f3n

Defina las siguientes variables de entorno con las credenciales de su tienda WooCommerce:

- `WC_URL` – URL base de la tienda (por ejemplo `https://mitienda.com`)
- `WC_CK` – Consumer Key
- `WC_CS` – Consumer Secret

## Uso

Inicie la API con `uvicorn`:

```bash
uvicorn app:app --reload
```

Los puntos finales disponibles son:

- `GET /products` para buscar productos por `search`, `product_id` o `category`.
- `GET /orders` para obtener pedidos filtrando por `user_id` o `order_id`.
- `POST /create_order` para crear un pedido nuevo enviando un JSON con los datos.

Cada respuesta es un JSON apto para ser consumido por ChatGPT u otro frontend.

