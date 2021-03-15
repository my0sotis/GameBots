class Pipe {
  constructor() {
    let spacing = 125;   //上下管子之间的间隙
    let centery = random(spacing, height - spacing);  //确定空隙的位置

    this.top = centery - spacing / 2;   //管子的位置
    this.bottom = height - (centery + spacing / 2);
    this.x = width;   //从最右边开始移动
    this.w = 80;
    this.speed = 6;
  }

  // 检测鸟是否撞到柱子
  hits(bird) {
    if ((bird.y - bird.r) < this.top || (bird.y + bird.r) > (height - this.bottom)) {
      if (bird.x > this.x && bird.x < this.x + this.w) {
        return true;
      }
    }
    return false;
  }

  // 画出管子
  show() {
    stroke(255);
    fill('green');
    rect(this.x, 0, this.w, this.top);
    rect(this.x, height - this.bottom, this.w, this.bottom);
  }

  // 更新管子位置
  update() {
    this.x -= this.speed;
  }

  // 判断管子是否移出屏幕
  offscreen() {
    if (this.x < -this.w) {
      return true;
    } else {
      return false;
    }
  }
}