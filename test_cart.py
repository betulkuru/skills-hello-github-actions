from selenium import webdriver
from pages.search_page import SearchPage
from pages.cart_page import CartPage


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://demoblaze.com")

    # Laptops kategorisine git
    search_page = SearchPage(driver)
    search_page.select_laptops_category()

    # Bir ürünü seç ve sepete ekle
    cart_page = CartPage(driver)
    cart_page.select_product()  # Bu adımı kullanmayabilirsiniz, çünkü doğrudan butona tıklıyoruz
    cart_page.add_product_to_cart()

    # Sepete git ve doğrula
    cart_page.open_cart()
    assert cart_page.verify_cart(), "Sepette ürün bulunamadı!"

    driver.quit()
test_add_to_cart()