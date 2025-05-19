import os
from typing import Any, Dict, List, Optional
from woocommerce import API


def create_client() -> API:
    """Create a WooCommerce client from environment variables."""
    url = os.getenv("WC_URL")
    ck = os.getenv("WC_CK")
    cs = os.getenv("WC_CS")
    if not (url and ck and cs):
        raise RuntimeError(
            "Se requieren las variables de entorno WC_URL, WC_CK y WC_CS"
        )
    return API(url=url, consumer_key=ck, consumer_secret=cs, version="wc/v3", timeout=15)


def search_products(
    wcapi: API,
    name: Optional[str] = None,
    product_id: Optional[int] = None,
    category: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Return a list of products that match the search criteria."""
    params: Dict[str, Any] = {}
    endpoint = "products"

    if product_id is not None:
        endpoint = f"products/{product_id}"
    else:
        if name:
            params["search"] = name
        if category:
            params["category"] = category

    response = wcapi.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        # Single product returns a dict, ensure list
        return data if isinstance(data, list) else [data]
    raise RuntimeError(f"Error al buscar productos: {response.text}")


def get_orders(
    wcapi: API,
    user_id: Optional[int] = None,
    order_id: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """Return a list of orders filtered by user or a specific order ID."""
    params: Dict[str, Any] = {}
    endpoint = "orders"

    if order_id is not None:
        endpoint = f"orders/{order_id}"
    if user_id is not None:
        params["customer"] = user_id

    response = wcapi.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        return data if isinstance(data, list) else [data]
    raise RuntimeError(f"Error al obtener pedidos: {response.text}")


def create_order(wcapi: API, order_data: Dict[str, Any]) -> Dict[str, Any]:
    """Create an order with the provided data."""
    if not order_data.get("line_items"):
        raise ValueError("El pedido debe incluir 'line_items'")

    response = wcapi.post("orders", order_data)
    if response.status_code in (200, 201):
        return response.json()
    raise RuntimeError(f"Error al crear el pedido: {response.text}")
