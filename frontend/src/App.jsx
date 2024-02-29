import { createRoot } from "react-dom/client";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Welcome from "./Welcome.jsx"
const App = () => {
  return (
<BrowserRouter>
  <h1>html nugget</h1>
  <Welcome></Welcome>
  <Routes>
    <Route path="/welcome" element={<Welcome />} />
  </Routes>
</BrowserRouter>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);