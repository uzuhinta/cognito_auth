import { Button, TextField } from "@mui/material";
import { signUp } from "aws-amplify/auth";
import { useState } from "react";

function Signup() {
    const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailErr, setEmailErr] = useState('');
  const [passwordErr, setPasswordErr] = useState('');

  const formInputChange = (formField, value) => {
    if (formField === "email") {
      setEmail(value);
    }
    if (formField === "password") {
      setPassword(value);
    }
  };

  const validation = () => {
    return new Promise((resolve,reject)=>{
      if (email === '' && password === '') {
        setEmailErr("Email is Required");
        setPasswordErr("Password is required")
        resolve({email:"Email is Required",password:"Password is required"});
      }
      else if (email === '') {
        setEmailErr("Email is Required")
        resolve({email:"Email is Required",password:""});
      }
      else if (password === '') {
        setPasswordErr("Password is required")
        resolve({email:"",password:"Password is required"});
      }
      else if (password.length < 6) {
        setPasswordErr("must be 6 character")
        resolve({email:"",password:"must be 6 character"});
      }
      else{
        resolve({email:"",password:""});
      }
      reject('')
    });
  };

  const handleClick = () => {
    setEmailErr("");
    setPasswordErr("");
    validation()
      .then(async (res) => {
        if (res.email === '' && res.password === '') {
          let username=email;
          const { isSignUpComplete, userId, nextStep } = await signUp({
            username,
            password,
            options: {
              userAttributes: {
                email
              },
            }
          });
          console.log('isSignUpComplete, userId, nextStep',{isSignUpComplete, userId, nextStep },)
        }
      }, err => console.log(err))
      .catch(err => console.log(err));
  }

  return (
    <div className="signup">

      <div className='form'>
        <div className="formfield">
          <TextField
            value={email}
            onChange={(e) => formInputChange("email", e.target.value)}
            label="Email"
            helperText={emailErr}
          />
        </div>
        <div className='formfield'>
          <TextField
            value={password}
            onChange={(e) => { formInputChange("password", e.target.value) }}
            type="password"
            label="Password"
            helperText={passwordErr}
          />
        </div>
        <div className='formfield'>
          <Button type='submit' variant='contained' onClick={handleClick}>Signup</Button>
        </div>
      </div>

    </div>
  )
}

export  default Signup;