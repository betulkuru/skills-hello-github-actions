from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_link = (By.CLASS_NAME, "card-title")  # Ürün başlığı
        self.add_to_cart_button = (By.XPATH, "//a[@onclick='addToCart(8)']")  # Doğru XPath
        self.cart_link = (By.ID, "cartur")  # Sepet bağlantısı
        self.cart_items = (By.CLASS_NAME, "success")  # Sepetteki öğeler

    def select_product(self):
        # Ürüne tıklayın
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_link)
        )
        product.click()

    def add_product_to_cart(self):
        # Add to cart butonuna tıklayın
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_button.click()

    def open_cart(self):
        # Sepete git
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart_link.click()

    def verify_cart(self):
        # Sepetteki ürünleri kontrol edin
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_items)
        )
        return len(items) > 0
