import { CognitoUserPool } from "amazon-cognito-identity-js";

const poolData = {
    UserPoolId: import.meta.env.VITE_USER_POOL_ID,
    ClientId: import.meta.env.VITE_CLIENT_ID
}
console.log('poolData', poolData)
export default new CognitoUserPool(poolData)