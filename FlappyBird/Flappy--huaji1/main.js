// developed by chris
let totalPopulation = 400; //总个体数
let Birds = [];
let currentBirds = [];
let pipes = [];

let counter = 0;

// 控制组件
let speedSlider;
let speedSpan;
let highScoreSpan;
let allTimeHighScoreSpan;
let birdSprite;
// 目前最高的分数，也代表目前最高适应度
let highScore = 0;

let runBest = false;
let runBestButton;

function preload() {
  birdSprite = loadImage('image/bird.png');
}

function setup() {
  let canvas = createCanvas(600, 400);
  canvas.parent('container');

  // 获取当前页面的元素
  speedSlider = select('#speedSlider');
  speedSpan = select('#speed');
  highScoreSpan = select('#hs');
  allTimeHighScoreSpan = select('#ahs');
  runBestButton = select('#best');
  runBestButton.mousePressed(runTheBest);

  // 按照最大个体数创建个体
  for (let i = 0; i < totalPopulation; i++) {
    let bird = new Bird();
    currentBirds[i] = bird;
    Birds[i] = bird;
  }
}

// 是否选择只训练当前做的最好的鸟
function runTheBest() {
  runBest = !runBest;
  if (runBest) {
    resetGame();
    runBestButton.html('继续训练群体');

  } else {
    nextGeneration();
    runBestButton.html('最优个体');
  }
}

function draw() {
  background('Azure');

  // 加速与否？
  let cycles = speedSlider.value();
  speedSpan.html(cycles);


  // 加速的倍数
  for (let n = 0; n < cycles; n++) {
    for (let i = pipes.length - 1; i >= 0; i--) {
      pipes[i].update();
      if (pipes[i].offscreen()) {
        pipes.splice(i, 1);
      }
    }


    if (runBest) {
      bestBird.makePrediction(pipes);
      bestBird.update();
      for (let j = 0; j < pipes.length; j++) {
        if (pipes[j].hits(bestBird)) {
          resetGame();
          break;
        }
      }

      if (bestBird.bottomTop()) {
        resetGame();
      }
    }
    //训练所有鸟
    else {
      for (let i = currentBirds.length - 1; i >= 0; i--) {
        let bird = currentBirds[i];
        bird.makePrediction(pipes);
        bird.update();

        for (let j = 0; j < pipes.length; j++) {
          if (pipes[j].hits(currentBirds[i])) {
            currentBirds.splice(i, 1);
            break;
          }
        }

        if (bird.bottomTop()) {
          currentBirds.splice(i, 1);
        }

      }
    }

    // 调整管道横向间隔
    if (counter % 60 == 0) {
      pipes.push(new Pipe());
    }
    counter++;
  }

  // 本代最高分数
  let tempHighScore = 0;
  if (!runBest) {
    // 选出做的最好的鸟
    let tempBestBird = null;
    for (let i = 0; i < currentBirds.length; i++) {
      let s = currentBirds[i].score;
      if (s > tempHighScore) {
        tempHighScore = s;
        tempBestBird = currentBirds[i];
      }
    }


    if (tempHighScore > highScore) {
      highScore = tempHighScore;
      bestBird = tempBestBird;
    }
  } else {
 
    tempHighScore = bestBird.score;
    if (tempHighScore > highScore) {
      highScore = tempHighScore;
    }
  }

  // 实时更新分数
  highScoreSpan.html(tempHighScore);
  allTimeHighScoreSpan.html(highScore);

  for (let i = 0; i < pipes.length; i++) {
    pipes[i].show();
  }

  if (runBest) {
    bestBird.show();
  } else {
    for (let i = 0; i < currentBirds.length; i++) {
      currentBirds[i].show();
    }
    if (currentBirds.length == 0) {
      nextGeneration();
    }
  }
}