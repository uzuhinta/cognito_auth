import { AuthenticationDetails, CognitoUser } from "amazon-cognito-identity-js"
import userpool from "../userpool"

export const authenticate = (email, password)  => {
    return new Promise((res, rej) => {
        const user = new CognitoUser({
            Username: email,
            Pool: userpool
        })

        const authDetails = new AuthenticationDetails({
            Username: email,
            Password: password
        })

        user.authenticateUser(authDetails, {
            onSuccess: (result) => {
                console.log('login success');
                res(result)
            },
            onFailure: (err) => {
                console.log('login failed', err)
                rej(err)
            }
        })
    })
}

export const logout = () => {
    const user = userpool.getCurrentUser();
    user.signOut();
    window.location.href = '/'
}