class Pipe {
    constructor() {
        let spacing = 150;
        this.top = random(height / 6, 3 / 4 * height);
        this.bottom = height - (this.top + spacing);
        this.x = width;
        this.w = 80;
        this.speed = 3;
        this.beenhit = false;
    }

    show() {
        fill('green');
        if (this.beenhit) {
            fill(255, 0, 0);

        }

        rect(this.x, 0, this.w, this.top);
        rect(this.x, height - this.bottom, this.w, this.bottom);
    }

    update() {
        this.x -= this.speed;
    }
    offscreen() {
        if (this.x < -this.w) return true;
        else return false;
    }

    hit(bird) {
        if ((bird.y - 16) <= this.top || (bird.y + 16) >= (height - this.bottom)) {
            if ((bird.x + 16) >= this.x && (bird.x - 16) <= (this.x + this.w)) {
                this.beenhit = true;
                return true;
            }
        }
        this.beenhit = false;
        return false;
    }

    
}
