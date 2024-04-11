// Класс Product
class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }

    render() {
        const catalog = document.getElementById('catalog');

        const productElement = document.createElement('div');
        productElement.innerHTML = `<h3>${this.name}</h3><p>Цена: $${this.price}</p>`;

        catalog.appendChild(productElement);
    }
}

// Класс Button
class Button {
    constructor(text, onClick) {
        this.text = text;
        this.onClick = onClick;
    }

    render() {
        const catalog = document.getElementById('catalog');

        const buttonElement = document.createElement('button');
        buttonElement.textContent = this.text;
        buttonElement.addEventListener('click', this.onClick);

        catalog.appendChild(buttonElement);
    }
}

// Создание экземпляров классов и добавление на страницу
const product1 = new Product('Товар 1', 10.99);
product1.render();

const product2 = new Product('Товар 2', 19.99);
product2.render();

const addButton = new Button('Добавить товар', () => {
    const productName = prompt('Введите название товара:');
    const productPrice = parseFloat(prompt('Введите цену товара:'));

    const newProduct = new Product(productName, productPrice);
    newProduct.render();
});
addButton.render();