from typing import Any, Dict, List, Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from woocommerce_api import create_client, search_products, get_orders, create_order


app = FastAPI(title="WooCommerce ChatGPT Plugin")


def get_client():
    """Dependency that provides a WooCommerce API client."""
    return create_client()


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderRequest(BaseModel):
    line_items: List[OrderItem]
    billing: Optional[Dict[str, Any]] = None
    shipping: Optional[Dict[str, Any]] = None


@app.get("/products")
async def api_products(
    search: Optional[str] = None,
    product_id: Optional[int] = None,
    category: Optional[str] = None,
    client=Depends(get_client),
):
    """Search for products by name, ID or category."""
    try:
        products = search_products(
            client, name=search, product_id=product_id, category=category
        )
        return {"products": products}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/orders")
async def api_orders(
    user_id: Optional[int] = None,
    order_id: Optional[int] = None,
    client=Depends(get_client),
):
    """Retrieve orders by customer or specific ID."""
    try:
        orders = get_orders(client, user_id=user_id, order_id=order_id)
        return {"orders": orders}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/create_order")
async def api_create_order(
    order: OrderRequest,
    client=Depends(get_client),
):
    """Create a new order with the provided information."""
    try:
        # Convert OrderItem models to dicts expected by WooCommerce
        order_dict = order.dict()
        order_dict["line_items"] = [item.dict() for item in order.line_items]
        created = create_order(client, order_dict)
        return created
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
