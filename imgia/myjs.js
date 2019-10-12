// Initialize the Image Classifier method with MobileNet. A callback needs to be passed.
let classifier;

// A variable to hold the image we want to classify
let img;

function preload() {
    classifier = ml5.imageClassifier('MobileNet');
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.src = 'https://www.cnetfrance.fr/i/edit/2015/10/apple-imac-21.5-pouces-retina-4k-2015-770x577.jpg';
    img.width = 224;
    img.height = 224;
    // img = loadImage('https://www.cnetfrance.fr/i/edit/2015/10/apple-imac-21.5-pouces-retina-4k-2015-770x577.jpg');
}

function setup() {
    createCanvas(400, 400);
    classifier.classify(img, gotResult);
    image(img, 0, 0);
}

// A function to run when we get any errors and the results
function gotResult(error, results) {
// Display error in the console
if (error) {
    console.error(error);
} else {
    // The results are in an array ordered by confidence.
    console.log(results);
    createDiv('Label: ' + results[0].label);
    createDiv('Confidence: ' + nf(results[0].confidence, 0, 2));
}
}
