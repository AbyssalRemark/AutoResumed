import { createRoot } from "react-dom/client";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Welcome from "./Pages/Welcome.jsx"
import LoginPage from "./Pages/LoginPage.jsx"
import RegistrationPage from "./Pages/RegistrationPage.jsx"
import Layout from "./Utils/Layout.jsx"
import UserForm from "./Pages/UserForm.jsx";
import 'bootstrap/dist/css/bootstrap.css';

const App = () => {
  return (
    <BrowserRouter>
      <Layout></Layout>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/welcome" element={<Welcome />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegistrationPage />} />
        <Route path="/create" element={<UserForm />} />
      </Routes>
    </BrowserRouter>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);