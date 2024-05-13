import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@mui/material";
import { getCurrentUser, signOut } from "aws-amplify/auth";

function Dashboard() {
  const Navigate = useNavigate();

  useEffect(() => {
    const getUser = async () => {
      let user = await getCurrentUser();
      console.log("user", JSON.stringify(user));
      if (!user) {
        Navigate("/login");
      }
    };
    getUser();
  }, []);

  const handleLogoout = () => {
    signOut();
  };

  return (
    <div className="Dashboard">
      <Button
        style={{ margin: "10px" }}
        variant="contained"
        onClick={handleLogoout}
      >
        Logout
      </Button>
    </div>
  );
}

export default Dashboard;
