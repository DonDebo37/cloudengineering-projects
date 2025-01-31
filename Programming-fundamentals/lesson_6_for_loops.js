// --- For Loops -----
let regions = ["us-west-1", "us-east-1", "eu-west-2", "eu-east-1"];

for (let i = 0; i < regions.length; i++) {
    console.log("Deploying to region: " + regions[i]);
}

// ---- Exercise ---

// Array of cloud services
const cloudServices = ["EC2", "S3", "Lambda", "DynamoDB"];

for (let i = 0; i < cloudServices.length; i++) {
    console.log("Deploying " + cloudServices[i] + " service");
}

// ---- Exercise ---