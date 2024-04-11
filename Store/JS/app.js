import Product from './Product.js'

let product = new Product()


const name = document.getElementById('name')
const price = document.getElementById('price')
const currancy = document.getElementById('currancy')
const imgLink = document.getElementById('imgLink')
const submit = document.getElementById('submit')


const divElements = document.querySelectorAll('div');

// Проходимся по каждому div элементу
let buybutton = document.getElementById('buybutton');

const massivCopy = product.get_massiv()
for (let item of massivCopy) {
  product.create(item.name, item.price, item.currancy, item.img);
}

// buybutton.addEventListener('click', () => {
//   const divElements = document.querySelectorAll('div.product'); // Получаем все div элементы на странице

//   divElements.forEach((divElement) => {
//     const buttonElement = divElement.querySelector('button');
//     if (buttonElement && buttonElement.classList.contains('delbutton')) {
//       divElement.remove();
//     }
//   });
// });


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
      product.save(name.value, price.value, option_value, imgLink.value)
  })


product.create('Телефон', '100000', '$', 'https://content2.onliner.by/catalog/device/header/ac009f440515d5e17988887f0786495d.jpg')
product.create('Ноутбук', '1500', '$', 'https://content.onliner.by/news/1100x5616/912aa88adccb90e0707ba11964a94a16.jpeg')







