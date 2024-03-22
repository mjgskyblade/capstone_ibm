import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/Register";

function App() {
    return (
      <Router> 
        <Routes>
          <Route path="/register" element={<Register />} /> 
          <Route path="/login" element={<LoginPanel />} />
        </Routes>
      </Router>
    );
  }
  
export default App;
