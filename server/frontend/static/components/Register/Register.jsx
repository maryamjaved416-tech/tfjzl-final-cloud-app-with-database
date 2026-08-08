import React, { useState } from 'react';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <form>
        <label>Username:</label>
        <input type="text" name="username" onChange={handleChange} /><br/>

        <label>First Name:</label>
        <input type="text" name="firstName" onChange={handleChange} /><br/>

        <label>Last Name:</label>
        <input type="text" name="lastName" onChange={handleChange} /><br/>

        <label>Email:</label>
        <input type="email" name="email" onChange={handleChange} /><br/>

        <label>Password:</label>
        <input type="password" name="password" onChange={handleChange} /><br/>

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
