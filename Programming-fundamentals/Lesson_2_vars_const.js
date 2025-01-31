// variables Const
const API_ENDPOINT = 'https://api.mycloud.com/v1';
console.log(API_ENDPOINT); // Outputs: https://api.mycloud.com/v1

// API_ENDPOINT = 'https://api.mycloud.com/v2'; // This would throw an error because it has been changed

// ---- Configuration Management ----
const AWS_REGION = 'us-east-1';
const MAX_RETRIES = 3;
const DYNAMODB_TABLE = 'USERS'

function fetchUserData(userId) {
    // Use these Constants in your AWS SDK calls

}

// ---- Security ----
const API_KEY = process.env.API_KEY;
API_KEY = 'new-key'; // This would throw an error because it has been changed

// ----- Preventing Bugs -----
const LAMBDA_TIMEOUT_MS = 3000;

function configureLambda(functionName) {
    LAMBDA_TIMEOUT_MS = 5000; // This would throw an error because it has been changed
}