// --- Basic Functions ---

function sayHello() {
    console.log("Hello, Cloud Engineer!");
}

// ---- Calling function
sayHello();

// ---- Function Parameters ---

function deployToRegion(region) {
    console.log("Deploying to region: " + region);

}

// ---- Calling Function with Parameters ---
deployToRegion("us-west-1");


function configureService(serviceName, tier) {
    console.log("Configuring " + serviceName + " service with tier: " + tier);
}

configureService("EC2", "t2.micro")
configureService("Lambda", "t3.small")