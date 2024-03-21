import Button from './Button.js'

export default class Product {

  
  massiv = [];
  buttonfab= new Button();
  
  
  create(name, price, currancy, img) {
    let product = document.createElement('div')
    product.className = 'product'
    let productName  = document.createElement('h3')
    productName.innerText = `${name}`
    let productPrice = document.createElement('p')
    productPrice.innerText = `${price}${currancy}`
    let image = document.createElement('img')
    let button = document.createElement('button');
    button.innerHTML = '&#10006;';
    button.className = 'delete';
    image.src = `${img}`
    image.className = 'product-image'

    button.addEventListener('click',()=> {
       // Получаем родительский элемент (карточку)
  let card = button.parentElement;

  // Получаем родительский контейнер карточек
  let container = card.parentElement;

  // Удаляем карточку из контейнера
  container.removeChild(card);
    })

    let addButton=this.buttonfab.createButton('Добавить в корзину')
    // let addButton = document.createElement('button')
    // addButton.innerText = 'Добавить в корзину'
    // addButton.className='addbutton'
    addButton.addEventListener('click', () => {
      if (addButton.innerText == 'Добавить в корзину') {
      addButton.innerText = 'Убрать из корзины'
      addButton.className='delbutton'
      }
      else {
      addButton.innerText = 'Добавить в корзину'
      addButton.className='addbutton'
      }
    })
    

    product.append(image, productName, productPrice, addButton, button)
    
    document.getElementById('products').append(product)
    const productData = {
      name: name,
      price: price,
      currancy: currancy,
      img: img
    };
    this.massiv.push(productData)
    this.save(this.massiv)
    console.log(this.massiv)
    this.massiv=[]
   
    
  }

  save(prod){
    if (!localStorage.getItem('product')) {
      console.log("SAVEd")
      localStorage.setItem('product', JSON.stringify(prod));
    } else {
      prod = [];
    }
  }
}

