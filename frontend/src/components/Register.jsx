import { useState } from "react";

const Register = () => {
  const [formData, setFormData] = useState({
    shop_id: "",
    password: "",
    name: "",
    location: ""
  });

    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        const response = await fetch("http://127.0.0.1:8080/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
        });

        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || "Registration failed");
        alert("Success!");
      } catch (err) {
        alert("Error: " + err.message);
      }
    };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Create Shop ID"
        onChange={(e) => setFormData({...formData, shop_id: e.target.value})} required />
      <input type="password" placeholder="Password"
        onChange={(e) => setFormData({...formData, password: e.target.value})} required />
      <input type="text" placeholder="Shop Name"
        onChange={(e) => setFormData({...formData, name: e.target.value})} required />
      <input type="text" placeholder="Location"
        onChange={(e) => setFormData({...formData, location: e.target.value})} required />
      <button type="submit">Register</button>
    </form>
  );
};
export default Register;