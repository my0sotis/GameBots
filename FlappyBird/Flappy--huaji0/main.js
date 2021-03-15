var bird;
var pipes = [];
var count = -1;
function setup() {
    createCanvas(600, 600);
    bird = new Bird();
    pipes.push(new Pipe());
}
function draw() {
    background(5, 242, 255);
    bird.update();
    bird.show();

    if (frameCount % 215 == 0) {
        pipes.push(new Pipe());
        count++;
    }
    for (let i = pipes.length - 1; i >= 0; i--) {
        pipes[i].show();
        pipes[i].update();
        if (pipes[i].offscreen()) {
            pipes.splice(i, 1);
        }

        if (pipes[i].hit(bird)) {
            count = 0;
            console.log('Hit!!!');
        }

        if (!pipes[i].hit(bird)) {
            if ((bird.x - 16) > (pipes[i].x + pipes[i].w)) {
                bird.score = count;
                console.log('score: ' + bird.score);
                return true;
            }
        }
    }
}

function keyPressed() {
    if (key == ' ') {
        console.log('space');
        bird.up();
    }
}


// function bird_pass(pipe) {
//     if (!pipe.hit(bird)) {
//         if ((bird.x - 16) > (pipe.x + pipe.w)) {
//             bird.score++;
//             return true;
//         }
//     }
//     return false;
// }