import { useState } from "react";

const Login = () => {
  const [shopId, setShopId] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    // Sending as query parameters to match the FastAPI function signature
    const url = `http://localhost:8080/login?shop_id=${shopId}&password=${password}`;

    const response = await fetch(url, { method: "POST" });
    const data = await response.json();

    if (response.ok) alert("Welcome back, " + data.shop_name);
    else alert("Login Failed: " + data.detail);
  };

  return (
    <form onSubmit={handleLogin}>
      <input type="text" placeholder="Enter Shop ID"
        onChange={(e) => setShopId(e.target.value)} required />
      <input type="password" placeholder="Password"
        onChange={(e) => setPassword(e.target.value)} required />
      <button type="submit">Login</button>
    </form>
  );
};
export default Login;