import { createRoot } from "react-dom/client";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Welcome from "./Welcome.jsx"
import LoginPage from "./LoginPage.jsx"
import RegistrationPage  from "./RegistrationPage.jsx"
import 'bootstrap/dist/css/bootstrap.css';
const App = () => {
  return (
<BrowserRouter>
  <h1>AutoResumed</h1>
  <Link to="/login">login</Link>
  {` `}
  <Link to="/register">register</Link>
  <Routes>
    <Route path="/welcome" element={<Welcome />} />
    <Route path="/login" element={<LoginPage />} />
    <Route path="/register" element={<RegistrationPage />} />
  </Routes>
</BrowserRouter>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);