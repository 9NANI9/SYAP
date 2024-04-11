import Product from './Product.js'

let product = new Product()

const massivCopy = product.get_cart()
for (let item of massivCopy) {
  product.create(item.name, item.price, item.currancy, item.img);
  const temp=document.querySelector(".addbutton")
  temp.remove()
}
const cost=product.count_total(massivCopy)
console.log(cost)

const labelDollar = document.querySelector('label[for="price-dollar"]');
labelDollar.textContent = cost.dollar+" $";

// Изменение значения метки для евро
const labelEuro = document.querySelector('label[for="price-euro"]');
labelEuro.textContent = cost.euro+"€ ";

// Изменение значения метки для рубля
const labelRuble = document.querySelector('label[for="price-ruble"]');
labelRuble.textContent = cost.ruble+"₽ ";