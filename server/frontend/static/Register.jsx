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

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <div style={{textAlign:'center', padding:'30px'}}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit} style={{display:'inline-block', textAlign:'left'}}>
        
        <label>Username:</label><br/>
        <input type="text" name="username" value={formData.username} onChange={handleChange} required /><br/><br/>

        <label>First Name:</label><br/>
        <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required /><br/><br/>

        <label>Last Name:</label><br/>
        <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required /><br/><br/>

        <label>Email:</label><br/>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required /><br/><br/>

        <label>Password:</label><br/>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required /><br/><br/>

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
