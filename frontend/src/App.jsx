import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Auth from './auth';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </Router>
  );
}

export default App;
