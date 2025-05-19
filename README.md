# chatbotR

Ejemplo de chatbot en Python que se conecta con WooCommerce utilizando su API REST. Permite consultar productos, pedidos y crear nuevas órdenes desde una interfaz de línea de comandos.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el chatbot, defina las siguientes variables de entorno con las credenciales de su tienda WooCommerce:

- `WC_URL` – URL base de la tienda (por ejemplo `https://mitienda.com`)
- `WC_CK` – Consumer Key
- `WC_CS` – Consumer Secret

## Uso

Ejecute el script `chatbot.py`:

```bash
python chatbot.py
```

El programa iniciará un pequeño chat en consola donde podrá solicitar:

- Listar productos escribiendo alguna frase que contenga "producto".
- Consultar pedidos existentes escribiendo algo que contenga "pedido".
- Crear un nuevo pedido escribiendo "comprar" o "nuevo pedido"; el bot pedirá el identificador del producto y la cantidad.

Escriba `salir` para terminar la conversación.

Este ejemplo es una base simple que puede ampliarse para integrarse en otras plataformas de chat o incorporar más lógica conversacional.
