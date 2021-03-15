function resetGame() {
  counter = 0;
  // 重置分数
  if (bestBird) {
    bestBird.score = 0;
  }
  pipes = [];
}

// 创建下一代
function nextGeneration() {
  resetGame();
  normalizeFitness(Birds);
  currentBirds = generate(Birds);
  Birds = currentBirds.slice();
}

function generate(oldBirds) {
  let newBirds = [];
  for (let i = 0; i < oldBirds.length; i++) {
    // 基于适应度选择一只鸟
    let bird = poolSelection(oldBirds);
    newBirds[i] = bird;
  }
  return newBirds;
}

//计算适应度
function normalizeFitness(birds) {

  for (let i = 0; i < birds.length; i++) {
    birds[i].score = pow(birds[i].score, 2);
  }


  let sum = 0;
  for (let i = 0; i < birds.length; i++) {
    sum += birds[i].score;
  }

  for (let i = 0; i < birds.length; i++) {
    birds[i].fitness = birds[i].score / sum;
  }
}


// 基于适应度选择一只鸟
function poolSelection(birds) {

  let index = 0;
  let r = random(1);
  while (r > 0) {
    r -= birds[index].fitness;
    index += 1;
  }
  index -= 1;

  return birds[index].copy();
}