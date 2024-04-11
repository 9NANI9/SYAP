var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

let score = 0;
let lives = 3;
//ШАРИК
var x = canvas.width / 2;
var y = canvas.height-300;
var dx = 2;
var ballRadius = 30;

//ДРОТИК
var paddleHeight = 60;
var paddleWidth = 6;
var paddleX = (canvas.width - paddleWidth) / 2;
var paddleY=canvas.height - paddleHeight;

var rightPressed = false;
var leftPressed = false;
var throwPressed=false;

function drawBall() {
  ctx.beginPath();
  ctx.arc(x, y, ballRadius, 0, Math.PI * 2);

  
  var gradient = ctx.createRadialGradient(x, y, ballRadius, x, y, ballRadius * 0.2);
  gradient.addColorStop(0, "#ffffff"); 
  gradient.addColorStop(0.2, "#c86b85");
  gradient.addColorStop(1, "#ffffff");

  ctx.fillStyle = gradient;
  ctx.fill();
  ctx.closePath();
}
function drawLives() {
  ctx.font = "16px Arial";
  ctx.fillStyle = "#e6a4b4";
  ctx.fillText(`Lives: ${lives}`, canvas.width - 65, 20);
}

function drawPaddle() {
  ctx.beginPath();
  ctx.rect(paddleX, paddleY, paddleWidth, paddleHeight);
  ctx.fillStyle = "#e6a4b4";
  ctx.fill();
  ctx.closePath();
} 

function drawScore() {
  ctx.font = "16px Arial";
  ctx.fillStyle = "#e6a4b4";
  ctx.fillText(`Score: ${score}`, 8, 20);
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawBall();
  drawPaddle();
  drawScore();
  drawLives();
  
  
  if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
      dx = -dx;
  }

  if(rightPressed && paddleX < canvas.width-paddleWidth) {
      paddleX += 7;
  }
  else if(leftPressed && paddleX > 0) {
      paddleX -= 7;
  }
  else if(throwPressed ) {
    if(paddleY>-60){
    paddleY-= 7;
    }
    collisionDetection()
}
  
  x += dx;
}



function collisionDetection() {
  if(paddleY===62){
    if (paddleX < ballRadius+x && paddleX>x-ballRadius) {
      score++
      reset()
  }
  else{
    lives--;
if (!lives) {
  alert("GAME OVER");
  document.location.reload();
  // clearInterval(interval); // Needed for Chrome to end game
} else {
  reset()
  }
  }
}
}



document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("click", ThrowHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
document.addEventListener("mousemove", mouseMoveHandler, false);


function ThrowHandler(){
  throwPressed = true;
}

function keyDownHandler(e) {
  if (e.keyCode == 39) {
    rightPressed = true;
  } else if (e.keyCode == 37) {
    leftPressed = true;
  }
  else if (e.keyCode == 38) {
    throwPressed = true;
  }
}

function keyUpHandler(e) {
  if (e.keyCode == 39) {
    rightPressed = false;
  } else if (e.keyCode == 37) {
    leftPressed = false;
  }
  else if (e.keyCode == 38) {
    throwPressed = true;
  }
}

function mouseMoveHandler(e) {
  var relativeX = e.clientX - canvas.offsetLeft;
  if(relativeX > 0 && relativeX < canvas.width && !throwPressed) {
    paddleX = relativeX - paddleWidth/2;
  }
}

function reset(){
 paddleHeight = 60;
 paddleWidth = 6;
 paddleX = (canvas.width - paddleWidth) / 2;
 paddleY=canvas.height - paddleHeight;
 throwPressed=false;
}

var interval = setInterval(draw, 10);
