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


## Deploy del Chatbot con n8n

1. En n8n, cree las credenciales **"Meta API"** de tipo *Header Auth* (cabecera `Authorization` con valor `Bearer <tu_token>`) y **"OpenAI API"** de tipo *Header Auth* (cabecera `Authorization` con valor `Bearer <tu_api_key>`).
2. Importe el archivo `n8n/chatbot_whatsapp_ranwey.json` desde la interfaz de n8n mediante la opci\u00f3n *Import from file*.
3. Configure en Facebook Developers la URL del webhook que indica el nodo *Webhook* del flujo (por ejemplo `https://<tu_n8n>/webhook/whatsapp`) para WhatsApp, Facebook e Instagram.
4. Dentro del workflow ubique la variable `whatsapp:+YOUR_WHATSAPP_NUMBER` y reempl\u00e1cela por su n\u00famero verificado de Meta.

El repositorio incluye el script `scripts/deploy_workflow.sh` para importar o exportar el flujo v\u00eda API. Use `npm run n8n:import` o `npm run n8n:export` seg\u00fan corresponda.
