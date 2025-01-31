// Data Types in JavaScript

// 1 ----- Number ----
const instanceCount = 3;
const cpuUtilization = 0.75;

console.log(typeof instanceCount); // Outputs: number
console.log(typeof cpuUtilization); // Outputs: number

// 2 ----- String ----
const region = 'us-east-1';
const errorMessage = 'An error occurred';
const logEntry = 'Deployment failed in ${region}: ${erromessage}';

console.log(typeof region); // outputs: string

// 3 ----- Boolean ----
const isDeployed = true;
const isRunning = false;

console.log(typeof isDeployed); // outputs: boolean

if (isDeployed && !isRunning) {
    console.log ("Running in production mode");
}

// 4 ---- undefined ----
let configFile;
console.log(typeof configFile); // outputs: undefined

if (configFile === undefined) {
    console.log("No config file provided");
     // load config file here
}

// 5 ---- null ----
const cacheResult = null;
console.log(typeof cacheResult); // outputs: object (this is a know JavaScripts quirk)

if (cacheResult === null) {
    console.log("Cache is empty");
    // fetch data from database
}

// 6 --- Object Literals ---
const ec2Instance = {
    instanceId: 'i-123456789abcde',
    instanceType: 't2.micro',
    region: 'us-east-1',
    status: 'running'
};

console.log(typeof ec2Instance); // Outputs: object
console.log(ec2Instance.instanceType); // Outputs: t2.micro

// 7 ---- Array ----
const instanceIds = ['i-123456789abcde', 'i-987654321fedcb'];
console.log(typeof instanceIds); // Outputs: object
console.log(Array.isArray(instanceIds)); // Outputs: true
