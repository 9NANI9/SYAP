import Product from './Product.js'

let product = new Product()

const name = document.getElementById('name')
const price = document.getElementById('price')
const currancy = document.getElementById('currancy')
const imgLink = document.getElementById('imgLink')
const submit = document.getElementById('submit')


// Находим все div элементы на странице
const divElements = document.querySelectorAll('div');

// Проходимся по каждому div элементу

let buybutton = document.getElementById('buybutton');

buybutton.addEventListener('click', () => {
  const divElements = document.querySelectorAll('div.product'); // Получаем все div элементы на странице

  divElements.forEach((divElement) => {
    const buttonElement = divElement.querySelector('button');
    if (buttonElement && buttonElement.classList.contains('delbutton')) {
      divElement.remove();
    }
  });
});
// product.massiv = JSON.parse(localStorage.getItem('product')) || [];
// for (let item of product.massiv) {
//     console.log("ПРОВЕРКА")
//     console.log(item.name, item.price, item.currency, item.img);
//   }

// const massivCopy = [...product.massiv];
// console.log("JOPJOPA  "+massivCopy)
// for (let item of massivCopy) {
//   console.log("JOPA");
//   console.log(item.name, item.price, item.currency, item.img);
//   product.create(item.name, item.price, item.currency, item.img);
// }
submit.addEventListener('click', () => {
    let options = document.getElementsByName('currancy')
    let option_value
      for (let opt of options) {
        if(opt.checked){
          option_value = opt.value;
          break;
        }
      }
      product.create(name.value, price.value, option_value, imgLink.value)
  })


product.create('Телефон', '100000', '$', 'https://content2.onliner.by/catalog/device/header/ac009f440515d5e17988887f0786495d.jpg')
product.create('Ноутбук', '1500', '$', 'https://content.onliner.by/news/1100x5616/912aa88adccb90e0707ba11964a94a16.jpeg')
//console.log(product)






// let product = document.createElement('div');
// let product_name = document.createElement('h4');
// product_name.textContent = 'JOPA'
// let product_img = document.createElement('img')
// product_img.src = 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Macaca_nigra_self-portrait_large.jpg'
// product_img.height = '200'
// product.append(product_name, product_img);

// document.body.append(product);