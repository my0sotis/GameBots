// let birdSpite = loadImage('image/bird.png');

class Bird {
    constructor() {
        this.y = height / 2;
        this.x = 200;
        this.gravity = 1;
        this.lift = -24;
        this.velocity = 0;
        this.score = 0;

    }
    show() {
        // ellipse(this.x, this.y, 16, 16);
        fill(254);
        ellipse(this.x, this.y, 32, 32);
    }
    update() {
        this.velocity += this.gravity;
        this.velocity *= 0.9
        this.y += this.velocity;


        if (this.y > height) {  //不能超出下界
            this.y = height;
            this.velocity = 0;
        }
        if (this.y < 0) {   //不能超出上界
            this.y = 0;
            this.velocity = 0;
        }
    }  
    up() {
    this.velocity += this.lift;
    }
}
