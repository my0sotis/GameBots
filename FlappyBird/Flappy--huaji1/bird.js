function mutate(x) {  //产生变异
  if (random(1) < 0.1) {
    let offset = randomGaussian() * 0.5;
    let newx = x + offset;
    return newx;
  } else {
    return x;
  }
}

class Bird {
  constructor(neuronet) {
    this.x = 64;
    this.y = height / 2;
    this.r = 12;

    this.gravity = 0.8;
    this.lift = -12;
    this.velocity = 0;
    this.icon = birdSprite;
    if (neuronet instanceof NeuralNetwork) {
      this.neuronet = neuronet.copy();
      this.neuronet.mutate(mutate);
    } else {
      this.neuronet = new NeuralNetwork(5, 8, 2);
    }


    this.score = 0; // 活得越长，分数越高
    this.fitness = 0; //所获得的分数进行处理后即是适应度
  }


  copy() {
    return new Bird(this.neuronet);
  }

  // 画出鸟
  show() {
    //fill(100, 100);
    imageMode(CENTER);
    image(this.icon, this.x, this.y, this.r * 2, this.r * 2);
    

    //ellipse(this.x, this.y, this.r * 2, this.r * 2);
  }

  // 做出预测动作
  makePrediction(pipes) {

    let frontPipe = null;  //找最近的管道
    let record = Infinity;
    for (let i = 0; i < pipes.length; i++) {
      let distance = pipes[i].x - this.x;
      if (distance > 0 && distance < record) {
        record = distance;
        frontPipe = pipes[i];
      }
    }

    if (frontPipe != null) {

      let inputs = [];
      //定义输入
      inputs[0] = map(frontPipe.x, this.x, width, 0, 1);
      inputs[1] = map(frontPipe.top, 0, height, 0, 1);
      inputs[2] = map(frontPipe.bottom, 0, height, 0, 1);
      inputs[3] = map(this.y, 0, height, 0, 1);
      inputs[4] = map(this.velocity, -5, 5, 0, 1);

      // 从神经网络中获得输出
      let action = this.neuronet.predict(inputs);
      if (action[1] > action[0]) {
        this.up();
      }
    }
  }

  // 跳高
  up() {
    this.velocity += this.lift;
  }

  //碰触上面或者地面就判定死亡
  bottomTop() {
    return (this.y > height || this.y < 0);
  }

  // 更新鸟的位置和速度及分数
  update() {
    this.velocity += this.gravity;
    this.y += this.velocity;
    this.score++;
  }
}
