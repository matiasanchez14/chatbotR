import os
from woocommerce import API


def create_client():
    """Crea el cliente de WooCommerce a partir de variables de entorno."""
    url = os.getenv("WC_URL")
    ck = os.getenv("WC_CK")
    cs = os.getenv("WC_CS")
    if not url or not ck or not cs:
        raise RuntimeError("Se requieren las variables de entorno WC_URL, WC_CK y WC_CS")
    return API(url=url, consumer_key=ck, consumer_secret=cs, version="wc/v3", timeout=15)


def list_products(wcapi):
    """Muestra una lista básica de productos."""
    response = wcapi.get("products")
    if response.status_code == 200:
        for p in response.json():
            print(f"{p['id']} - {p['name']} : {p['price']}")
    else:
        print("Error al obtener los productos", response.text)


def list_orders(wcapi):
    """Muestra los pedidos existentes."""
    response = wcapi.get("orders")
    if response.status_code == 200:
        for o in response.json():
            print(f"Pedido #{o['id']} - Estado: {o['status']}")
    else:
        print("Error al obtener los pedidos", response.text)


def create_order(wcapi, product_id, quantity):
    """Crea un nuevo pedido sencillo con un único producto."""
    data = {"line_items": [{"product_id": product_id, "quantity": quantity}]}
    response = wcapi.post("orders", data)
    if response.status_code in (200, 201):
        order = response.json()
        print(f"Pedido creado: #{order['id']}")
    else:
        print("Error al crear el pedido", response.text)


def main():
    try:
        wcapi = create_client()
    except RuntimeError as exc:
        print(exc)
        return

    print("Chatbot para WooCommerce\nEscriba 'salir' para terminar")
    while True:
        text = input("Cliente: ").strip().lower()
        if text == "salir":
            break
        elif "producto" in text:
            list_products(wcapi)
        elif "pedido" in text and "nuevo" not in text:
            list_orders(wcapi)
        elif "comprar" in text or "nuevo pedido" in text or "vender" in text:
            product_id = input("ID del producto: ")
            qty = input("Cantidad: ")
            try:
                create_order(wcapi, int(product_id), int(qty))
            except ValueError:
                print("Datos no válidos")
        else:
            print("Lo siento, no entiendo la consulta.")


if __name__ == "__main__":
    main()
