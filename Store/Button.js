export default class Button {
    constructor (width, height, text, color, textColor){
      this.width = width
      this.height = height
      this.text = text
      this.color = color
      this.textColor = textColor
    }
    createButton(tex) {
      const buttonElement = document.createElement('button')
      buttonElement.className = 'addbutton'
      buttonElement.style.width = this.width
      buttonElement.style.height = this.height
      buttonElement.style.backgroundColor = this.color
      buttonElement.innerText = tex
      buttonElement.style.color = this.textColor

      return buttonElement
    }

    setColor(color){
      this.color = color
    }
    setWidth(width){
      this.width = width
    }
    setHeight(height){
      this.height = height
    }
    setText(text){
      this.text = text
    }

}