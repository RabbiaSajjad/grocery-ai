import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Pantry from "./pages/Pantry";
import Planner from "./pages/Planner";
import History from "./pages/History";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/login">Login</Link> |{" "}
        <Link to="/register">Register</Link> |{" "}
        <Link to="/pantry">Pantry</Link> |{" "}
        <Link to="/planner">AI Planner</Link> |{" "}
        <Link to="/history">History</Link>
      </nav>

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/pantry" element={<Pantry />} />
        <Route path="/planner" element={<Planner />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;