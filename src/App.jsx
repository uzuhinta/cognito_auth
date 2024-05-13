import { useEffect } from 'react'

import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import Home from './Home'
import Signup from './Signup'
import Dashboard from './Dashboard'
import Login from './Login'

import { Amplify } from 'aws-amplify';
import { getCurrentUser } from 'aws-amplify/auth';

Amplify.configure({
    Auth: {
        Cognito: {
            userPoolId: import.meta.env.VITE_USER_POOL_ID,
            userPoolClientId: import.meta.env.VITE_CLIENT_ID
        }
    }
});


function App() {
  useEffect(()=>{
    let user=getCurrentUser();
      if(user){
        <Navigate to="/dashboard" replace />
      }
  },[]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}/>
        <Route path='/signup' element={<Signup />}/>
        <Route path='/login' element={<Login />}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
