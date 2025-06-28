import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
import hashlib

# Page config
st.set_page_config(page_title="TechStore", page_icon="🛒", layout="wide")

# Sample product data with real images
PRODUCTS = {
    1: {
        'name': 'MacBook Pro 16"',
        'price': 2499.99,
        'description': 'M3 Pro chip, 18GB RAM, 512GB SSD',
        'category': 'Laptops',
        'stock': 10,
        'image_url': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp16-spacegray-select-202311?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1698696765011'
    },
    2: {
        'name': 'iPhone 15 Pro',
        'price': 999.99,
        'description': 'A17 Pro chip, 128GB, Pro camera',
        'category': 'Smartphones',
        'stock': 20,
        'image_url': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-model-unselect-gallery-1-202309?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1693346852625'
    },
    3: {
        'name': 'AirPods Pro',
        'price': 249.99,
        'description': 'ANC, spatial audio, MagSafe',
        'category': 'Audio',
        'stock': 35,
        'image_url': 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MWP22?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1591634795000'
    }
}

# Session state
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Functions
def add_to_cart(pid, qty):
    if pid in st.session_state.cart:
        st.session_state.cart[pid] += qty
    else:
        st.session_state.cart[pid] = qty

def cart_total():
    return sum(PRODUCTS[pid]['price'] * qty for pid, qty in st.session_state.cart.items())

def show_products():
    st.title("🛍️ Shop Products")
    cols = st.columns(2)
    for i, (pid, p) in enumerate(PRODUCTS.items()):
        with cols[i % 2]:
            st.image(p['image_url'], width=300)
            st.subheader(p['name'])
            st.write(p['description'])
            st.write(f"Price: ${p['price']} | Stock: {p['stock']}")
            qty = st.number_input(f"Qty for {p['name']}", 1, p['stock'], 1, key=f"qty_{pid}")
            if st.button(f"Add to Cart", key=f"add_{pid}"):
                add_to_cart(pid, qty)
                st.success(f"Added {qty} x {p['name']} to cart")

def show_cart():
    st.title("🛒 Your Cart")
    if not st.session_state.cart:
        st.info("Cart is empty.")
        return
    for pid, qty in st.session_state.cart.items():
        p = PRODUCTS[pid]
        st.image(p['image_url'], width=150)
        st.write(f"**{p['name']}** x {qty} = ${p['price'] * qty:.2f}")
    st.markdown(f"### Total: ${cart_total():.2f}")

def main():
    page = st.sidebar.selectbox("Navigate", ["Products", "Cart"])
    if page == "Products":
        show_products()
    elif page == "Cart":
        show_cart()

if __name__ == '__main__':
    main()

