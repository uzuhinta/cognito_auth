import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import userpool from "./userpool";
import { logout } from "./services/authenticate";
import { Button } from "@mui/material";

function Dashboard() {
    const Navigate = useNavigate();

  useEffect(()=>{
    let user=userpool.getCurrentUser();
    console.log(user);
    if(!user){
      Navigate('/login');
    }
  },[]);

  const handleLogoout=()=>{
    logout();
  };

  return (
    <div className='Dashboard'>
      <Button
        style={{margin:"10px"}}
        variant='contained'
        onClick={handleLogoout}
      >
        Logout
      </Button>
    </div>
  )
}

export default Dashboard;