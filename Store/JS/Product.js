import Button from './Button.js'
import { startRotate,stopRotate } from './3d.js'

export default class Product {

  
  constructor() {
    this.massiv = JSON.parse(localStorage.getItem('product')) || [];
    this.buttonfab = new Button();
    this.cart = JSON.parse(localStorage.getItem('cart')) || [];
    // this.cart =[];
  }
  
  create(name, price, currancy, img) {
    let product = document.createElement('div');
    product.className = 'product';
    product.addEventListener('mousemove',startRotate)
    product.addEventListener('mouseout',stopRotate)
    // Создание дополнительного div
    let additionalDiv = document.createElement('div');
    additionalDiv.className = 'additional-div';
    
    let productName = document.createElement('h3');
    productName.innerText = `${name}`;
    
    let productPrice = document.createElement('p');
    productPrice.innerText = `${price}${currancy}`;
    
    let image = document.createElement('img');
    image.src = `${img}`;
    image.className = 'product-image';
    
    let button = document.createElement('button');
    button.innerHTML = '&#10006;';
    button.className = 'delete';
    
    
    additionalDiv.appendChild(image);
    additionalDiv.appendChild(productName);
    additionalDiv.appendChild(productPrice);
    additionalDiv.appendChild(button);
      
   
    product.appendChild(additionalDiv);

    button.addEventListener('click',()=> {
        let card = button.parentElement;
        let container = card.parentElement;
        this.remove(name, price, currancy, img)
        this.removeFromCart(name, price, currancy, img)
        container.removeChild(card);
    })

    let addButton=this.buttonfab.createButton('Добавить в корзину')
    additionalDiv.appendChild(addButton);
    addButton.addEventListener('click', () => {
      
      if (addButton.innerText == 'Добавить в корзину') {
      addButton.innerText = 'Убрать из корзины'
      addButton.className='delbutton'
      const cartData = {
        name: name,
        price: price,
        currancy: currancy,
        img: img
    };
    this.cart.push(cartData)
    localStorage.setItem('cart', JSON.stringify(this.cart));
      }
      else {
      addButton.innerText = 'Добавить в корзину'
      addButton.className='addbutton'
      }
    })
  
    // product.append(image, productName, productPrice, addButton, button)
    document.getElementById('products').append(product)
  }

  save(name, price, currancy, img){
    const productData = {
          name: name,
          price: price,
          currancy: currancy,
          img: img
      };
    this.massiv.push(productData)
    // localStorage.clear()
    localStorage.setItem('product', JSON.stringify(this.massiv));
  }

  get_massiv(){
    return this.massiv
  }

  get_cart(){
    return this.cart
  }

  remove(name, price, currancy, img){

    const productToRemove = {
        name: name,
        price: price,
        currancy: currancy,
        img: img
    };

    const index = this.massiv.findIndex(product => (
      product.name === productToRemove.name &&
      product.price === productToRemove.price &&
      product.currency === productToRemove.currency &&
      product.img === productToRemove.img
    ));
    
    if (index !== -1) {
      this.massiv.splice(index, 1);
    }
    localStorage.removeItem('product');
    localStorage.setItem('product', JSON.stringify(this.massiv));
  }

  removeFromCart(name, price, currancy, img) {
    const productToRemove = {
      name: name,
      price: price,
      currancy: currancy,
      img: img
    };

    const index = this.cart.findIndex(
      (product) =>
        product.name === productToRemove.name &&
        product.price === productToRemove.price &&
        product.currancy === productToRemove.currancy &&
        product.img === productToRemove.img
    );

    if (index !== -1) {
      this.cart.splice(index, 1);
    }
    localStorage.removeItem('cart');
    localStorage.setItem('cart', JSON.stringify(this.cart));
  }

  count_total(mas)
  {

    let total_cost={
      dollar:0,
      euro:0,
      ruble:0
    }
   
      mas.forEach(element => {
        console.log("RABOTEAM")
        if (element.currancy == "$")
          total_cost.dollar += parseFloat(element.price);
        if (element.currancy == "€")
          total_cost.euro += parseFloat(element.price);
        if (element.currancy == "₽")
          total_cost.ruble += parseFloat(element.price);
      });
     
  
  console.log("total_cost")
  console.log(total_cost)
  return total_cost
}
}
